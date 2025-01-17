# Question 1.a: Second Largest Element

def second_largest(nums):
    if len(nums) < 2:
        return None  # Not enough elements

    first, second = float('-inf'), float('-inf')
    for num in nums:
        if num > first:
            first, second = num, first
        elif num > second and num != first:
            second = num

    return second



# Question 1.b: Reverse String Using Stack

def reverse_string(s):
    stack = []
    for char in s:
        stack.append(char)

    reversed_s = ''
    while stack:
        reversed_s += stack.pop()

    return reversed_s

# Example Usage
if __name__ == "__main__":
    # Example for Question 1.a
    print("Second Largest:", second_largest([10, 20, 4, 45, 99, 87, 90]))

    # Example for Question 1.b
    print("Reversed String:", reverse_string("hello"))

