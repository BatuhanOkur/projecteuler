#https://projecteuler.net/problem=19
import datetime

def howManySundays(y1,y2):
	count = sum(1
		for y in range(y1, y2+1)
		for m in range(1, 13)
		if datetime.date(y, m, 1).weekday() == 6)
	return str(count)

print(howManySundays(1901,2000))