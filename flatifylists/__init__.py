output = []
def flatifyList(input_list):
    if not isinstance(input_list, list):
        raise TypeError('Only input of type `list` is allowed.')
    for i in input_list:
        if type(i) == list:
            flatifyList(i)
        else:
            output.append(i)
    return output