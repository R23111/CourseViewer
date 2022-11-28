import os

class Videos_Folder:
    
    def __init__(self, path:str) -> None:
        if path == ".":
            self._base_path = os.getcwd()
        if path[0] == "~":
            path.replace("~", os.path.expanduser())
        self._base_path = ""