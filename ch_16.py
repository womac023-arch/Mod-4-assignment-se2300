# Remove abbreviations
def first_Negative(numbers_List):
    # check each number
    for n in numbers_List:
        # Check if number is negative
        if n < 0:
            # Return first negative number
            return n
    return None
