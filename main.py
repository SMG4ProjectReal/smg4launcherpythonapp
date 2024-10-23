from asyncio import wait
import urllib.request
import random

program1_dicter = {
            "1": "Windows XP End of support remake",
            }

program2_dicter = {
            "2": "JD2017 Controller Fix by Rama",
            }

program3_dicter = {
            "3": "PS1VideoCDCreator by Newbilius",
            }

print("Welcome to the SMG4 Launcher Python Version The Nightly Edition")
print("1. Windows XP End of support, 2. JD2017 Controller Fix by Rama, PS1VideoCDCreator by Newbilius")

user_input = input("Type the Downloading File:")

while True: 
   if user_input in program1_dicter.keys():
    urllib.request.urlretrieve("https://smg4project.github.io/smg4launcherserver/XP.End.of.support.application.exe", "XP.End.of.support.application.exe")
    input("Done! now it program closing you can open again")
    wait(1)
    quit()
   if user_input in program2_dicter.keys():
      urllib.request.urlretrieve("https://smg4project.github.io/smg4launcherserver/jd17pc_controller_fixer.bat", "jd17pc_controller_fixer.bat")
      input("Done! now it program closing you can open again")
      wait(1)
      quit()
   if user_input in program3_dicter.keys():
      urllib.request.urlretrieve("https://github.com/Newbilius/PS1VideoCDCreator/releases/download/v1.1/PS1VideoCDCreator_1.1.7z.7z", "PS1VideoCDCreator_1.1.7z.7z")
      input("Done! now it program closing you can open again")
      wait(1)
      quit()