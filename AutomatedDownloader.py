import calendar
import datetime
import inspect
import os
import pickle
import win32api
import sanityCheck
from pyicloud import *
from pyicloud.exceptions import PyiCloudAPIResponseError, PyiCloudFailedLoginException
from requests.exceptions import ConnectionError


class Cmd:
    def __init__(self):
        self.username = self.password = ''
        self.list_year, self.list_month, self.list_images, self.count = [], [], [], 0
        # To check the Path of the script
        self.path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))  # script directory
        # Variable Initialization for log file
        self.message = self.time = self.today = self.phone = ''
        self.dev = 0

    def get_password_username(self):
        # Deciphering your password
        a = open(self.path + '/Automation/Credentials/Credentials.txt', 'r+')
        raw = a.read().split('*/*/')
        count = 1
        s1 = ''
        l1 = []
        for i in raw[0]:
            if i == '%':
                l1.append(int(s1) - count)
                count += 1
                s1 = ''
                continue
            s1 += i
        for i in l1:
            self.password += chr(i)
        # Deciphering your username
        l2 = []
        raw1 = raw[1].split('@*@')
        username = str(raw1[0])
        size = int(raw1[1].split('ved')[0])
        s = ''
        for i in username:
            if i == '@':
                l2.append(int(s) - size)
                size -= 1
                s = ''
                continue
            s += i
        for i in l2:
            self.username += chr(i)
        self.dev = int(raw1[1].split('ved')[1])

    def download_photos(self):
        try:
            # Deciphering Username and password
            self.get_password_username()
            # Authentication
            api = PyiCloudService(self.username, self.password)
            user_name = str(api.devices[self.dev]).split(":")[1].strip()

        except PyiCloudAPIResponseError:
            raise PyiCloudFailedLoginException
        except PyiCloudFailedLoginException:
            error = 'Invalid email/password combination.\nPlease try again.'
            win32api.MessageBox(0, error, 'PyCloud - Message', 0x00000000L + 0x00000010L + 0x00020000L)
            return error
        except ConnectionError:
            error = 'Internet is not working.\nPlease try again.'
            win32api.MessageBox(0, error, 'PyCloud - Message', 0x00000000L + 0x00000010L + 0x00020000L)
            return error
        try:
            self.sanity = sanityCheck.Sanity(user_name)
            self.sanity.check()
        except:
            win32api.MessageBox(0, "Some problem occurred.\nPlease try again.\nTry deleting the folder(with your "
                                   "device's name)", 'PyCloud - Message', 0x00000000L + 0x00000010L + 0x00020000L)

        # Reading input data
        try:
            with open(self.path + '/' + user_name + '/AppData/AppData.dat', "rb") as f:
                self.list_year = pickle.load(f)
                self.list_month = pickle.load(f)
                self.list_images = pickle.load(f)
                self.count = pickle.load(f)
                f.close()
        except IOError:
            if not os.path.exists(user_name + '/AppData'):
                folder = user_name + '/AppData'
                os.makedirs(os.path.join(self.path, folder))
            return
        # Downloading All Photos from user's iCloud account.
        for photo in api.photos.all:
            if photo.filename not in self.list_images:
                download = photo.download()
                info = str(photo.created).split()[0].split('-')
                year = str(info[0])
                month = calendar.month_name[int(info[1])]
                if year not in self.list_year:
                    os.makedirs(os.path.join(self.path + '/' + user_name + '/Photos', year))
                    self.list_year.append(year)
                if (month + '_' + year) not in self.list_month:
                    os.makedirs(os.path.join(self.path + '/' + user_name + '/Photos', year, month))
                    self.list_month.append((month + '_' + year))
                self.list_images.append(photo.filename)
                with open(self.path + '/' + user_name + '/Photos/{}/{}/{}'.format(year, month, photo.filename),
                          'wb+') as opened_file:
                    opened_file.write(download.raw.read())
                    opened_file.close()
                self.message += '{} downloaded, Date of creation: {} {}, {}\n'.format(photo.filename, info[2],
                                                                                      calendar.month_abbr[int(info[1])],
                                                                                      info[0])
                print '{} downloaded, Date of creation: {} {}, {}'.format(photo.filename, info[2],
                                                                          calendar.month_abbr[int(info[1])],
                                                                          info[0])
                self.count += 1
                with open(self.path + '/' + user_name + '/AppData/AppData.dat', "wb") as f:
                    pickle.dump(self.list_year, f)
                    pickle.dump(self.list_month, f)
                    pickle.dump(self.list_images, f)
                    pickle.dump(self.count, f)
                    f.close()

        self.phone = 'Phone: ' + str(api.devices[0]).split(':')[0] + '\n' + 'User:' + str(api.devices[0]).split(':')[1]
        self.today = list(str(datetime.date.today()).split('-'))  # gets today's date
        self.time = list(str(datetime.datetime.now().time()).split(':'))  # gets current time
        self.time = self.time[0] + ':' + self.time[1]
        self.message += 'Total Images: {}, Date of Download: {} {}, {} at {}\n'.format(self.count,
                                                                                       self.today[2],
                                                                                       calendar.month_abbr[
                                                                                           int(self.today[1])
                                                                                       ],
                                                                                       self.today[0],
                                                                                       self.time)
        print 'Total Images: {}, Date of Download: {} {}, {} at {}'.format(self.count,
                                                                           self.today[2],
                                                                           calendar.month_abbr[
                                                                               int(self.today[1])
                                                                           ],
                                                                           self.today[0],
                                                                           self.time)

        # self.send_mail(self.username, str(self.today[2]), calendar.month_abbr[int(self.today[1])], str(self.today[0]))
        # Saving application Log to a text file
        log_file = open(self.path + '/' + user_name + '/AppData/AppLog.txt', 'a+')
        log_file.writelines(self.message + '--------------------------------------------------------------\n')
        log_file.close()
        win32api.MessageBox(0, self.phone + '\n' + self.message, 'PyCloud - Message',
                            0x00000001L + 0x00000040L + 0x00020000L)


if __name__ == '__main__':
    Cmd().download_photos()
