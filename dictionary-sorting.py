import datetime
def timer(funct):
    def run_timer(*args,**kwargs):
        start = datetime.datetime.now()
        funct(*args,**kwargs)
        end = datetime.datetime.now()
        result_time = end - start
        print(result_time)
    return run_timer

def sort_keys():
    '''
    sort the given dictionary based on keys
    :return:
    '''
    input_val = {'c':23,'b':1,'a':78}
    answer = dict(sorted(input_val.items()))
    print(answer)

def sort_values():
    '''
    sort the given dictionary based on values
    :return:
    '''
    input_val = {'c':23,'b':1,'a':78}
    answer = dict(sorted(input_val.items(),key= lambda x:x[1]))
    print(answer)

@timer
def group_anagrams():
    '''
    group the anagrams & sort them
    :return:
    '''
    input_val = ["eat", "tea", "tan", "ate", "nat", "bat"]
    default_dict = dict()
    # print(default_dict.keys())
    for values in input_val:
        key = str(sorted(values))
        if key in default_dict.keys():
            default_dict[key].append(values)
            default_dict[key] = sorted(default_dict[key])
        else:
            default_dict[key] = [values]
    group = default_dict.values()
    sorted_group = sorted(group)
    print(sorted_group)



group_anagrams()