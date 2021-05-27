numbers=[1,0,1,0,0,0,1,1,1,1,1,0,0,1,1,0,1,1,1]

def check_one(nums):
    counter=0
    max=0
    for num in nums:
        if num==1:
            counter+=1
        if counter>max:
            max=counter
        elif num==0:
            counter=0
    return max
print(check_one(numbers))