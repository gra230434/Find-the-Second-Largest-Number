howmany_number = int(input())
number_lists = [int(i) for i in input().split()]

print (number_lists)
number_lists.sort()

the_big_one = number_lists.pop()
the_second_one = number_lists.pop()
while the_second_one == the_big_one:
	the_big_one = the_second_one
	the_second_one = number_lists.pop()
	if not number_lists :
		break

print (the_second_one)
