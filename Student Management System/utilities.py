exiting_text = 'Exited From The System'
error_text = 'Please choose your option currectly. Try again!(1/2/3/4/5/6)'


def style(text):
    def underline(*args):
        print('*'* 100)
        text(*args)
        print('*'* 100)
    return underline


