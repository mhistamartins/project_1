# to define a variable, you are using the syntax:
#bvariable_name = <value>

int_number = 10 #snake case
int_number_2 = int_number + 100
string_variable = "it is my string variable" #single quotqtion * works as well
my_long_variable = """ghdhhdjdjjjdjjsjjs kkskks
hshjsjjs
jsjjss"""


print(int_number_2)

#if and else condition

if int_number < int_number_2:
    print("statement is true")
else:
    print("statement is fale")


# loop: for loop and do while loop

for iterate_value in range(1, 5):
    print(iterate_value)

print(int_number)
while int_number > 0:
    print(int_number)
    int_number -= 1

#working with functions
def calculate_two_numbers(value_1, vaulue_2):
    result = value_1 + vaulue_2
    return result
print("..........................")
print(calculate_two_numbers(28,10))


#to get input from user use the function input

input_from_user = input("enter message here:")
print(input_from_user)

#to print out numbers on the terminal:
print( "some text with {} and {} ".format(int_number, int_number_2))

#or

print( f'other string with {int_number} and {int_number_2}')

