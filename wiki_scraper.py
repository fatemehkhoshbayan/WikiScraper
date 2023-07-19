from datetime import datetime

from colorama import Fore, Style
from colorama import init as colorama_init

from helpers import RobotStrings
from scraper_utils import scrape_scientist_info_from_wiki

colorama_init()


class Scraper:
    def __init__(self, name, known_scientists):
        self.name = name
        self.known_scientists = known_scientists

    def say_hello(self):
        print(RobotStrings.HELLO.format(self.name))

    def say_capabilities(self):
        print(RobotStrings.CAPPABILITY)

    def get_user_input(self):
        return int(input(RobotStrings.USER_INPUT))

    def _calculate_age(self, date_of_birth, date_of_death):
        birth = datetime.strptime(date_of_birth, "%d %B %Y")
        death = datetime.strptime(date_of_death, "%d %B %Y")
        age = (
            death.year
            - birth.year
            - ((death.month, death.day) < (birth.month, birth.day))
        )
        return age

    def display_scientist_list(self):
        print(RobotStrings.USER_SCIENTIST_PROMPT)
        for i, name in enumerate(self.known_scientists):
            print(f"{i+1}: {name}")

    def say_goodbye(self):
        print(RobotStrings.GOODBY.format(self.name))

    def _generate_scientist_info_message(self, scientist_name):
        (
            first_paragraph_text,
            second_paragraph_text,
            date_of_birth,
            date_of_death,
        ) = scrape_scientist_info_from_wiki(scientist_name)
        age = self._calculate_age(date_of_birth, date_of_death)
        display_info = RobotStrings.DISPLAY_INFO.format(
            scientist_name, date_of_birth, age, date_of_death, first_paragraph_text, second_paragraph_text
        )
        return display_info

    def get_scientist_info(self, sci_num: int):
        scientist_info = self._generate_scientist_info_message(
            self.known_scientists[sci_num - 1]
        )
        print(f"{Fore.LIGHTGREEN_EX}{scientist_info}{Style.RESET_ALL}")
