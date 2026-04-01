

def freq_sort():
    '''
    Sort the given list on the basis of frequency and if it ties then sort it in value in ascending order
    :return:
    '''
    from collections import Counter
    input_val = [7,7,8,8,3,5,5,7,2,2,1]
    freq = Counter(input_val)
    # print(freq)
    final = sorted(input_val, key= lambda x:(freq[x],-x), reverse=True)
    print(final)

freq_sort()