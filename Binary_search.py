import random
import time
#brute force method
def brute_force(list,target):
    for i in range(len(list)):
        if list[i] == target:
            return i
    return -1
    
#recussion method
def binary_search(list,target,left = None,right = None):
    if left is None:
        left = 0
    if right is None:
        right = len(list) - 1
    mid = (left+right) // 2
    
    if right < left:
        return -1
    if list[mid] == target:
        return mid
    elif list[mid] > target:
        return binary_search(list,target,left, mid - 1)
    else:
        return binary_search(list,target,mid + 1, right)

#iterative method
def binary_search2(list,target):
    high = len(list) - 1
    low = 0 
    while high >= low:
        mid = (low + high) //2
        if list[mid] == target:
            return mid
        elif list[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

if __name__ == '__main__':
    length = 10000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length,3*length))
    sorted_list = sorted(list(sorted_list))
    T = random.randint(-3*length,3*length)
    start = time.time()
    for target in sorted_list:
        brute_force(sorted_list,T)
    end = time.time()
    print(f"time used : {(end-start)} seconds.")
    
    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list,T)
    end = time.time()
    print(f"time used : {(end-start)} seconds.")