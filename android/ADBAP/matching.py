import re

def matchPackages(data):
	pattern = r"\w+\..+"
	pattern = re.compile(pattern)
	return (pattern.findall(str(data)))
	
