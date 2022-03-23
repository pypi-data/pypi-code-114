import os
from typing import Union


class init:
    # --- PRIVATE FUNCTIONS ---
    # inits the db
    def __init__(self, name: str) -> None:
        if not os.path.exists(name):
            name = f"{name}.txt"
            with open(name, "a") as db:
                os.utime(name, None)
                db.close()
        self.name: str = name
        self.__update_length()

    # updates the length of the db
    def __update_length(self) -> None:
        self.length = self.count(self.get_all())

    # -- PUBLIC FUNCTIONS ---
    # adds elements to the db
    def add(self, *elements: Union[str, int]) -> None:
        for element in elements:
            element = str(element)
            with open(self.name, "r+") as db:
                to_write: str = "\n" if not len(db.read()) == 0 else ""
                to_write += element
                db.write(to_write)
                db.close()
        self.__update_length()

    # removes all the elements from the db
    def remove_all(self) -> None:
        with open(self.name, "w") as db:
            db.write("")
            db.close()
        self.__update_length()

    # removes elements to the db
    def remove_by_element(self, *elements: Union[str, int]) -> None:
        for element in elements:
            element = str(element)
            with open(self.name, "r+") as db:
                lines: list = db.read().split("\n")
                for line in lines:
                    if line == element:
                        lines.remove(line)
                self.remove_all()
                for line in lines:
                    self.add(line)
                db.close()
        self.__update_length()

    # removes elements to the db by string
    def remove_by_string(self, *strings: Union[str, int]) -> None:
        for string in strings:
            string = str(string)
            with open(self.name, "r+") as db:
                lines: list = db.read().split("\n")
                for line in lines:
                    if string in line:
                        lines.remove(line)
                self.remove_all()
                for line in lines:
                    self.add(line)
            db.close()
        self.__update_length()

    # removes elements to the db by index
    def remove_by_index(self, *indexes: Union[str, int]) -> None:
        fixer: int = 0
        for index in indexes:
            index = int(index)
            with open(self.name, "r+") as db:
                lines: list = db.read().split("\n")
                lines.remove(lines[index - fixer])
                self.remove_all()
                for line in lines:
                    self.add(line)
            db.close()
            fixer += 1
        self.__update_length()

    # gets all the elements from the db
    def get_all(self) -> str:
        with open(self.name, "r") as db:
            data: str = db.read()
            db.close()
        return data

    # gets all the elements from the db by string
    def get_by_string(self, *strings: Union[str, int]) -> str:
        to_return: str = ""
        for string in strings:
            string = str(string)
            with open(self.name, "r") as db:
                lines: list = db.read().split("\n")
                for line in lines:
                    to_return += f"{line}\n" if string in line else ""
                db.close()
        fixed_to_return: str = to_return[:-1]
        return fixed_to_return

    # gets the element from the db by index
    def get_by_index(self, *indexes: Union[str, int]) -> str:
        to_return: str = ""
        for index in indexes:
            with open(self.name, "r") as db:
                lines: list = db.read().split("\n")
                to_return += f"{lines[index]}\n"
                db.close()
        fixed_to_return: str = to_return[:-1]
        return fixed_to_return

    # counts the elements in txtdb output
    def count(self, txtdb_output: Union[str, int, float]):
        txtdb_output = str(txtdb_output)
        elements = txtdb_output.split("\n")
        elements_length = len(elements)
        return elements_length
