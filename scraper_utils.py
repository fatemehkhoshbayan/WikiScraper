import re
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from helpers import RegexPaterns, Xpath


options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()))


def open_webpage(webpage):
    """Open the webpage and then maximize it"""
    driver.get(webpage)
    driver.maximize_window()


def get_element(element_path: str):
    """Get element by Xpath and clean the text"""
    element_text = driver.find_element(By.XPATH, element_path)
    try:
        element_text = re.sub(RegexPaterns.CLEAN_TEXT, "", element_text.text)
        return element_text
    except:
        return ""


def get_first_two_paragraphs():
    first_paragraph_text = get_element(Xpath.PARAGRAPH.format(2))
    second_paragraph_text = get_element(Xpath.PARAGRAPH.format(3))
    if first_paragraph_text == "":
        first_paragraph_text = get_element(Xpath.PARAGRAPH.format(3))
        second_paragraph_text = get_element(Xpath.PARAGRAPH.format(4))
    return first_paragraph_text, second_paragraph_text


def get_date_of_birth(element_path):
    text = get_element(element_path)
    date_of_birth = re.findall(RegexPaterns.DATE, text)[0]
    return date_of_birth


def get_date_of_death(element_path):
    text = get_element(element_path)
    died = re.findall(RegexPaterns.DATE, text)[0]
    return died


def get_dates_info():
    try:
        date_of_birth = get_date_of_birth(Xpath.DATE.format(3))
        date_of_death = get_date_of_death(Xpath.DATE.format(4))
    except IndexError:
        date_of_birth = get_date_of_birth(Xpath.DATE.format(4))
        date_of_death = get_date_of_death(Xpath.DATE.format(5))
    return date_of_birth, date_of_death


def get_all_info():
    first_paragraph_text, second_paragraph_text = get_first_two_paragraphs()
    date_of_birth, date_of_death = get_dates_info()
    return first_paragraph_text, second_paragraph_text, date_of_birth, date_of_death


def scrape_scientist_info_from_wiki(scientist_name):
    """Scrap the first two paragraph and date of birth, death"""
    main_url = f"https://en.wikipedia.org/wiki/{scientist_name}"
    open_webpage(main_url)
    first_paragraph_text, second_paragraph_text, date_of_birth, date_of_death = get_all_info()
    time.sleep(1.3)
    return first_paragraph_text, second_paragraph_text, date_of_birth, date_of_death
