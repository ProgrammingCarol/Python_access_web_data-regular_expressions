import re
myfile = open('regex_sum_113279.txt','r')

nums_list = [0]
for line in myfile:
    nums = re.findall('[0-9]+',line)
    if not nums:
        continue
    else:
        nums_list.extend(nums)
        nums_list = list(filter(None,nums_list))

nums = list(map(int,nums_list))
print(sum(nums))
