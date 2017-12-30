@echo PyCloud Downloader has been automated will run everyday on 11 PM
@echo off
schtasks /Create /tn PyCloud-Downloader /tr "%cd%\AutomatedDownloader.bat" /sc DAILY /st 23:00:00
pause