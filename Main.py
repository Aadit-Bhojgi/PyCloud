from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
import sys
import os
import inspect
import win32api
import Auth
import sanityCheck
import GUI
import Instruction
import LogIn
import Broswer
import pickle
import calendar
import datetime
from requests.exceptions import ConnectionError
from pyicloud import PyiCloudService, exceptions

user = user_password = ''


def message_alert(data, alert):
    msg = QtGui.QMessageBox()
    msg.setWindowIcon(QtGui.QIcon(":/Images/AppleLogo.png"))
    msg.setText(data)
    if alert == 'exit':
        msg.setIcon(QtGui.QMessageBox.Warning)
        msg.addButton(QtGui.QMessageBox.Ok)
        msg.addButton(QtGui.QMessageBox.Cancel)
    if alert == 'info':
        msg.setIcon(QtGui.QMessageBox.Information)
        msg.addButton(QtGui.QMessageBox.Ok)
    if alert == 'action':
        msg.setIcon(QtGui.QMessageBox.Information)
        msg.addButton(QtGui.QMessageBox.Ok)
        msg.addButton(QtGui.QMessageBox.Cancel)
    msg.setDefaultButton(QtGui.QMessageBox.Ok)
    result = msg.exec_()
    if result == msg.Ok:
        return 1
    else:
        return 0


class PyMain(QtGui.QWidget, GUI.Ui_Pycloud):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.password.setEchoMode(QtGui.QLineEdit.Password)
        self.commandLinkButton.clicked.connect(self.populate)
        self.commandLinkButton_2.clicked.connect(self.instruction)
        self.dialog = PyInst()
        self.thread = GetThread()
        self.api = Auth.PyiCloudService
        self.login = PyMain
        self.battery = ''

    def instruction(self):
        self.dialog.hide()
        self.dialog.show()

    def populate(self):
        if not self.thread.isRunning():
            global user, user_password
            user = self.username.text()
            user_password = self.password.text()
            self.thread = GetThread(self.username.text(), self.password.text())
            self.thread.authResult.connect(self.handle_auth_result)
            self.thread.start()

    def handle_auth_result(self, result):
        if form.isVisible():
            if isinstance(result, Auth.PyiCloudService):
                self.api = result
                user_name = str(self.api.iphone).split(":")[1].strip()
                phone_name = str(self.api.iphone).split(':')[0].strip()
                battery = str(round(self.api.iphone.status()['batteryLevel'], 2) * 100).split('.')[0] + '%'
                self.login = PyLogin(self.api, user_name, phone_name, battery)
                self.login.hide()
                self.login.show()
                form.hide()
                if self.dialog.isVisible():
                    self.dialog.reject()
            else:
                print result

    def closeEvent(self, event):
        result = message_alert('Do you want to Exit?', 'exit')
        if result:
            event.accept()
            # This nested if has very import aspect in this code
            if self.thread.isRunning():
                self.thread.terminate()
            if self.dialog.isVisible():
                self.dialog.reject()
            try:
                if isinstance(self.login, PyLogin):
                    self.login.reject()
            except AttributeError:
                pass
        else:
            event.ignore()


class GetThread(QThread):
    authResult = QtCore.pyqtSignal(object)

    def __init__(self, username='none', password='none'):
        QThread.__init__(self)
        self.username = str(username)
        self.password = str(password)
        self.user = Auth.Auth(self.username, self.password)

    def authentication(self):
        self.user = Auth.Auth(self.username, self.password)
        result = self.user.authentication()
        self.authResult.emit(result)

    def run(self):
        self.authentication()


class PyInst(QtGui.QDialog, Instruction.Ui_Dialog):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.label_13.setOpenExternalLinks(True)


