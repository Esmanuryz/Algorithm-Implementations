# Question 4: Fibonacci

def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_memoized(n, memo={}):
    if n in memo:  # memoization a method is what keeps the value that used before (usefull for recursive functions) .
    # If a number has been calculated before, the stored value is used instead of recalculating.
        return memo[n]
    if n <= 1:
        memo[n] = n
    else:
        memo[n] = fibonacci_memoized(n - 1, memo) + fibonacci_memoized(n - 2, memo)
    return memo[n]

# Example Usage
if __name__ == "__main__":

    print("Fibonacci (Recursive):", fibonacci_recursive(10))
    print("Fibonacci (Memoized):", fibonacci_memoized(10))