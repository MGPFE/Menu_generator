"""
CHECK MY GITHUB FOR OTHER PROJECTS
https://github.com/MGPFE

HOW TO USE
FIRST CREATE AN OBJECT FOR EXAMPLE menu = Menu_generator()
HERE YOU CAN PASS VARIOUS ARGUMENTS TO CUSTOMIZE THE MENU TO YOUR LIKING

EXAMPLE OF MAIN MENU CREATION
choice = menu.main_menu(**{
    "main": ["Test1", "Test2", "Test3"],
    "side": ["test_side1", "test_side2", "test_side3", "test_side4", "test_side5"]
})
THIS CREATES MAIN MENU

EXAMPLE OF SUB MENU CREATION
choice = menu.sub_menu(**{
    "title": ["Test Title"],
    "main": ["test1", "test2", "test3"]
})

BOTH FUNCTIONS DISPLAY A CHOICE INPUT FOR USER AT THE END
THE RETURN VALUE SHOULD BE INT BUT YOU CAN USE ALL THE OTHER DATATYPES TOO
"""
from datetime import datetime
from sys import platform
import traceback
import os


class Menu_generator:
    def __init__(
        self,
        app_name="Default app name",
        app_ver="1.0",
        side_title="Default side title",
        side_bar=True,
        side_spacing=15,
        separator=True,
        enumeration=True,
        decoration=True,
        choice_msg="Choice"
    ):
        self.app_name = app_name
        self.app_ver = app_ver
        self.side_bar = side_bar
        self.side_title = side_title
        self.side_spacing = side_spacing
        self.separator = separator
        self.enumeration = enumeration
        self.decoration = decoration
        self.choice_msg = choice_msg
        self.clear = Menu_generator.check_os()

    @staticmethod
    def check_os():
        if platform == "linux" or platform == "darwin":
            return "clear"
        elif platform == "win32":
            return "cls"

    def logger(func):
        def wrapper(self, *args, **kwargs):
            try:
                return func(self, *args, **kwargs)
            except Exception:
                TIME = datetime.now().strftime("%H:%M:%S")
                TRACEBACK = traceback.format_exc()
                with open("crash_log.txt", "a") as f:
                    f.write(f"{TIME} -- {TRACEBACK}\n")
                input(TRACEBACK)
        return wrapper

    def format_entries(self, main, side=None):
        # THIS METHOD HAS TO BE CALLED BEFORE SPLITTING SIDE
        # INTO MULTIPLE LISTS!!!
        if self.enumeration:
            for index, entry in enumerate(main, 1):
                main[index - 1] = f"{index}. {entry}"

        if self.decoration:
            for index, entry in enumerate(main):
                main[index] = f"|{entry}"
            try:
                for index, entry in enumerate(side):
                    side[index] = f"|{entry}"
            except TypeError:
                pass

        if side:
            return main, side

        return main

    """
    THIS METHOD IS HANDLED BY main_menu AND sub_menu
    IT CHECKS IF DATA FOLLOWS GUIDELINES IN
    main_menu METHOD
    """
    def validate_data(self, dct):
        if dct:
            for k, v in dct.items():
                if not isinstance(v, list):
                    raise Exception(f"Value from key {k} is not a list!")
        else:
            raise Exception("You didn't pass anything to the function!")

    @logger
    def main_menu(self, **kwargs) -> int:
        """
        ARGUMENTS NEED TO BE PASSED IN A DICTIONARY
        KEYWORDED AND WITH UNPACK OPERATOR
        EX. **{"main": ["item1", "item2"]}
        EACH VALUE FROM KWARGS KEY VALUE PAIRS
        HAS TO BE A LIST OR A TUPLE IN ORDER
        TO GENERATE IT TO THE SCREEN
        """
        os.system(self.clear)
        self.validate_data(kwargs)

        main = kwargs.get("main")
        main_len = len(main)
        side = kwargs.get("side")
        side_len = len(side) if side else 0

        self.SPACE = 45
        # PREVENTS MENU OPTIONS FROM TOUCHING SIDE MENU
        # THESE NUMBERS ARE PICKED FOR BEST LOOK
        for entry in main:
            if len(entry) >= 25:
                self.SPACE = len(entry) + 25

        if self.side_bar:
            main, side = self.format_entries(main[:], side[:])

            """
            THE SIDE CONTENT WILL BE SLICED INTO
            MULTIPLE LIST BASED ON THE LENGTH OF main
            THIS IS DONE IN ORDER TO MAINTAIN EVENLY
            POSITIONED MENU AND SIDE MENU ENTRIES
            """
            slicer = main_len
            sliced_side = []
            amount = side_len // main_len

            """
            IF DIVIDING LENGTH OF SIDE CONTENT BY
            LENGTH OF MAIN CONTENT GIVES US ANYTHING OTHER
            THAN 0 THEN THAT MEANS SIDE LIST HAS TO BE SLICED
            """
            # if amount != 0:
            current_point = 0
            for _ in range(amount):
                sliced = side[current_point:(main_len + current_point)]
                sliced_side.append(sliced)
                current_point += main_len

            # GET THE UNEVEN REMAINDER FROM side
            for li in sliced_side:
                for i in li:
                    side.remove(i)
            if side:
                sliced_side.append([i for i in side])
            # COMMENTED IF ENDS HERE

            print(f"{self.app_name} {self.app_ver}")

            # MENU GENERATION WITH SIDEBAR
            if self.side_bar:
                # self.SPACE WAS HERE
                print(f"{self.side_title:>{self.SPACE}}")

                for index, entry in enumerate(main, 1):
                    sd = []
                    for i in range(len(sliced_side)):
                        try:
                            sd.append(sliced_side[i][index - 1])
                        except IndexError:
                            i += 1
                            pass

                    side_str = str()
                    for string in sd:
                        side_str += f"{string:<{self.side_spacing}}"
                    print(f"{entry:<{self.SPACE-18}}{side_str}")

        else:
            print(f"{self.app_name} {self.app_ver}\n")
            main = self.format_entries(main[:])
            for entry in main:
                print(entry)

        """
        THIS PRINTS THE EXIT SEPARATOR
        THE NUMBER 18 IN THIS IS
        PICKED BASED ON THE BEST LOOK
        """
        if self.separator:
            x = str()
            print(f"{x:-<{self.SPACE - 18}}")
        else:
            print("")

        print(f"{main_len + 1}. Exit")
        choice = input(f"\n{self.choice_msg}: ")
        print(choice)
        return choice

    @logger
    def sub_menu(self, **kwargs) -> int:
        os.system(self.clear)
        self.validate_data(kwargs)

        title = kwargs.get("title")
        main = kwargs.get("main")

        main = self.format_entries(main[:])
        print(f"{title[0]}\n")
        for entry in main:
            print(entry)

        choice = input(f"\n{self.choice_msg}: ")
        print(choice)
        return choice
