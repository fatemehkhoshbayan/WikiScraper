from wiki_scraper import Scraper

SCIENTISTS = ["Albert Einstein", "Isaac Newton",
              "Marie Curie", "Charles Darwin", 
              "Johann Sebastian Bach", "Wolfgang Amadeus Mozart", 
              "Leonardo da Vinci"]

scraper = Scraper("WikiScraper", SCIENTISTS)


def introduce_yourself():
    scraper.say_hello()
    scraper.say_capabilities()


def say_goodby():
    scraper.say_goodbye()


def display_scientists_info():
    while True:
        scraper.display_scientist_list()
        try:
            sci_num = scraper.get_user_input()
            scraper.get_scientist_info(sci_num)
        except:
            break


def main():
    introduce_yourself()
    display_scientists_info()
    say_goodby()


if __name__ == "__main__":
    main()
