# Tokens
T_UNKNOWN = "UNKNOWN"
T_ZERO = "ZERO"
T_ONE = "ONE"

tokens = []
current_character = 0

def apply_tokens(string):
    global current_character

    for char in string:
        if char == "0":
            tokens.append(T_ZERO)
        elif char == "1":
            tokens.append(T_ONE)
        else:
            print("Unknown Character: \'" + char + "\' Character " + str(current_character + 1))
            tokens.append(T_UNKNOWN)
        
        current_character += 1

    print(tokens)