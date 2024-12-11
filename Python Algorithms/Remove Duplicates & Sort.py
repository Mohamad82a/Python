

def remove_duplicates_1(nums):
    result = []
    [result.append(x) for x in nums if x not in result]
    n = len(result)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if result[j] < result[min_index]:
                min_index = j
        result[i], result[min_index] = result[min_index], result[i]
    return f'Sorted list 1: {result}'
    

# def remove_duplicates_2(nums):
#     nums[:] = sorted(set(nums))
#     return f'Sorted list 2: {list(nums)}'
    
    

if __name__ == '__main__':

    nums1 = [1,1,1,2,3,4,8,8,5,5,6,7,7,10,9,4,5,6,2,3,5,1,8]
    sorted_list1 = remove_duplicates_1(nums1)
    # sorted_list2 = remove_duplicates_2(nums1)
    
    print(sorted_list1)
    # print(sorted_list2)

