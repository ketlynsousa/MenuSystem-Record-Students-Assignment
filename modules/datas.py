def readInt(txt):
    while True:
        try:
            num = int(input(txt))
        except (TypeError, ValueError):
            print(f"{use_colours('red')}ERROR!Enter a valid integer number.{use_colours('clean')}")
        except KeyboardInterrupt:
            print(f"{use_colours('red')}\nThe user preferred not to enter any number.{use_colours('clean')}")
            return 0
        else:
            return num

def readFloat(txt):
    while True:
        try:
            text = str(input(txt)).replace(',', '.')
            num = float(text)
        except (ValueError, TypeError):
            print(f"{use_colours('red')}ERROR!Enter a valid decimal number.{use_colours('clean')}")
        except KeyboardInterrupt:
            print(f"{use_colours('red')}\nThe user preferred not to enter any number.{use_colours('clean')}")
            return 0.0
        else:
            return num
from modules.interface import use_colours
