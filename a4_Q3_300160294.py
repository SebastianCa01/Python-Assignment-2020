#Family name: Sebastian Doka
#Student number: 300160294
#Course : ITI 1120
#Assignment Number 4 Question 3
#date: 2020 11 02

def longest_run(t):
    '''(list of numbers)->int
    Takes in a list of numbers and reurns the length of the longest sequence of consecutive
    repeated numbers.
    '''
    result=0
    max_result=0
    

    if len(t)==0:
        return 0
    
    
    last_seen=t[0]

    for v in t[0:]:
        if v==last_seen:
            result += 1
        else:
            if result > max_result:
                max_result = result
            last_seen = v
            result=1
        


    if result > max_result:
        max_result = result

    return max_result

input_list = input("Please input a list of numbers separated by space: ").strip().split()
new_list=[] 
for element in input_list:
    new_list.append(float(element))


print(longest_run(new_list))


