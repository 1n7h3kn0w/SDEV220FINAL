from pickle import dumps, loads

def ClearFile(PATH: str) -> None:
    with open(PATH, 'w+') as FILE:
        FILE.write("")

def WriteFile(PATH: str, data: tuple) -> None:
    with open(PATH, 'wb') as file:
        file.write(dumps(data))

def ReadFile(PATH: str) -> tuple:
    default = ({}, {}, {}, 0, 0, 0)
    with open(PATH, 'rb') as file:
        read = file.read()
    
    if(read == b'' or read == dumps(default)):
        return default
    else:
        return loads(read)