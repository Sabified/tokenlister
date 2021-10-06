# Tokens

TOKENS = {
    "0": "ZERO",
    "1": "ONE"
}

T_UNKNOWN = "UNKNOWN"

tokens = []

def apply_tokens(string):
    current_character = 0

    for char in string:
        if char in TOKENS:
            tokens.append(TOKENS[char])
        else:
            print("Unknown Character: \'" + char + "\' Character " + str(current_character + 1))
            tokens.append(T_UNKNOWN)
        
        current_character += 1

    print(tokens)