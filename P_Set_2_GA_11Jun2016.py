

## (1) Given a list of strings, identify all strings containing the letter 'o'.
##Then make a new list with these words, and
##print them out.

my_list = ['General Assembly','Python','Object','For loop','lists','Tuples','seattle']
new_list = list()
for word in my_list:
    if 'o' in word or 'O' in word:
        new_list.append(word)
print(new_list)

## (2) Given a list of integers, square them, make a new list, print it out

my_list = [1,2,3,4,5,6,7]
new_list = list()

for num in my_list:
    num = num**2
    new_list.append(num)

print(new_list)

## (3) Remove redundancy in list . e.g. input list is [20,14,14,14,10,10] output list is [20,14,10]

my_list = [20,14,14,14,10,10,20]
new_list = list()
for item in my_list:
    if item not in new_list:
        new_list.append(item)
print(new_list)
    

        

