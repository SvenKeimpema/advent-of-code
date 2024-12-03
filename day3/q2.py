from reader import FileReader
from dataclasses import dataclass
from pprint import pp

@dataclass
class Token:
    value: str
    ty: str

    def __str__(self) -> str:
        return "value: " + self.value + " type: " + self.ty

def parse(data: str) -> list[Token]:
    tokens: list[Token] = []
    idx = 0
    while idx < len(data):
        if data[idx:idx+len("mul")] == "mul":
            tokens.append(Token(ty="mul", value=""))
            idx += len("mul")
            continue
        elif data[idx:idx+len("do()")] == "do()":
            tokens.append(Token(ty="do", value=""))
            idx += len("do()")
            continue
        elif data[idx:idx+len("don't()")] == "don't()":
            tokens.append(Token(ty="don't", value=""))
            idx += len("don't()")
            continue
        elif data[idx].isnumeric():
            num = ""
            while data[idx].isnumeric():
                num += data[idx]
                idx += 1
            tokens.append(Token(ty="num", value=num))
            continue
        elif data[idx] == "(":
            tokens.append(Token(ty="l_paren", value=""))
        elif data[idx] == ")":
            tokens.append(Token(ty="r_paren", value=""))
        elif data[idx] == ",":
            tokens.append(Token(ty="comma", value=""))
        else:
            tokens.append(Token(ty="invalid", value=""))

        idx += 1

    return tokens


if __name__ == "__main__":
    data = FileReader.read("day3/data.txt").replace(" ", "")
    idx = 0
    tokens = parse(data)
    do = True
    s = 0
    while idx < len(tokens):
        token = tokens[idx]
        if token.ty == "do":
            do = True
        elif token.ty == "don't":
            do = False

        if do and len(tokens) > idx+5 and token.ty == "mul" and tokens[idx+1].ty == "l_paren" and tokens[idx+2].ty == "num" and tokens[idx+3].ty == "comma" and tokens[idx+4].ty == "num" and tokens[idx+5].ty == "r_paren":
            s += int(tokens[idx+2].value)*int(tokens[idx+4].value)
        
        idx += 1
    
    print(s)
            