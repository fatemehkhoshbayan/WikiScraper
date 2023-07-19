import io
import unittest
from unittest import mock
from unittest.mock import patch

from ..main import SCIENTISTS
from wiki_scraper import Scraper


class TestRobot(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.robot = Scraper("Quandrinaut", SCIENTISTS)

    def test_calculate_age_birth_month_after_death_month(self):
        birth_date = "7 November 1867"
        death_date = "4 July 1934"
        self.assertEqual(self.robot._calculate_age(birth_date, death_date), 66)

    def test_calculate_age_birth_month_before_death_month(self):

        birth_date = "7 November 1867"
        death_date = "4 December 1934"
        self.assertEqual(self.robot._calculate_age(birth_date, death_date), 67)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_say_hello(self, mock_stdout):
        self.robot.say_hello()
        self.assertIn(self.robot.name, mock_stdout.getvalue())


if __name__ == "__main__":
    unittest.main()
