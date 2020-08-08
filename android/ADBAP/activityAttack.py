from os import system
from bs4 import BeautifulSoup
from sys import argv,exit
from threading import Thread

"""

	Usage:

		python3 activityAttack.py <ManifestFile> <PackageName>
			<packagename> is the name of the application which is to be attacked.
			<ManifestFile> is the AndroidManifest.xml file of the app to be attacked.

"""

if len(argv) < 3:
	print("Invalid Args:\rUsage:python3 activityAttack.py <manifestFile> <packageName>")
	exit()




def Activities(soup):

	""" This function returns two lists, list1=exported activites, list2=unexpotedActivities """

	activities = soup.findAll("activity")
	exported = []  # List of exported activies.
	unexported = [] # List of uneported activies.
	for activity in activities:
		try:
			if activity["android:exported"] == "true":
				exported.append(activity["android:name"])
			else:
				unexported.append(activity["android:name"])
		except:
			pass
	return exported, unexported

def PackageName():
	return str(argv[2])

def MakeSoup(f):
	""" This function makes soup to be feed to the Activities() """
	""" Takes one argument: f:= filename """
	f = open(f, "r")
	data = "".join(x.replace("\n", "") for x in f.readlines())
	soup = BeautifulSoup(data, "lxml")
	return soup

def launch(package, component):
	cmd = f"adb shell am start-activity {package}/{component}"
	system(cmd)



package = PackageName()
exp, unexp = Activities(MakeSoup(str(argv[1])))


for ex in exp:
	Thread(target=launch, args=(package, ex,)).start()

for un in unexp:
	Thread(target=launch, args=(package, un,)).start()
