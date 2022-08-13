from program_options import *
from tkinter import *


def main():

    window = Tk()
    window.title('FINAL PROJECT')
    window.geometry('390x190')
    window.resizable(False, False)
    widgets = OPTIONS(window)
    window.mainloop()


if __name__ == '__main__':
    main()
