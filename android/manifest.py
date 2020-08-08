#!/bin/python3
from sys import argv,exit
from bs4 import BeautifulSoup

class androidManifest:

	"""

		Parameters:
		===========
		manifestFile: <AndroidManifest.xml>

		
		Methods:
		=======
	
		Activities(): returns all activites [both exported as well as unexported] from the manifest file.(return type LIST)
		Services(): returns all the services present manifest file.(return type LIST)
		Providers(): returns the Provider's Authority name.(return type LIST)
		Receivers(): returns all the receivers names.(return type LIST)
		Permissions(): returns all the permissions used by app.(return type LIST)
		MetaData(): return data from meta tags.(return type LIST)
		Actions(): returns all the actions present in the manifest file.(return type LIST)

		PackageName(): returns package name.(return type STRING)

		
		Requirements:
		============
		BeautifulSoup Module.
		Lxml module (optional).
	


		Description:
		============
		manifest = androidmanifest("<pathToAndroidManifestFile>")
		pkgname = manifest.PackageName()
		activities = manifest.Activities() # activities holds a list of activities from manfiest file.
		actions = manifest.Actions() # List of actions.



	"""


	def __init__(self, manifestFile):	
		self.f = manifestFile # Manifest file.

		self.soup = self.MakeSoup(self.f) # Soup made from manifest file.


	def PackageName(self):

		manifest = self.soup.find("manifest")

		return manifest["package"]



	def Activities(self):

		""" This function returns two lists, list1=exported activites, list2=unexpotedActivities """

		activities = self.soup.findAll("activity")
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
		return (exported+unexported)



	def Services(self):
		services = self.soup.findAll("service")
		return [service["android:name"] for service in services]


	def Providers(self):
		""" Only exported Providers """
		providers = self.soup.findAll("provider")
		# print(len(providers))
		providers = [p["android:name"] for p in providers if p["android:exported"]=="true" ]
		return (providers)

	def Receivers(self):
		""" Only exported receivers. """
		recvs = self.soup.findAll("receiver")
		# exported = []
		receivers = []
		for rec in recvs:
			try:

				receivers.append(rec["android:name"])
				# if rec["android:exported"]:
				# 	if rec["android:exported"] == "true":
				# 		exported.append(rec["android:name"])
			except:
				pass

		# print(len(recvs))
		return receivers

	def Permissions(self):
		perms = self.soup.findAll("uses-permission")
		names = [p["android:name"] for p in perms]
		return names

	def MetaData(self):
		metas = self.soup.findAll("meta-data")
		name = [m["android:name"] for m in metas]
		return name


	def Actions(self):
		actions = self.soup.findAll("action")
		names = set([action["android:name"] for action in actions])
		return names


	def MakeSoup(self, f):
		f = open(f, "r")
		data = "".join(x.replace("\n", "") for x in f.readlines())
		soup = BeautifulSoup(data, "lxml")
		return soup


if __name__ == "__main__":
	if len(argv) < 2:
		Usage = ''' python activities.py <path to AndroidManifest.xml> '''
		print(usage)
		exit()
	else:
		
		manifest = androidManifest(argv[1])
		for acti in manifest.Services():
			print(acti)
		print(manifest.PackageName())

