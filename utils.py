def get_int(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Please enter a valid number.")


def get_string(message):
    return input(message).strip()