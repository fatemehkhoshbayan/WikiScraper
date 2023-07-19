class Xpath:
    PARAGRAPH = '//*[@id="mw-content-text"]/div[1]/p[{}]'
    DATE = '//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[{}]/td[1]'


class RegexPaterns:
    CLEAN_TEXT = r"[\(\[]\d?[\)\]]"
    DATE = r"\d\d? [a-zA-Z]* \d\d\d\d"


class RobotStrings:
    HELLO = "\nHello, my name is {}"
    CAPPABILITY = (
        "\nI can give you some information about some celebrities."
        "\nI will retrieve this information from wikipedia."
    )
    USER_SCIENTIST_PROMPT = (
        "\nwhich celebrity would you like to know about (Enter the number:)"
    )
    USER_INPUT = "\nEnter celebrity's number (or input anything else to exit): "
    GOODBY = (
        "\n\nGoodbye, {} wishs you a good day and hopes you learnt alot."
        " Come back soon and ask about more celebrities.\n "
    )
    DISPLAY_INFO = (
        "\n{} born in {}, and died at the age of {} years old in {}."
        "\n\n\nHere is some more information about this brilliant celebrity: \n\n{} \n\n{}"
    )
