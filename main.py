# Tokens

TOKENS = {
    "0": "ZERO",
    "1": "ONE",
    "2": "TWO",
    "3": "THREE",
    "4": "FOUR",
    "5": "FIVE",
    "6": "SIX",
    "7": "SEVEN",
    "8": "EIGHT",
    "9": "NINE"
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