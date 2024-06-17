# Write a program to find the number of times a number exists in a list. return in descending order of number 
of occurrences a number exists


def count_of_numbers(L):
    d = {}
    for i in L:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d

list = [ 8,45,25,6, 11, 29, 42, 25, 14,42,25]
#original sequance of no.of times a number exists 
count_of_numbers = count_of_numbers(list)
print(f'general no.of occurences of a number sequence{count_of_numbers}')
#return the sequence in descending order of its occurrences
count_of_numbers_result = dict(sorted(count_of_numbers.items(), key=lambda i:i[1], 
                                      reverse=True))
# ''' here i[1] represents the values in a dictionary if we replace 0 
# then it will return with the values rather than their occurrences''
# print(descending order of no.of occurrences sequence{count_of_numbers_result}')





# write a program to find a number that is prime or not prime.



def is_prime(n):
    if n<2:
        return False 
    for i in range(2,n):  #time complexity is O(n)
        if n%i==0:
            return False
    return True   #if one is True then no need to check for the other so terminates the loop
n=int(input('enter a number:'))
if is_prime(n):
    print(f'given number {n} is prime')
else:
    print(f'given number {n} is not prime')


#### Optimize the code by reducing time complexity
def is_prime_Opti(x):
    if x<2:
        return False
    for i in range(2,int(x**.5+1)): #time complexity is O(sqrt(n))
        if x%i==0:
            return False
    return True
x=int(input('enter a number:'))
if is_prime_Opti(x):
    print(f'given number {x} is prime')
else:
    print(f'given number {x} is not prime')








#  write a program to delete duplicates and return the list without duplicates.


def delete_duplicates(arr):
    res = []
    for i in arr:
        if I am not in res:
            res.append(i)
    return res

array = [1, 2, 3, 2, 1, 3, 2, 4, 5, 4]
res = delete_duplicates(array)
reverse_res=sorted(delete_duplicates(array), reverse=True)
print(f'given array is: {array}')
print(f'array without duplicates is: {res}')
print(f'array without duplicates in reverse order is:{reverse_res}')




#  Write a program to find the second large number in a list.


def find_second_largest_num(arr):
    if len(arr) < 2:
        return "List should have at least two elements"

    unique_arr = list(set(arr))  # Remove duplicates
    unique_arr.sort(reverse=True)   # time complexity is O(nlogn)

    if len(unique_arr)>= 2:
        return unique_arr[1] 
    else:
        "No second-largest number"

array = [2,5,9,3,8,96,25,36,45]
res = find_second_largest_num(array)
print(f"The second-largest number is: {res}")




# Write a program to find the second-largest negative number in a list.


def second_largest_negative(arr):
    largest_neg = float('-inf')
    second_largest_neg = float('-inf')

    for i in arr:
        if i < 0:
            if i > largest_neg:
                second_largest_neg = largest_neg
                largest_neg = i
            elif i > second_largest_neg and i != largest_neg:
                second_largest_neg = i

    if second_largest_neg != float('-inf'):
        return second_largest_neg 
    else:
        "No second-largest negative number"


numbers = [3, -5, -28, 7, -81, 4, -16]
result = second_largest_negative(numbers)
print(f"The second-largest negative number is: {result}")