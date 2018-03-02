import inspect
import os
import win32api
from pyicloud import *
from pyicloud.exceptions import PyiCloudAPIResponseError, PyiCloudFailedLoginException
from requests.exceptions import ConnectionError
from pyicloud import exceptions


class Auth:
    def __init__(self, username='none', password='none'):
        self.username = username
        self.password = password
        self.list_year, self.list_month, self.list_images, self.count = [], [], [], 0
        # To check the Path of the script
        self.path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))  # script directory
        # Variable Initialization for log file
        self.message = self.time = self.today = self.phone = self.data_1 = self.data_2 = ''

    def authentication(self):
        try:
            # Authentication
            api = PyiCloudService(self.username, self.password)
            devices = api.devices
            return api, devices

        except PyiCloudAPIResponseError:
            raise PyiCloudFailedLoginException
        except PyiCloudFailedLoginException:
            error = 'Invalid email/password combination.\nPlease try again.'
            win32api.MessageBox(0, error, 'PyCloud - Message', 0x00000000L + 0x00000010L + 0x00020000L)
            return error
        except exceptions.PyiCloudNoDevicesException:
            error = "Enable 'Find My iPhone' on your Device\nand then try again."
            win32api.MessageBox(0, error, 'PyCloud - Message', 0x00000000L + 0x00000010L + 0x00020000L)
            return error
        except ConnectionError:
            error = 'Internet is not working.\nPlease try again.'
            win32api.MessageBox(0, error, 'PyCloud - Message', 0x00000000L + 0x00000010L + 0x00020000L)
            return error


if __name__ == 'main':
    pass
