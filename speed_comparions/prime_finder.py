import time

def find_primes(start, end):
  """
  Counts the number of prime numbers between a start and end integer (inclusive).

  Args:
      start: The starting integer.
      end: The ending integer.

  Returns:
      The number of prime numbers between start and end.
  """
  # Handle edge cases where start or end is less than 2
  if start < 2:
    start = 2
  if end < 2:
    return 0
  
  # Initialize count to 0
  count = 0
  
  # Loop through each number from start to end
  for num in range(start, end + 1):
    # If the number is prime, increment the count
    if is_prime(num):
      count += 1
  
  # Return the count of prime numbers
  return count

def is_prime(num: float):
  """
  Checks if a number is prime.

  Args:
      num: The number to check.

  Returns:
      True if the number is prime, False otherwise.
  """
  # Handle cases 0, 1, and negative numbers
  if num <= 1:
    return False
  
  # Loop through potential factors from 2 to the square root of num
  for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
      return False
  
  # If no factors found, the number is prime
  return True

if __name__ == '__main__':
    start = time.time()
    nr_primes = find_primes(7890, 567890)
    print(nr_primes)
    end = time.time()
    print(end - start)
