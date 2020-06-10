def palindrome(string_to_process):

    # check if input is a string
    if not isinstance(string_to_process, str):
        return {"valid": False, "message": "Input is not a valid string"}

    # remove any whitespaces
    s = get_rid_of_whitespaces(string_to_process.lower())

    # check string length
    if len(s) == 0:
        return {"valid": False, "message": "Input must contain at least one letter"} 

    # check if string contains any character that is not part of the English alphabet
    if not contains_only_letters(s):
        return {"valid": False, "message": "Input must only contain letters"}
    
    return is_palidrome(string_to_process)


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


def is_palidrome(string_to_process):
    return {"valid": True, "message": "Input is a valid palidrome"}


if __name__ == "__main__":
    word_list = [1, "", "   ", "mom111", "mom"]

    for i in range(len(word_list)):
        actual_result = palindrome(word_list[i])
        print(str(actual_result))
        assert actual_result["valid"] is True, "{0} - {1}".format(word_list[i], actual_result["message"])
