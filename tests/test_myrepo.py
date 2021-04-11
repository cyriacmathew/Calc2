from comprepo import paycode

def test_add():
	result = paycode.add(1, 2)
	assert result == 3

def test_subtract():
	result = paycode.subtract(2, 1)
	assert result == 1