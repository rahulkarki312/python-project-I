import random
import time

# naive search: scan the entire list and ask if its equal to the target
# if yes, then return the index
# if no, then return -1


def naive_search(l, target):
    # example l = {1, 3, 10, 12}
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1

# binary search uses divide and conquer:
# we will leverage the fact that our list is sorted


def binary_search(l, target, low=None, high=None):  # low and high as indices
    if low is None:
        low = 0
    if high is None:
        high = len(l)-1
    if high < low:  # if can't find the target (i.e if iterated correctly, this would be false)
        return -1
#     example l = {1, 3, 5, 10, 12} #should return 3
    midpoint = (high+low) // 2  # 2

    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint - 1)
    else:
        # target > l[midpoint]
        return binary_search(l, target, midpoint + 1, high)


if __name__ == '__main__':
    l = [1, 3, 5, 10, 12]
    target= 10
    print(naive_search(l, target))
    print(binary_search(l, target))


length = 10000
# build a sorted list of 10000
sorted_list = set()
while len(sorted_list) < length:
    sorted_list.add(random.randint(-3*length, 3*length))
sorted_list = sorted(list(sorted_list))

start = time.time()
for target in sorted_list:  # its going to make each element a target element
    naive_search(sorted_list, target)
end = time.time()
print("Naive search time: ", (end-start)/length, "seconds")     # calculates the time to iterate over the list per one target!

start = time.time()
for target in sorted_list:  # its going to make each element a target element
    binary_search(sorted_list, target)
end = time.time()
print("Binary search time: ", (end-start)/length, "seconds")










