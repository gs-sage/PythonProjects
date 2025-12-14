# function to print the length of a list
def len_list(list):
    return len(list)

# function to print the elements of a list in a single line
def el_list(list):
    for el in list:
        print(el, end=" ")


# function to find the factorial of n
def factorial(num):
    factorial = 1
    for i in range(1, num+1):
        factorial = factorial * i
    return factorial

# function to convert USD to INR
def currency_conversion(currency):
    conversion_rate = 90.60
    converted_currency = currency * conversion_rate
    return converted_currency

# function that prints out if the number is odd or even
def odd_even(number):
    if(number%2==0):
        return "EVEN"
    else:
        return "ODD"

new_list = [1,2,3,4,5,6,7,8,9]

print(len_list(new_list)) # prints the length of the list
el_list(new_list) # prints the element in a list
print()
print(factorial(5)) # gets the factorial of a number
print(currency_conversion(1000)) # converts currency
print(odd_even(10)) # will print even
print(odd_even(5)) # will print odd



    