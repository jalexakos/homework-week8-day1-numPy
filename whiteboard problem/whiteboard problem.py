# Given two arrays, write a function to compute their intersection.
# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Note:
# Each element in the result must be unique.

def find_intersect(arr1,arr2):
    answer = []
    for num in arr1:
        if num in arr2 and num not in answer:
            answer.append(num)

    return answer

print(find_intersect([2,2],[1,2,2,1]))
print(find_intersect([4,9,5],[9,4,9,8,4]))

def fI(arr1,arr2):
    set1 = set(arr1)
    set2 = set(arr2)
    answer = set1.intersection(set2)
    return list(answer)

print(fI([2,2],[1,2,2,1]))
print(fI([4,9,5],[9,4,9,8,4]))

# Joel solution:

def intersection(nums1,nums2):
    temp = set(nums1)
    if len(nums2) > len(nums1):
        temp = set(nums2)
        newList = [value for value in nums1 if value in temp]
    else:
        newList = [value for value in nums2 if value in temp]
    return list(set(newList))

print(intersection([2,2],[1,2,2,1]))
print(intersection([4,9,5],[9,4,9,8,4]))