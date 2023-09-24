#Family name: Sebastian Doka
#Student number: 300160294
#Course : ITI 1120
#Assignment Number 4 Question 2
#date: 2020 11 02

def two_length_run(t):
    '''(list of numbers)->bool
    Takes in a list of numbers and returns true if there is a sequence of length
    at least two of consecutive repeated values and false otherwise
    '''
    result=0
    max_result=0
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

    if max_result >= 2:
        return True
    else:
        return False


input_list = input("Please input a list of numbers separated by space: ").strip().split()
print(two_length_run(input_list))
    
