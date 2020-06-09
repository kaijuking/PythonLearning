def roman_numerals(x):
    roman_val = {"i": 1, "v": 5, "x": 10, "l": 50, "c": 100, "m": 1000}

    total = 0
    tmp_list = []
    input_length = len(x)
    input = x.lower()

    # covers the case where the inputted value is only one character
    if input_length > 0 and input_length < 2:
        for i in range(len(input)):
            total += roman_val[input[i]]

    # covers the case where the inputted value is two or more characters
    if input_length > 1:
        for i in range(len(input)):
            tmp_list.append(roman_val[input[i]])

    # compare two indexes to see if 'i + 1' is greater than 'i'
    for i in range(len(tmp_list) - 1):
        if tmp_list[i + 1] > tmp_list[i]:
            tmp_list[i + 1] = tmp_list[i + 1] - tmp_list[i]
            tmp_list[i] = 0

    # total up all the values in the list
    for i in tmp_list:
        total += i

    print("Input = {0}, Actual Value = {1}".format(input, str(total)))
    return total


if __name__ == "__main__":
    test_values = {"i": 1, "iv": 4, "lxx": 70, "MMXX": 2020, "xiv": 14, "mmxlix": 2049, "m": 1000, "MCMLIV": 1954,
                   "MCCXXXIV": 1234, "": 0}

    for k, v in test_values.items():
        actual_value = roman_numerals(k)
        assert actual_value == v, "Input = {0}, Expected Value = {1}, Actual Value {2}".format(k, v, actual_value)