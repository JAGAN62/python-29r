
def length_of_parameters(string_list): 
    '''
    this code snippet is common solution for 
    1. Given a list of words, return a dictionary where the keys are words and values are their lengths.
    2. Given a string, return a dictionary where keys are characters and values are their occurrence.

    ''' 
    answer =  {}
    for i in string_list:
        for _ in i:
            if i not in answer:
                answer[i]=0 #len(i)
                answer[i] += 1
            elif i in answer:
                 answer[i] += 1
    return answer
print('length of words : ',length_of_parameters(['apple','ball','cat','dog']))
print('Characer occurence : ',length_of_parameters('apple'))


# Given two lists of equal length, create a dictionary where one list contains keys and the other contains values.
def list_eq(list1,list2):
    if len(list1) != len(list2):
        return 'both lists are not of same length'
    else:
        answer={}
        for i in range(len(list1)):
            answer[list1[i]]=list2[i]
    return answer
print(list_eq(['a','b','c'],[1,2,3]))
