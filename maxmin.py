def find_max_min(n):
  min_num = min
  max_num = max
  num = int(raw_input("The max and min numbers are:"))

  if min_num == max_num:
  	return [len(n)]
  else:
  	return (min_num, max_num)