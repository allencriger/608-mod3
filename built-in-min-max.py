def maximum(value1, value2, value3):
	"""Return the maximum of three values."""
	max_value = value1
	if value2 > max_value:
		max_value = value2
	if value3 > max_value:
		max_value = value3
	return print('Maximum value is:',max_value)
    
def minimum(value4, value5, value6):
    """Return the minimum of three values."""
    min_value = value4
    if value5 < min_value:
        min_value = value5
    if value6 < min_value:
        min_value = value6
    return print('Minimum value is:',min_value)
    
maximum(12, 27, 36)

maximum(12.3, 45.6, 9.7)

minimum(12, 27, 36)

minimum(12.3, 45.6, 9.7)

