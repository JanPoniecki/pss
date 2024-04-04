def srt(array):
	if len(array) <= 1:
		return array
	else:
		pivot = array.pop(0)
		lower = []
		greater = []
		for a in array:
			if a < pivot:
				lower.append(a)
			else:
				greater.append(a)
		return srt(lower) + [pivot] + srt(greater)

array = [39, 40, 52, 38, 19, 67, 12, 34, 3, 79]
print(srt(array))