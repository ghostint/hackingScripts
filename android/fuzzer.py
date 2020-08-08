from manifest import androidManifest
from threading import Thread
from subprocess import Popen, PIPE, STDOUT
from termcolor import cprint
from time import sleep
from sys import argv, exit

class fuzzer:

	def __init__(self, testFile):

		self.testFile = testFile
		self.manifest = androidManifest(self.testFile)

		self.pkg = self.manifest.PackageName() # storing pkg name in self.pkg

		self.log = ""

	def FzzActivities(self):
		""" Method for fuzzing activities. 

			Background:
			==========
			adb shell am start-activity com.android.chrome/org.chromium.chrome.browser.incognito.IncognitoTabLauncher
			

			Descriptions:
			============
			Method to try all the activities in the manifest file.

			Returns:
			=======
			Currently this returns nothing.
			
			
		"""

		for activities in self.manifest.Activities():
			cmd = ["adb", "shell", "am", "start-activity", str(self.pkg)+"/"+activities]
			Thread(target=self.Run, args=(cmd,)).run()
			


	def FzzBroadcast(self):
		"""
		
			Background:
			==========

			> adb shell am broadcast -n com.android/chrome


		"""

		for receiver in self.manifest.Receivers():
			
			cmd = ["adb", "shell", "am", "broadcast", "-n", self.pkg+"/"+receiver]
			Thread(target=self.Run, args=(cmd,)).run()


	def FzzServices(self):
		
		for service in self.manifest.Services():
			cmd = ["adb", "shell", "am", "startservice", "-n", self.pkg+"/"+service]
			Thread(target=self.Run, args=(cmd,)).run()


	def Run(self, cmd):
		output = Popen(cmd, stdout=PIPE, stderr=STDOUT).communicate()[0] # output hold the, return data.
		# sleep(0.5)
		element = "".join(cmd).split("/")[1]
		cprint("[Tested]:"+element, color="cyan")

	
if len(argv) != 2:
	print("Requires a test file to work with: \n")
	print("Give a testFile as argument.\nThanks for using......\n")
	exit()
else:

	f = fuzzer(str(argv[1]))
	f.FzzServices()
	f.FzzActivities()
	f.FzzServices()
	f.FzzBroadcast()
	# sleep(0.1)i

	# f.FzzBroadcast()
