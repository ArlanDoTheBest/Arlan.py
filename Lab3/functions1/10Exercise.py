list = input().split()
list = [int(nums) for nums in list]
def unique(list):
    unique_list = []
    for nums in list:
        if nums not in unique_list:
            unique_list.append(nums)
            
    print(unique_list)

unique(list)