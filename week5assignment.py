# Program to find most frequent
# element in a list
 

from collections import Counter
list_of_max = []
 
def most_frequent(list_of_num:list, k:int):
    """ This is a function that prints the k most frequent element(s)
    it takes in a list and an integer k as arguments and prints the 
    k most frequent elements.

    Args:
    list : the list to be counted
    k : the number of frequent elements you need
    """

    count = Counter(list_of_num)
    ans = count.most_common()
    print(ans)
    for i in range(0, k):
        list_of_max.append(ans[i][0])
        print(f"top {i+1} most frequent element is {list_of_max}")
    print(f"top {i+1} most frequent element is {list_of_max}")
  
   
k = 3
# list_of_num = [7,5,4,7,7,8,5,4,7,7,7,7,7,7,7,0, 3,78,87,34,78,78]
list_of_num = [10, 11, 11, 13, 12, 140, 15, 12, 13, 13, 15, 15, 15, 15, 15, 140, 140, 140, 140]
(most_frequent(list_of_num, k))


empty_list = []
k=4
####SECOND METHOD
import numpy as np
result = list(zip(*np.unique(list_of_num, return_counts=True)))
ress = dict(result)
sorted_list = sorted(ress.items(), key = lambda x:x[1], reverse = True)
print(sorted_list)
for i in range(0, k):
    empty_list.append(sorted_list[i][0])
    print(f"top {i+1} most frequent element is {empty_list}")
    # print(empty_list)
   
print(f"top {i+1} most frequent element is {empty_list}")
