from pexpect import spawn
from time import sleep
from sys import exit

class ADB:
	
	"""
	This class is used to interact with the adb, using PEXPECT.
		Class can be used to send command to adb over pexpect, by calling the Run() method on a class instance.

		Requires 2 variables to run:
			1. CMD := Command to be run on the adb 
			2. IDENT := Device identifier used in the child.expect()
			3. showresult := boolean, optional, set True for result output.

		===========================
		Using this Class
		===========================

		adb = ADB("ls /etc/", "OnePlus", showresult=True).Run()

	"""

	def __init__(self, cmd, ident, showresult=False):
		self.cmd = cmd
		self.ident = str(ident)+".*"
		self.adb = spawn("adb shell")
		self.result = showresult

		self.ok = 1

		self.out = ""

	def Run(self):
		return self.__SendCommand()

	def __SendCommand(self):
		adb = self.adb
		adb.expect(self.ident)
		adb.sendline(self.cmd)
		adb.expect(self.ident)
		self.out += str(adb.before)
		sleep(0.1)
		return (str(self.out))
		exit()

# adb = `ADB("pm list packages", "OnePlus").Run()
# print(adb)