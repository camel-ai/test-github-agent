def product_except_self(nums):
    n = len(nums)
    result = [1] * n
    
    for i in range(n):
        for j in range(n):
            if i != j:
                result[i] *= nums[j]
                
    return result

# Test the function with the example input
print(product_except_self([1, 2, 3, 4]))  # Output: [24, 12, 8, 6]
