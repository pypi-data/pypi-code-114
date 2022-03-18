def get_input(
    prompt="Enter a value: ",
    validator=lambda x: True,
    error_message="Invalid input. Please try again.",
):
    while True:
        value = input(prompt)
        if validator(value):
            return value
        print(error_message)
