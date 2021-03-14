import sys

x = int(input("X :"))
y = int(input("Y :"))

try :
	a = x/y

except ZeroDivisionError:
	print("Error : Can't Divide By Zero.")
	sys.exit(1)

print(a)