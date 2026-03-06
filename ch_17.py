def factorial(n):
    # Set result to 1
    result = 1
  
    # Generate numbers from 1 to n
    # The loop multiplies result by each number
    for i in range(1, n + 1):
        result *= i
    # Return the final calculated value
    return result
