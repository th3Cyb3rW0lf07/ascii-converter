def ascii_to_char(ascii_codes):
    characters = [chr(code) for code in ascii_codes]
    return characters

def main():
    user_input = input("Enter ASCII codes separated by commas: ")
    ascii_strings = user_input.split(',')
    ascii_codes = [int(code.strip()) for code in ascii_strings]

    characters = ascii_to_char(ascii_codes)

    output_strings = ''.join(characters)

    print("The corresponding characters are:", output_strings)

if __name__ == "__main__":
    main()
