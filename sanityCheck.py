import os
import inspect
import pickle
import datetime
import calendar
import win32api
from collections import OrderedDict

try:
    class Sanity:
        def __init__(self, folder):
            self.path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))  # script directory
            self.folder = folder
            self.list_images, self.list_year, self.list_month, self.count = [], [], [], 0
            self.files, self.folders, self.new_month, self.new_year, self.dir = [], [], [], [], OrderedDict()
            self.today = list(str(datetime.date.today()).split('-'))  # gets today's date
            self.time = list(str(datetime.datetime.now().time()).split(':'))  # gets current time
            self.time = self.time[0] + ':' + self.time[1]
            self.message = ''

        def check(self):
            # Reading input data
            try:
                with open(self.path + '/' + self.folder + '/AppData/AppData.dat', "rb") as f:
                    self.list_year = pickle.load(f)
                    self.list_month = pickle.load(f)
                    self.list_images = pickle.load(f)
                    self.count = pickle.load(f)
                    f.close()
            except IOError:
                self.folder = self.folder + '/AppData'
                os.makedirs(os.path.join(self.path, self.folder))
                return

            for directory, dirname, filename in os.walk(self.path + '/' + self.folder + '/Photos'):
                if filename != []:
                    self.files.append(filename)
                if dirname != []:
                    self.folders.append(dirname)
            self.files = [i for j in self.files for i in j]
            self.count = len(self.files)
            for picture in self.list_images:
                if picture not in self.files:
                    self.list_images.remove(picture)
                    self.message += '{} deleted\n'.format(picture)
            self.new_year = self.folders[0]
            for i in self.folders[0]:
                self.dir[i] = ''
            self.folders.remove(self.folders[0])
            for k in self.dir.keys():
                for item in self.folders[0]:
                    self.dir[k] = item + '_' + k
                    self.new_month.append(self.dir[k])
                self.folders.remove(self.folders[0])
            for month in self.list_month:
                if month not in self.new_month:
                    self.list_month.remove(month)
                    self.message += '{} Sub-directory deleted\n'
            for year in self.list_year:
                if year not in self.new_year:
                    self.list_month.remove(year)
                    self.message += '{} Directory deleted\n'
            self.message += 'Total Images: {}, Date of Deletion: {} {}, {} at {}\n'.format(self.count,
                                                                                           self.today[2],
                                                                                           calendar.month_abbr[
                                                                                               int(self.today[
                                                                                                       1])],
                                                                                           self.today[0],
                                                                                           self.time)
            with open(self.path + '/' + self.folder + '/AppData/AppData.dat', "wb") as f:
                pickle.dump(self.list_year, f)
                pickle.dump(self.list_month, f)
                pickle.dump(self.list_images, f)
                pickle.dump(self.count, f)
                f.close()
            # Saving application Log to a text file
            log_file = open(self.path + '/' + self.folder + '/AppData/AppLog.txt', 'a+')
            log_file.writelines(self.message + '--------------------------------------------------------------\n')
except Exception:
    win32api.MessageBox(0, 'Some problem occurred.\nPlease try again.', 'PyCloud - Message',
                        0x00000000L + 0x00000010L + 0x00020000L)


if __name__ == '__main__':
    pass