class PyLogin(QtGui.QDialog, LogIn.Ui_PyLogin):
    def __init__(self, api, user_name='', phone_name='', battery=''):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.show_result.hide()
        self.doc = QtGui.QTextDocument()
        self.api = api
        self.html_format_1 = '<html><head/><body><p><span style=" color:#ececec; font-size:25px">'
        self.html_format_2 = '</span></p></body></html>'
        self.user_name.setText(self.html_format_1 + user_name + self.html_format_2)
        self.user_name.text = self.doc.toHtml()
        self.phone_name.setText(self.html_format_1 + phone_name + self.html_format_2)
        self.phone_name.text = self.doc.toHtml()
        self.battery_status.setText(self.html_format_1 + battery + self.html_format_2)
        self.battery_status.text = self.doc.toHtml()
        self.goback.clicked.connect(self.back)
        self.thread_play = AlertThread(self.api)
        self.thread_update = UpdateThread(self.api)
        self.thread_lost = LostThread(self.api)
        self.thread_locate = LocateThread(self.api)
        self.play_sound.clicked.connect(self.playing)
        global user, user_password
        self.username = str(user)
        self.password = str(user_password)
        self.download.clicked.connect(self.download_photos)
        self.timer = QtCore.QTimer(self)  # Timer to update user info
        self.timer.timeout.connect(self.updating)
        self.timer.start(10)  # 10 milliseconds
        self.lost.clicked.connect(self.alert)
        self.map.clicked.connect(self.locate)
        self.locate_phone = Broswer.Locate()
        self.thread_delete = DeleteThread(self.username, self.password)
        self.delete_button.clicked.connect(self.delete_photos)
        self.download.clicked.connect(self.download_photos)
        self.thread_download = PhotosThread(self.api)
        self.show_result.setReadOnly(True)
        self.automation.clicked.connect(self.automate)
        # To check the Path of the script
        self.path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))  # script directory
        self.name = user_name.strip()

    def credentials(self):
        a = open(self.path + '\Automation\Credentials\Credentials.txt', 'w+')
        size = len(self.username)
        for_index = 1
        for i in self.password:
            a.writelines(str(ord(i) + for_index) + '%')
            for_index += 1
        a.writelines('*/*/')
        for i in self.username:
            a.writelines(str(ord(i) + size) + '@')
            size -= 1
        a.writelines('@*@' + str(len(self.username)))
        a.close()

    def automate(self):
        # Saving username and password (ciphered)
        if os.path.exists(self.path + '/Automation/Credentials/Credentials.txt'):
            result = message_alert('Do you want to over-write the previously saved credentials?\n'
                                   'NOTE : This may affect your already set automation\n(If credentials'
                                   ' will not be the same)', 'action')

            if result:
                self.credentials()
                QtGui.QDesktopServices.openUrl(QtCore.QUrl('Downloader.bat'))
        else:
            result = message_alert('By pressing OK your credentials for the logged in Apple ID will be saved (Ciphered)'
                                   ' in this system.\nDo you want to continue?', 'action')
            if result:
                os.makedirs(os.path.join(self.path, 'Automation\Credentials'))
                self.credentials()
                QtGui.QDesktopServices.openUrl(QtCore.QUrl('Downloader.bat'))

    def back(self):
        form.hide()
        if form.isMinimized():
            form.showNormal()
        form.show()

    def updating(self):
        if not self.thread_update.isRunning():
            self.thread_update.updateResult.connect(self.finalupdate)
            self.thread_update.start()

    def finalupdate(self, result):
        result = str(result).split(':')
        self.user_name.setText(self.html_format_1 + result[0] + self.html_format_2)
        self.user_name.text = self.doc.toHtml()
        self.phone_name.setText(self.html_format_1 + result[1] + self.html_format_2)
        self.phone_name.text = self.doc.toHtml()
        self.battery_status.setText(self.html_format_1 + result[2] + self.html_format_2)
        self.battery_status.text = self.doc.toHtml()

    def is_unique(self):
        if not self.thread_download.isRunning() and not self.thread_delete.isRunning() \
                and not self.thread_lost.isRunning() and not self.thread_locate.isRunning() \
                and not self.thread_play.isRunning():
            return 1
        else:
            return 0

    def download_photos(self):
        if self.is_unique():
            self.sanity = sanityCheck.Sanity(self.name)
            self.sanity.check()
            self.show_result.show()
            self.move_labels()
            self.show_result.setText('Downloading Photos Please Wait.')
            self.thread_download = PhotosThread(self.api)
            self.thread_download.alert.connect(self.photo_result)
            self.thread_download.start()

    def delete_photos(self):
        if self.is_unique():
            self.sanity = sanityCheck.Sanity(self.name)
            self.sanity.check()
            folder = str(self.api.iphone).split(":")[1].strip()  # For checking the Internet Connection
            path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))  # script directory
            filter = "Photos and Videos (*.JPG *.PNG *.MOV *.mp4 *gif);;All Files (*)"
            selected = QtGui.QFileDialog.getOpenFileNamesAndFilter(self, "Select Photos",
                                                                   path + '/' + folder + '/Photos',
                                                                   filter)
            delete_selected = []
            for i in range(0, len(selected[0])):
                delete_selected.append(str(selected[0][i]))
            if len(delete_selected) > 0:
                self.show_result.show()
                self.move_labels()
                self.show_result.setText('Deleting Photos Please Wait.')
                self.thread_delete = DeleteThread(self.username, self.password, delete_selected)
                self.thread_delete.alert.connect(self.photo_result)
                self.thread_delete.start()

    def move_labels(self):
        self.download.move(680, 340)
        self.download_label.move(740, 350)
        self.delete_button.move(680, 420)
        self.delete_label.move(740, 430)
        self.show_result.clear()

    def clear_text(self):
        self.show_result.clear()
        self.show_result.hide()
        self.download.move(230, 400)
        self.download_label.move(290, 410)
        self.delete_button.move(540, 400)
        self.delete_button.move(540, 400)
        self.delete_label.move(590, 410)

    def photo_result(self, result):
        if result == 'error':
            self.clear_text()
        elif result == 'finished_downloading':
            ret = message_alert('Photo(s) Downloaded', 'info')
            if ret:
                self.clear_text()
        elif result == 'finished_deleting':
            ret = message_alert('Photo(s) Deleted', 'info')
            if ret:
                self.clear_text()
        else:
            self.show_result.setText(result)

    def alert(self):
        if self.is_unique():
            self.thread_lost = LostThread(self.api, str(self.lost_phonne.text()), str(self.lost_message.toPlainText()))
            self.thread_lost.alert.connect(self.final_play_lost)
            self.thread_lost.start()

    def playing(self):
        if self.is_unique():
            self.thread_play = AlertThread(self.api)
            self.thread_play.alert.connect(self.final_play_lost)
            self.thread_play.start()

    def final_play_lost(self, alert):
        message_alert(alert, 'info')

    def locate(self):
        if self.is_unique():
            self.thread_locate.alert.connect(self.map_open)
            self.thread_locate.start()

    def map_open(self, result):
        print result

    def closeEvent(self, event):
        result = message_alert('Do you want to Exit?', 'exit')
        if result:
            self.timer.stop()
            event.accept()
            exit(0)
        else:
            event.ignore()


