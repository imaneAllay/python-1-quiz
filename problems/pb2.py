def max_values(nums):
  max=nums[0]
  max2=nums[0]
  for i in range(0,len(nums)):
    if nums[i]>max :
      max=nums[i]
    elif max > nums[i] > max2:
      max2 = nums[i]
  return max,max2






