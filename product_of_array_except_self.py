def product_except_self(nums):
    n = len(nums)
    result = [1] * n
    left_product = [1] * n
    right_product = [1] * n
    
    for i in range(1, n):
        left_product[i] = left_product[i - 1] * nums[i - 1]
    
    for i in range(n - 2, -1, -1):
        right_product[i] = right_product[i + 1] * nums[i + 1]
    
    for i in range(n):
        result[i] = left_product[i] * right_product[i]
    
    return result

# Test the function with the example input
print(product_except_self([1, 2, 3, 4]))  # Output: [24, 12, 8, 6]
