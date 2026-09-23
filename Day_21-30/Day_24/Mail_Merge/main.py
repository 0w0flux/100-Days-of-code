def main():
    open_letter()
    open_names()
    pass

def open_letter():
    global template
    with open("Day_21-30/Day_24/Mail_Merge/template.txt", mode="r") as file:
        template = file.read()
        print(template)

def open_names():
    with open("Day_21-30/Day_24/Mail_Merge/names.txt", mode="r") as file:
        names = file.readlines()
        
        for name in names:
            clean_name = name.strip()
            new_letter = template.replace("[name]", clean_name)

            with open(f"Day_21-30/Day_24/Mail_Merge/Letters\\{clean_name}.txt", "w") as letter:
                letter.write(new_letter)

if __name__ == "__main__":
    main()