from reader import FileReader

if __name__ == "__main__":
    print(len(FileReader.read("day3/text.txt").split("\n")))