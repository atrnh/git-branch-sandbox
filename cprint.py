"""
It's like pprint, except with colors :D
"""


def cprint(s, *msg_types, indent=0):
    styles = [getattr(colors, t, '') for t in msg_types]
    end = colors.end if msg_types else ''
    indent = ' ' * indent

    print(''.join(styles) +
          indent +
          s +
          end
          )

class symbols:
    ballotCross = '✘'
    bullet = '•'
    check = '✔'
    cross = '✖'
    ellipsis = '…'
    heart = '❤'
    info = 'ℹ'
    line = '─'
    middot = '·'
    minus = '－'
    plus = '＋'
    question = '?'
    questionFull = '？'
    questionSmall = '﹖'
    pointer = '❯'
    pointerSmall = '›'
    warning = '⚠'

class colors:
    end = '\033[0m'

    class fg:
        black = '\033[30m'
        red = '\033[31m'
        green = '\033[32m'
        yellow = '\033[33m'
        blue = '\033[34m'
        magenta = '\033[35m'
        cyan = '\033[36m'
        white = '\033[37m'

        # bright black \033[90m
        # bright red \033[91m
        # bright green \033[92m
        # bright yellow \033[93m
        # bright blue \033[94m
        # bright magenta \033[95m
        # bright cyan \033[96m
        # bright white \033[97m

    class bg:
        black = '\033[40m'
        red = '\033[41m'
        green = '\033[42m'
        yellow = '\033[43m'
        blue = '\033[44m'
        magenta = '\033[45m'
        cyan = '\033[46m'
        white = '\033[47m'


