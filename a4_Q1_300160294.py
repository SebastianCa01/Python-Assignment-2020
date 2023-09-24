#Family name: Sebastian Doka
#Student number: 300160294
#Course : ITI 1120
#Assignment Number 4 Question 1
#date: 2020 11 02

def number_divisible(l,n):
    '''(int,list of int)-> int
    Takes in a list of integers and a non-zero integer,n and outputs how many of the
    integers in the list can be divided by n
    Preconditions: l must be a list of integers no floats allowed, n must be a non-zero integer
    '''
    
    length=len(l)
    for i in range(0,len(l)):
        if l[i]% n !=0:
            length=length-1

    return length

input_list = input("Please input a list of numbers separated by space: ").strip().split()
integer=input("Please input an integer: ")
new_list= []
for i in input_list:
    new_list.append(int(i))
    
print("The number of elements divisible by " + integer + " is " + str(number_divisible(new_list,int(integer))))

