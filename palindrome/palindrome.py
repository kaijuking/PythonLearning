def palindrome_v1(s):

    # Check if input is a string
    if isinstance(s, str):
        # My approach
        return is_palidrome(s)
    else:
        return False


def palindrome_v2(s):

    # Check if input is a string and the intial checks return True
    if isinstance(s, str) and initial_check(s):
        # Compare the original string to its reversed equivalent
        reversed_string = reverse(s)
        if reversed_string == s:
            return True
        else:
             return False
    else:
        return False
   
    
def initial_check(string_to_process):
    

    # Remove any whitespaces
    s = get_rid_of_whitespaces(string_to_process.lower())

    # Check string length of 0
    if len(s) == 0:
        return False

    # Check if string contains any character that is not part of the English alphabet
    elif not contains_only_letters(s):
        return False

    else:
        return string_to_process


def is_palidrome(string_to_process):

    s = initial_check(string_to_process)

    if s:
        tmp_list = list(s)
        s_length = len(s)
        num_of_iterrations = int(s_length / 2)

        for i in range(num_of_iterrations):
            x = tmp_list[i]
            y = tmp_list[(s_length - 1) - i]

            if not x == y:
                return False
        
        return True

    else:
        return False


def reverse(s): 

    # Got this recursive function from: https://www.geeksforgeeks.org/reverse-string-python-5-different-ways/x
    if len(s) == 0: 
        return s 
    else: 
        return reverse(s[1:]) + s[0]


def get_rid_of_whitespaces(string_to_process):
    if " " in string_to_process:
        return string_to_process.replace(" ", "")
    else:
        return string_to_process


def contains_only_letters(string_to_process):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    only_letters = True

    for i in range(len(string_to_process)):
        if string_to_process[i] not in alphabet:
            only_letters = False

    return only_letters

if __name__ == "__main__":
    word_list = ["mom", "mooom", "mooooooooooooooooooooooooooooom", "moooooaoom", "", "   ", 1, -1, 0, 3.14, None]

    for i in range(len(word_list)):
        actual_result = palindrome_v1(word_list[i])
        print("palindrome_v1 - {0} - Type of {1} - Is a palindrome = {2}".format(word_list[i], type(word_list[i]), actual_result))

        actual_result = palindrome_v2(word_list[i])
        print("palindrome_v2 - {0} - Type of {1} - Is a palindrome = {2}".format(word_list[i], type(word_list[i]), actual_result))

