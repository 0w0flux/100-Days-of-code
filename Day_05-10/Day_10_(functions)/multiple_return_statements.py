def format_name(first_name, last_name):
    if first_name == "" or last_name == "":
        return "You did not provide valid inputs!" # Ends the function early
    
    formated_first_name = first_name.title()
    formated_last_name = last_name.title()

    return f"{formated_first_name} {formated_last_name}"

print(format_name(input("What is your first name? "), input("What is your last name? ")))