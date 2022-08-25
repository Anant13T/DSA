
def PrintMaxMinValue(a, b, c) :
	secondPart = c * 1.0 - (b * b / (4.0 * a))
	if a > 0 :
		print(secondPart)
	elif a < 0 :
		print(secondPart)
	else :
		print("Not a quadratic function")