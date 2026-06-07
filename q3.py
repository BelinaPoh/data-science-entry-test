"""
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
"""
def update_dictionary(dct, key, value):
    # If the key already exists in dct
    if key in dct:
    	# Print the original value
        print(dct[key])
        
    # Add new key-value pair or update value if key exist
    dct[key] = value
    	
    # Return updated dictionary
    return dct

# Task 2
# Invoke the function "update_dictionary" using the following scenarios:
# - {}, "name", "Alice"
# - {"age": 25}, "age", 26
print(update_dictionary({}, "name", "Alice"))
print(update_dictionary({"age": 25}, "age", 26))
