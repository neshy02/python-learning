# https://stepik.org/lesson/567058/step/5?unit=561332

n = list(map(int, input().split()))

def get_rec_sum(nums):
    if not nums:
        return 0
    
    return nums[0] + get_rec_sum(nums[1:])

print(get_rec_sum(n))