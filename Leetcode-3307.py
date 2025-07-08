
class Solution:

    def kthCharacter(self, k: int, operations: list[int]) -> str:
        print(operations)
        length = [1]
        for operation in operations:
            length.append(length[-1] * 2)

        print("length calculated:::",length)
        def backtrack(k, list_position, word):
            print(f"Back tracking started::: required position:{k}, current operation position:{list_position}, initial word:{word}")
            print("length list:::", length[:list_position])
            prev_len = length[list_position-1]
            print(f"previous length::: {prev_len}")
            if list_position == 0:
                return word
            if length[list_position-1] >= k:
                print(f"length is greater {length[list_position-1]} >= {k}")
                print("recursively calling back track function..")
                return backtrack(k, list_position-1, word)
            else:
                print(f"length is lesser {length[list_position-1]} < {k}")
                char = backtrack(k-prev_len,list_position-1, word)
                print(f"char obtained from backtrack function::: {char}")
                if operations[list_position-1] == 1:
                    return chr(97) if ord(char) == 122 else chr(ord(char)+1)
                return char

        return backtrack(k, len(operations)+1, 'a')

object_ = Solution()
print(object_.kthCharacter(100000000000000,[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))