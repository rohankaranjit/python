# WAP to check if a list contains a palindrome of elements
def is_palindrome(lst):
    # Create a copy of the list to check against the reversed list
    lst_copy = lst.copy()
    lst_copy.reverse()  # Reverse the copy of the list
    
    return lst == lst_copy  # Check if the original and reversed list are the same

# Test the function
sample_list = [1, 2, 3, 2, 1]
if is_palindrome(sample_list):
    print(f"{sample_list} is a palindrome!")
else:
    print(f"{sample_list} is not a palindrome.")

# You can test it with other lists like:
test_list = ["abc", "abc", 1]
if is_palindrome(test_list):
    print(f"{test_list} is a palindrome!")
else:
    print(f"{test_list} is not a palindrome.")
