'''
LRU Cache

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
'''


class LRUCache:
    '''
    Memory 77.65MB Beats 91.88%
    Runtime 2501ms Beats 5.02%
    '''
    def __init__(self, capacity: int):
        self.capa = capacity
        self.memory = {}
        self.least_mem = []

    def get(self, key: int) -> int:
        # print("get function called...")
        if key in self.memory.keys():
            # print(f"key {key} found and value is {self.memory[key]}")
            # removing and adding the recently used value at the end
            self.least_mem.remove(key)
            self.least_mem.append(key)
            return self.memory[key]
        else:
            # print(f"key not found {key}")
            return -1

    def put(self, key: int, value: int) -> None:
        # print("put function called....")
        if len(self.memory) == self.capa and key not in self.memory.keys():
            # print("memory limit reached so deleting least used key")
            del self.memory[self.least_mem[0]]
            del self.least_mem[0]
            # print(f"after deleting.... {self.memory}")
        self.memory[key] = value
        if key in self.least_mem:
            self.least_mem.remove(key)
        self.least_mem.append(key)
        # print(f"memory and last_mem updated {self.memory} {self.least_mem}")


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)