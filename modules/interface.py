def use_colours(colour):
    colours = {
        'clean': '\033[m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'magenta': '\033[35m',
        'cyan': '\033[36m',
        'gray': '033[37m',
        'bold': '\033[1m',
        'underline': '\033[4m'
    }
    return colours[colour]

def menu(lst):
    from modules.datas import readInt
    for index, lst in enumerate(lst, start=1):
        print(f"{use_colours('blue')}{index} - {lst}{use_colours('clean')}")
    line()
    answer = readInt(f'{use_colours('magenta')}\nEnter an option: {use_colours('clean')}')
    return answer

def line():
    print("=" * 30)

def heading(txt):
    line()
    print(use_colours('green'), txt.center(30), use_colours('clean'))
    line()
