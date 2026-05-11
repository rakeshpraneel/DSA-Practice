
def zip_values(a: list, b: list):
    return list(map(lambda x:sum(x), list(zip(a,b))))

def find_multiples(a: list, b: list):

    return list(map(lambda x,y:x*y, a,b))

def find_square(input_val: list):
    '''
    map usage
    :param input_val: list of integers
    :return: list of squared integers
    '''
    return list(map(lambda i: i*i, input_val))


def freq_sort(string):
    from collections import Counter

    dictionary = Counter(string)
    print(dictionary)
    # dictionary = {}
    # for i in string:
    #     if i not in dictionary:
    #         dictionary[i] = string.count(i)
    dictionary = dict(sorted(dictionary.items(), key= lambda x:x[1], reverse=True))
    answer = ""
    for x in dictionary.keys():
        answer += x
    # print(dictionary)
    return answer

    # sorted()


print(find_square([1,2,3,4]))

print(find_multiples([1,2,3,4],[5,6,7,8]))

print(zip_values([1,2,3,4],[5,6,7,8]))

s = "moscowincavery"
print(freq_sort(s))