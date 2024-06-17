class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __repr__(self):
        return f"Token({self.type}, {repr(self.value)})"


def tokeniser(string: str):
    tokens = []
    for i in range(len(string)):
        if string[i].isdigit():
            if tokens and tokens[-1].type == "INTEGER":
                tokens[-1].value = tokens[-1].value * 10 + int(string[i])
            else:
                tokens.append(Token("INTEGER", int(string[i])))
        elif string[i] == " ":
            pass
        elif string[i] == "+":
            tokens.append(Token("PLUS", "+"))
        elif string[i] == "*":
            tokens.append(Token("TIMES", "*"))
        elif string[i] == "-":
            tokens.append(Token("MINUS", "-"))
        elif string[i] == "/":
            tokens.append(Token("DIVIDE", "/"))
        elif string[i] == "(":
            tokens.append(Token("LPAREN", "("))
        elif string[i] == ")":
            tokens.append(Token("RPAREN", ")"))
        else:
            raise SyntaxError(f"{i} {string[i]}")
    return tokens


def step(tokens: list):
    for i in range(len(tokens)-2):
        if tokens[i].type == "INTEGER":
            if tokens[i+1].type == "TIMES":
                    r = tokens[i] * tokens[i+2]



def syntax_check(string: str):
    compt = 0
    for i in range(len(string)):
        if compt < 0:
            return False
        if string[i] == "(":
            compt += 1
        elif string[i] == ")":
            compt -= 1
    for i in range(len(string)-1):
        if string[i] in ["+", "*", "-", "/"] and string[i+1] in ["+", "*", "-", "/"]:
            return False
    if string[0] in ["+", "*", "-", "/"] or string[-1] in ["+", "*", "-", "/"]:
        return False
    return compt == 0

# print(syntax_check("183)7(3+g)dyd+"))


def main(chaine: str):
    if syntax_check(chaine):
        tokens = tokeniser(chaine)
        print(tokens)


if __name__ == "__main__":
    main(input("calc>"))

