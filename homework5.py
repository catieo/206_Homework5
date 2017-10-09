import re 

filevar = open("regex_sum_39677.txt")

list_of_nums = [] 
for line in filevar.readlines():
	line = line.rstrip()
	num = re.findall('[0-9]+', line)
	if num != []:
		list_of_nums.extend(num)

result = 0
for x in list_of_nums:
	result = result + int(x)

print(result)