class UpdateThread(QThread):
    updateResult = QtCore.pyqtSignal(object)

    def __init__(self, api):
        QThread.__init__(self)
        self.api = api

    def update(self):
        try:
            user_name = str(self.api.iphone).split(":")[1]
            phone_name = str(self.api.iphone).split(":")[0]
            battery_status = str(round(self.api.iphone.status()['batteryLevel'], 2) * 100).split('.')[0] + '%'
            result = user_name + ':' + phone_name + ':' + battery_status
            self.updateResult.emit(result)
        except ConnectionError:
            print 'No Internet'

    def run(self):
        self.update()


class AlertThread(QThread):
    alert = QtCore.pyqtSignal(object)

    def __init__(self, api):
        QThread.__init__(self)
        self.api = api

    def play(self):
        try:
            battery = str(round(self.api.iphone.status()['batteryLevel'], 2) * 100).split('.')[
                          0] + '%'  # For checking the Internet Connection
            self.api.iphone.play_sound()
            self.alert.emit('Alert sent on your iPhone.')
        except ConnectionError:
            win32api.MessageBox(0, 'Internet is not working.\nPlease try again.', 'PyCloud - Message',
                                0x00000000L + 0x00000010L + 0x00020000L)

    def run(self):
        self.play()


class LostThread(QThread):
    alert = QtCore.pyqtSignal(object)

    def __init__(self, api, phone='none', message='none'):
        QThread.__init__(self)
        self.api = api
        self.phone = phone
        self.message = message

    def play(self):
        try:
            battery = str(round(self.api.iphone.status()['batteryLevel'], 2) * 100).split('.')[
                          0] + '%'  # For checking the Internet Connection
            self.api.iphone.lost_device(self.phone, self.message)
            self.alert.emit('Lost message sent to your iPhone.\nReader may contact you soon.')
        except ConnectionError:
            win32api.MessageBox(0, 'Internet is not working.\nPlease try again.', 'PyCloud - Message',
                                0x00000000L + 0x00000010L + 0x00020000L)

    def run(self):
        self.play()


class LocateThread(QThread):
    alert = QtCore.pyqtSignal(object)

    def __init__(self, api):
        QThread.__init__(self)
        self.api = api

    def play(self):
        try:
            latitude = str(self.api.iphone.location()['latitude'])
            longitude = str(self.api.iphone.location()['longitude'])
            if win32api.MessageBox(0, 'Important\nPress CTRL+W in order to exit further', 'PyCloud - Message',
                                   0x00000001L + 0x00000040L + 0x00020000L) == 1:
                self.locate_phone = Broswer.Locate(latitude, longitude)
                self.locate_phone.locate_phone()
                result = latitude + ' ' + longitude
                self.alert.emit(result)
        except ConnectionError:
            win32api.MessageBox(0, 'Internet is not working.\nPlease try again.', 'PyCloud - Message',
                                0x00000000L + 0x00000010L + 0x00020000L)

    def run(self):
        self.play()


