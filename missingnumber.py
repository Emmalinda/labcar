def find_missing(list1,list2):
	list1 = []
	list2 =	[]
	n = ''
	
	if list1 == list2:
		return 0

	elif list1<list2:
		n = 'i for i in list2 if i is not in list1'
		return n

	elif list1>list2:
		n = 'i for i in list 1 if i is not in list2'
		return n



