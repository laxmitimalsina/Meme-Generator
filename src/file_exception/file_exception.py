import sys


class FileExceptions(Exception):
    def __init__(self, path, message=None):
        if message is None:
            message = ""

        self.path = path
        self.message = message

    @property
    def show(self):
        full_message = self.message + ": " + self.path
        print(full_message, file=sys.stderr)
        return full_message


class InvalidFilePath(FileExceptions, FileNotFoundError):
    def __init__(self, path, msg="File path not found"):
        super(InvalidFilePath, self).__init__(path, msg)


class InvalidFile(FileExceptions):
    def __init__(self, path, msg="Invalid file extension"):
        super(InvalidFile, self).__init__(path, msg)
