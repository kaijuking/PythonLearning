def roman_numerals_v1(x):
    
    # get rid of whitespaces
    x = get_rid_of_whitespaces(x)

    # return 0 if empty string
    if len(x) == 0:
        return 0

    # setup variables
    total = 0
    tmp_list = []
    roman_val = get_roman_values()
    input_length = len(x)
    input_str = x.lower()

    # covers the case where the inputted value is only one character
    if input_length > 0 and input_length < 2:
        for i in range(len(input_str)):
            total += roman_val[input_str[i]]

    # covers the case where the inputted value is two or more characters
    if input_length > 1:
        for i in range(len(input_str)):
            tmp_list.append(roman_val[input_str[i]])

    # compare two indexes to see if 'i + 1' is greater than 'i'
    for i in range(len(tmp_list) - 1):
        if tmp_list[i + 1] > tmp_list[i]:
            tmp_list[i + 1] = tmp_list[i + 1] - tmp_list[i]
            tmp_list[i] = 0

    # total up all the values in the list
    for i in tmp_list:
        total += i

    return total


# v2 function - (romans_str: str) -> int > this tells the user the function take a string and returns an integer
# Many thanks to Karina for her help and input
def roman_numerals_v2(romans_str: str) -> int:
 
    # get rid of whitespaces
    input_string = get_rid_of_whitespaces(romans_str)

    # return 0 if empty string
    if len(input_string) == 0:
        return 0

    # setup variables
    total = 0
    roman_val = get_roman_values()

    # create a list of numeric values based on the input string
    tmp_list = [roman_val[item.lower()] for item in input_string]
    string_length = len(tmp_list)

    # covers the case where the inputted value is only one character
    if string_length == 1:
        return roman_val[input_string.lower()]

    # compare two indexes to see if 'i + 1' is greater than 'i'
    for i in range(string_length - 1):
        if tmp_list[i + 1] > tmp_list[i]:
            tmp_list[i], tmp_list[i + 1] = 0, (tmp_list[i + 1] - tmp_list[i])
        # to save time, instead of replacing the element in a temp_list, add converted values to "total"
        total += tmp_list[i]
        
    return total + tmp_list[-1]  # the last el should be added as for loop range was (input_length - 1)  



def get_rid_of_whitespaces(string_to_process):
    if " " in string_to_process:
        return string_to_process.replace(" ", "")
    else:
        return string_to_process


def get_roman_values():
    return {"i": 1, "v": 5, "x": 10, "l": 50, "c": 100, "d": 500, "m": 1000}


if __name__ == "__main__":
    test_values = {"i": 1, "iv": 4, "lxx": 70, "MMXX": 2020, "xiv": 14, "mmxlix": 2049, "m": 1000, "MCMLIV": 1954,
                   "MCCXXXIV": 1234, "": 0, "D": 500, "   ": 0, "   i  ": 1}

    for k, v in test_values.items():
        actual_value = roman_numerals_v1(k)
        print("V1 - String = {0}, Expected = {1}, Actual = {2}".format(k, v, actual_value))
        assert actual_value == v, "Input = {0}, Expected Value = {1}, Actual Value {2}".format(k, v, actual_value)

    for k, v in test_values.items():
        actual_value = roman_numerals_v2(k)
        print("V2 - String = {0}, Expected = {1}, Actual = {2}".format(k, v, actual_value))
        assert actual_value == v, "Input = {0}, Expected Value = {1}, Actual Value {2}".format(k, v, actual_value)