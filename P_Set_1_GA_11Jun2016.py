

## (1)Write a script to request the user to enter his/her age. If age is below thirty print out "So you think you can
##change the world, wait till you turn thirty", if age
##is thirty or above print "Life not only begins at 30, it begins to show"


my_age = int(input("Please enter your age as completed years: "))

if my_age < 30:
    print("So you think you can change the world ? Wait till you turn thirty")
else:
    print("Life not only begins at 30, it begins to show")

##(2) Write a script that takes as input two string, and outputs a new string made of the first and last characters
## of the two string. E.g. input string "good boy" and "bad show" outputs "gybw"

string_1 = input("Enter first string: ")
string_2 = input("Enter second string: ")

new_string = string_1[0]+string_1[-1] + string_2[0] + string_2[-1]

print(new_string)

##(3) Write a script to which will convert an all uppercase word into a all lowercase word except the first character
## without using a for loop !

upper_string = input("Enter your upper case string: ")
print(upper_string[0]+ upper_string[1:].lower())

##(4) Find the first occurences of the words 'not' and 'good'. If not preceeds good, change the whole substring to 'bad'
## "This music is not very good" changes to "This music is bad"

myword = input("Enter your string: ")

if myword.find("not") < myword.find("good"):
    not_index = myword.find("not")
    good_index = myword.find("good")
    my_substring = myword[not_index:(good_index+4)]
    print(myword.replace(my_substring,"bad"))
else:
    print(myword)










