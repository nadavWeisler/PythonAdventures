def get_type(value):
    try:
        int(value)
        return "int"
    except ValueError:
        try:
            float(value)
            return "float"
        except ValueError:
            return "string"


if __name__ == '__main__':
    input_value = input("Enter value: ")
    print(get_type(input_value))
    input_value = input("Enter value: ")
    print(get_type(input_value))
    input_value = input("Enter value: ")
    print(get_type(input_value))
