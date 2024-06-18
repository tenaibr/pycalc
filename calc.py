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
            raise SyntaxError(f"char {string[i]} at {i}")
    return tokens


def calc(tokens: list[Token]):
    r = tokens[0].value
    prio = False
    for i in range(len(tokens)-2):
        for a in tokens:
            if a.type == "TIMES" or a.type == "DIVIDE":
                prio = True
        if i >= len(tokens)-2:
            return calc(tokens)
        if tokens[i].type == "LPAREN":
            for end in range(i, len(tokens)):
                if tokens[end].type == "RPAREN":
                    break
            tokens[i].value = calc(tokens[i+1:end])
            tokens[i].type = "INTEGER"
            for _ in range(end-i):
                tokens.pop(i+1)
        elif tokens[i].type == "INTEGER":
            if tokens[i+2].type == "INTEGER":
                if tokens[i+1].type == "TIMES":
                    r = tokens[i].value * tokens[i+2].value
                elif tokens[i+1].type == "DIVIDE":
                    r = tokens[i].value / tokens[i+2].value
                if not prio:
                    if tokens[i+1].type == "PLUS":
                        r = tokens[i].value + tokens[i+2].value
                    elif tokens[i+1].type == "MINUS":
                        r = tokens[i].value - tokens[i+2].value
                if r:
                    for _ in range(2):
                        tokens.pop(i+1)
                    tokens[i].value = r
        elif tokens[i].type in ["PLUS", "TIMES", "MINUS", "DIVIDE"]:
            pass
        print(tokens)
    if len(tokens) > 1:
        return calc(tokens)
    return r


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
        return calc(tokens)
    else:
        return "Erreur de syntaxe"


if __name__ == "__main__":
    while True:
        try:
            print(main(input(">>> ")))
        except KeyboardInterrupt:
            print("\nExiting...")
            break
