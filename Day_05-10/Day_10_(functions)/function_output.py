def format_name(first_name, last_name):
    formated_first_name = first_name.title()
    formated_last_name = last_name.title()

    return f"{formated_first_name} {formated_last_name}"

print(format_name("owE", "cARseTeNS"))



def function_1(text):
    return text + text

def function_2(text):
    return text.title()


print(function_1("hello"))

output = function_2(function_1("hello"))
print(output)

###########################################################

output_2 = function_1("hello")
print(function_2(output_2))
