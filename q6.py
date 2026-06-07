"""
    Task 1
    - Create a function that finds the first negative number in a list (lst).
    - Return the first negative number if found, otherwise return "No negatives".
    - Use a while loop to implement this
"""
def find_first_negative(lst):
  # Use index to loop through the list
  i = 0
  while i < len(lst):
    # Return number if negative 
    if lst[i] < 0:
      return lst[i]
    # Increment of index by 1
    i += 1
    
  # Return message if no negative number can be found
  return "No negatives"

# Task 2
# Invoke the function "find_first_negative" using the following scenario:
# - [3, 5, -1, 7, -2, 8]
# - [2, 10, 7, 0]
print(find_first_negative([3, 5, -1, 7, -2, 8]))
print(find_first_negative([2, 10, 7, 0]))
