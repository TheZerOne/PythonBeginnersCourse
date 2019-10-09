def func():
	 print("func() in one")

print("top level in one.py")

if __name__ == '__main__':
	print('One.py is being run directly')
else:
	print('one.py has been imported')