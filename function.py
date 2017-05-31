def my_abs(x):
	if not isinstance(x, (int, float)):
		raise TypeError('bad operand type')
	if x>0:
		return x
	else:
		return -x

def mulReturn():
	return [10,20,30]