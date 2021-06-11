random_list=[9,5,4,3,2,7,6,8,1]
sorted_list=[9,5,4,3,2,7,6,8,1]


def sorted(number):
	
	for i in sorted_list:
		index = sorted_list.index(i)
		second_index = index + 1

		if sorted_list.index(i) == len(sorted_list)-1:
			break

		if sorted_list[index] > sorted_list[second_index]:
			sorted_list[index], sorted_list[second_index] = sorted_list[second_index], sorted_list[index]
			print(sorted_list)

for i in sorted_list:
	sorted(i)


print('random list',random_list)
print('sorted list',sorted_list)
