import contextlib

@contextlib.contextmanager
def eat():
	print(1)
	yield
	print(2)
def sleep():
	print(2)
# sleep()
with eat() :
	sleep()