class DeleteThread(QThread):
    alert = QtCore.pyqtSignal(object)

    def __init__(self, username='none', password='none', list=[]):
        QThread.__init__(self)
        self.username = username
        self.password = password
        self.list = list
        self.delete_selected = {}
        self.flag = False
        self.warning = False
        self.result = ''
        self.count = 0

    def delete(self):
        try:
            for i in self.list:
                self.delete_selected[i.split('\\')[-1].strip("'")] = i
            self.api = PyiCloudService(str(self.username), str(self.password))  # For checking the Internet Connection
            self.folder = str(self.api.iphone).split(":")[1].strip()  # For checking the Internet Connection
            self.path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))  # script directory
            self.load = PhotosThread(self.api)
            self.load.loading_data(self.folder)
            self.count = self.load.count
            for photo in self.delete_selected.keys():
                self.flag = False
                for lib_photo in self.api.photos.all:
                    if lib_photo.filename == photo:
                        lib_photo.delete()
                        if os.path.exists(self.delete_selected[photo]):
                            os.remove(self.delete_selected[photo])
                        self.load.list_images.remove(photo)
                        self.load.count -= 1
                        self.count = self.load.count
                        for empty_folder in self.load.list_month:
                            temp = empty_folder
                            year = empty_folder.split('_')[1]
                            month = empty_folder.split('_')[0]
                            if not os.listdir(self.path + '/' + self.folder + '/Photos/' + year + '/' + month):
                                os.rmdir(self.path + '/' + self.folder + '/Photos/' + year + '/' + month)
                                self.load.list_month.remove(temp)
                        for empty_folder in self.load.list_year:
                            if not os.listdir(self.path + '/' + self.folder + '/Photos/' + empty_folder):
                                os.rmdir(self.path + '/' + self.folder + '/Photos/' + empty_folder)
                                self.load.list_year.remove(empty_folder)
                        with open(self.path + '/' + self.folder + '/AppData/AppData.dat', "wb") as f:
                            pickle.dump(self.load.list_year, f)
                            pickle.dump(self.load.list_month, f)
                            pickle.dump(self.load.list_images, f)
                            pickle.dump(self.load.count, f)
                            f.close()
                        self.result += photo + ' deleted\n'
                        self.alert.emit(self.result)
                        self.flag = True
                        break
                if self.flag is False:
                    if self.warning is False:
                        if win32api.MessageBox(0, 'Photo(s) selected is/are not present in your\niCloud Photo Library.'
                                                  '\nDo you really want to delete these photos from your system?',
                                               'PyCloud - Message', 0x00000001L + 0x00000010L + 0x00020000L) == 1:
                            self.warning = True
                    if os.path.exists(self.delete_selected[photo]) and self.warning is True:
                        os.remove(self.delete_selected[photo])
                        self.count -= 1
                        self.result += photo + ' deleted\n'
                        self.alert.emit(self.result)
        except ConnectionError, exceptions.PyiCloudAPIResponseError:
            win32api.MessageBox(0, 'Internet is not working.\nPlease try again.', 'PyCloud - Message',
                                0x00000000L + 0x00000010L + 0x00020000L)
            self.alert.emit('error')
        except:
            win32api.MessageBox(0, 'You messed up with your directory.\nNow you can manually delete photos\n'
                                   'or to fix this delete the whole directory(with your username) and download your'
                                   ' Photos again.', 'PyCloud - Message',
                                0x00000000L + 0x00000010L + 0x00020000L)
            self.alert.emit('error')

    def saving_data(self, api, folder):
        try:
            self.today = list(str(datetime.date.today()).split('-'))  # gets today's date
            self.time = list(str(datetime.datetime.now().time()).split(':'))  # gets current time
            self.time = self.time[0] + ':' + self.time[1]
            self.result += 'Total Images: {}, Date of Deletion: {} {}, {} at {}\n'.format(self.count,
                                                                                          self.today[2],
                                                                                          calendar.month_abbr[
                                                                                              int(self.today[
                                                                                                      1])],
                                                                                          self.today[0],
                                                                                          self.time)
            self.alert.emit(self.result)
            # Saving application Log to a text file
            log_file = open(self.path + '/' + folder + '/AppData/AppLog.txt', 'a+')
            log_file.writelines(self.result + '--------------------------------------------------------------\n')
            log_file.close()
        except ConnectionError, exceptions.PyiCloudAPIResponseError:
            win32api.MessageBox(0, 'Internet is not working.\nPlease try again.', 'PyCloud - Message',
                                0x00000000L + 0x00000010L + 0x00020000L)
            self.alert.emit('error')

    def run(self):
        self.delete()
        self.saving_data(self.api, self.folder)
        self.alert.emit('finished_deleting')


