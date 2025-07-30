'''

'''
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)
        print(hash_map)
        for val in strs:
            # print("".join(sorted(val)))
            hash_map["".join(sorted(val))].append(val)
        return [hash_map[key] for key in hash_map.keys()]

################################
from collections import defaultdict
class Solution:
    def createNewKey(self,hash_map,val):
        hash_map[val] = defaultdict(int)
        for chrs in val:
            hash_map[val][chrs]+=1
        return hash_map

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = dict()
        output = list()
        list_position = dict()
        new_value_counter = 0
        for val in strs:
            # print("---"*10)
            # print(f"value for current iteration::: {val}")
            if not hash_map:
                hash_map = self.createNewKey(hash_map,val)
                output.append([val])
                list_position[val] = new_value_counter
                new_value_counter+=1
            else:
                value_found_flag = False
                val_length = len(val)
                for key in hash_map.keys():
                    counter = 0
                    for chrs in hash_map[key]:
                        if val.count(chrs) == hash_map[key][chrs]:
                            # print(f"value count matched::: {chrs}")
                            counter += 1
                    if counter == len(hash_map[key]) and counter == len(set(val)):
                        value_found_flag = True
                        output[list_position.get(key)].append(val)
                        break
                if not value_found_flag:
                    hash_map = self.createNewKey(hash_map,val)
                    output.append([val])
                    list_position[val] = new_value_counter
                    new_value_counter+=1
        # print(hash_map.items())
        # print(list_position)
        # print(sorted(output))
        return output