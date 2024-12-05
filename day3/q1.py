from reader import FileReader

if __name__ == "__main__":
    data = FileReader.read("day3/data.txt")
    mul_lines: list[str] = data.split("mul")
    s = 0

    for line in mul_lines:
        if not line.startswith("("):
            continue

        r_bracket = line.find(")")

        if r_bracket == -1:
            continue
        
        parts = line.split(",", 1)

        if len(parts) <= 1:
            continue

        num1 = parts[0][1:]
        num2 = parts[1][:parts[1].find(")")]

        try:
            num1, num2 = int(num1), int(num2)
        except ValueError:
            continue

        s += num1 * num2
    
    print(s)