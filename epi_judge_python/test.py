# The grades may not always be A, B, C, D, E, and I. 
# For example, A- is a valid grade in some places as is 3.7. 
# You should treat whatever is in the passed-in list as a valid grade.

def grade_stats(lis):
    # If the passed-in list is empty, your function should return an empty dictionary.

    # Insert your code here
    my_dict={}

    for grade in lis:
        if grade in my_dict:
            my_dict[grade]+=1
        else:
            my_dict[grade]=1

    return my_dict