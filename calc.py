class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __repr__(self):
        return f"Token({self.type}, {self.value})"

def tokeniser(string: str):
    tokens = []
    for i in range(len(string)):
        if string[i].isdigit():
            if tokens and tokens[-1].type == "INTEGER":
                tokens[-1].value = tokens[-1].value * 10 + int(string[i])
            else:
                tokens.append(Token("INTEGER", int(string[i])))
        elif string[i] == "+":
            tokens.append(Token("PLUS", "+"))
    return tokens


def syntax_check(string: str):
    compt = 0
    for i in range(len(string)):
        if compt < 0:
            return False
        if string[i] == "(":
            compt +=1
        elif string[i] == ")":
            compt -= 1
    for i in range(len(string)-1):
        if string[i] in ["+", "*", "-", "/"] and string[i+1] in ["+", "*", "-", "/"]:
            return False
    return compt == 0

# print(syntax_check("183)7(3+g)dyd+"))

def main(chaine: str):
    if syntax_check(chaine):
        tokens = tokeniser(chaine)
        print(tokens)

if __name__ == "__main__":
    main(input("calc>"))