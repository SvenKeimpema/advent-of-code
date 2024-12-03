class FileReader:
    @classmethod
    def read(cls, path: str) -> str:
        with open(path, "r") as file:
            return file.read()