class PhotosThread(QThread):
    alert = QtCore.pyqtSignal(object)

    def __init__(self, api):
        QThread.__init__(self)
        self.api = api
        self.list_year, self.list_month, self.list_images, self.count = [], [], [], 0
        self.message = self.time = self.today = self.phone = ''
        # To check the Path of the script
        self.path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))  # script directory

    def loading_data(self, folder):
        # Reading input data
        if os.path.exists(self.path + '/' + folder + '/AppData/AppData.dat'):
            with open(self.path + '/' + folder + '/AppData/AppData.dat', "rb") as f:
                self.list_year = pickle.load(f)
                self.list_month = pickle.load(f)
                self.list_images = pickle.load(f)
                self.count = pickle.load(f)
                f.close()
        else:
            return

    def download_initiate(self, api, folder):
        try:
            # Downloading All Photos from user's iCloud account.
            for photo in api.photos.all:
                if photo.filename not in self.list_images:
                    download = photo.download()
                    info = str(photo.created).split()[0].split('-')
                    year = str(info[0])
                    month = calendar.month_name[int(info[1])]
                    if year not in self.list_year:
                        os.makedirs(os.path.join(self.path + '/' + folder + '/Photos', year))
                        self.list_year.append(year)
                    if (month + '_' + year) not in self.list_month:
                        os.makedirs(os.path.join(self.path + '/' + folder + '/Photos', year, month))
                        self.list_month.append((month + '_' + year))
                    self.list_images.append(photo.filename)
                    with open(self.path + '/' + folder + '/Photos/{}/{}/{}'.format(year, month,
                                                                                   photo.filename),
                              'wb') as opened_file:
                        opened_file.write(download.raw.read())
                        opened_file.close()
                    self.message += '{} downloaded, Date of creation: {} {}, {}\n'.format(photo.filename, info[2],
                                                                                          calendar.month_abbr[
                                                                                              int(info[1])],
                                                                                          info[0])
                    self.alert.emit(self.message)
                    self.count += 1
                    with open(self.path + '/' + folder + '/AppData/AppData.dat', "wb") as f:
                        pickle.dump(self.list_year, f)
                        pickle.dump(self.list_month, f)
                        pickle.dump(self.list_images, f)
                        pickle.dump(self.count, f)
                        f.close()
        except ConnectionError:
            error = 'Internet is not working.\nPlease try again.'
            win32api.MessageBox(0, error, 'PyCloud - Message', 0x00000000L + 0x00000010L + 0x00020000L)

    def saving_data(self, api, folder):
        self.phone = 'Phone: ' + str(api.devices[0]).split(':')[0] + '\n' + 'User:' + \
                     str(api.devices[0]).split(':')[1]
        self.today = list(str(datetime.date.today()).split('-'))  # gets today's date
        self.time = list(str(datetime.datetime.now().time()).split(':'))  # gets current time
        self.time = self.time[0] + ':' + self.time[1]
        self.message += 'Total Images: {}, Date of Download: {} {}, {} at {}\n'.format(self.count,
                                                                                       self.today[2],
                                                                                       calendar.month_abbr[
                                                                                           int(self.today[
                                                                                                   1])],
                                                                                       self.today[0],
                                                                                       self.time)
        self.alert.emit(self.message)
        # Saving application Log to a text file
        log_file = open(self.path + '/' + folder + '/AppData/AppLog.txt', 'a+')
        log_file.writelines(self.message + '--------------------------------------------------------------\n')
        log_file.close()

    def download(self):
        try:
            self.message = ''
            folder = str(self.api.iphone).split(":")[1].strip()  # For checking the Internet Connection
            self.loading_data(folder)
            self.download_initiate(self.api, folder)
            self.saving_data(self.api, folder)
        except ConnectionError:
            win32api.MessageBox(0, 'Internet is not working.\nPlease try again.', 'PyCloud - Message',
                                0x00000000L + 0x00000010L + 0x00020000L)
            self.result = 'No Internet'
            self.alert.emit(self.result)

    def run(self):
        self.download()
        self.result = 'finished_downloading'
        self.alert.emit(self.result)


def main():
    app = QtGui.QApplication(sys.argv)
    global form
    form = PyMain()
    # form.setWindowFlags(form.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
