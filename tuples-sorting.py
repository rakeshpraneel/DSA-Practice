'''
sort the given list of tuples in increasing order
[(1,7),(1,3),(3,4,5),(2,2)]
'''

def main_funct():
    # input_val = input("provide the list:")
    input_val = [(1,7),(1,3),(3,4,5),(2,2)]
    answer = sorted(input_val, key= lambda x: x[0])
    print(answer)

def multi_sort():
    '''
    sort in ascending using first element and descending using second element.
    '''
    input_val = [(1, 7), (3, 4, 5),(1, 3), (2, 2), (2,3)]
    answer = sorted(input_val, key=lambda x: (x[0],-x[1]))
    print(answer)

def mixed_length_sort():
    '''
    sort in ascending using first element if ties sort based on length.
    '''
    input_val = [(1, 7), (3, 4, 5), (1, 3), (2, 2), (2, 3), (3,1)]
    answer = sorted(input_val, key=lambda x: (x[0], len(x)))
    print(answer)

def sum_sort():
    '''
    sort based on sum of elements and if ties sort based on first element
    '''
    input_val = [(1, 7), (3, 4, 5), (2, 2), (1, 3), (2, 3), (3,1)]
    answer = sorted(input_val, key=lambda x: (sum(x),x[0]))
    print(answer)

def distance_from_origin():
    '''
    sort based on distance from origin
    '''
    input_val = [(1, 7), (-1,-1), (2, 2), (1, 3), (2, 3), (3,1)]
    answer = sorted(input_val, key=lambda x: (x[0]**2+x[1]**2))
    print(answer)

def k_no_of_pts():
    '''
    return k number of points that is closest to origin
    '''
    k = 3
    input_val = [(1, 7), (-1,-1), (2, 2), (1, 3), (2, 3), (3,1)]
    answer = sorted(input_val, key=lambda x: (x[0]**2+x[1]**2))
    print(answer[:k])

k_no_of_pts()