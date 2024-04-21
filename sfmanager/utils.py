from time import sleep
from loguru import logger

import pkg_resources
import httpx
import subprocess
import sys
import os

logger.add("logs.log", level="DEBUG")

def whatIsIt():
	print("")
	print("Hello dear user!")
	sleep(1)
	print("Thanks for download my library!")
	sleep(2)
	print("Homepage on github: https://github.com/GrandTheBest/sfmanager")
	sleep(2)
	print("Issues page on github: https://github.com/GrandTheBest/sfmanager/issues")
	sleep(2)
	print("By this library you can work with text, image and other files.")
	sleep(2)
	print("You can read, set, add and replace content in text files.")
	sleep(2)
	print("Also you can create, copy, move, rename and remove any files.")
	sleep(2)
	print("That's all. Stay tuned!")
	sleep(2)
	print("Thanks for using! Good luck!")
	sleep(1)

@logger.catch
def checkUpdates():
	logger.info("Checking for updates")

	version = pkg_resources.get_distribution("sfmanager").version
	updates = httpx.get("https://raw.githubusercontent.com/GrandTheBest/sfmanager/main/version")

	if updates.status_code == 200:
		values = updates.text[0:5]

		if str(version) == str(values):
			logger.success("No update required")
			whatIsIt()
		else:
			logger.info("Downloading an update using pip")

			subprocess.check_call([sys.executable, "-m", "pip", "install", "sfmanager==" + values])
			logger.success("sfmanager updated, changes will take effect after restart")

			os.chdir(os.path.join(pkg_resources.get_distribution("sfmanager").location, "sfmanager"))
checkUpdates()