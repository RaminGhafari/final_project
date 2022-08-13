from delete_record import *
import tkinter.messagebox
from add_record import *
from tkinter import *


class OPTIONS:
    """
    Class representing a window -- main window (or options window) for the students records program.
    """
    def __init__(self, window):
        """
        Constructor to create initial state of the main window; for example, creating frames and labels for add, view,
        delete, and close buttons.
        :param window: A window that already uses tkinter library
        """
        self.window = window

        # Frame for name of the program
        self.frame_select = Frame(self.window)
        self.label_select = Label(self.frame_select, text="Students' Records",
                                  font=('Times New Roman', 15))
        self.label_select.pack(padx=120, pady=0, side='left')
        self.frame_select.pack(anchor='w', pady=10)

        # Frame for creating add and search buttons
        self.frame_add = Frame(self.window)
        self.button_add = Button(self.frame_add, text="Add a student's record",
                                 font=('Times New Roman', 13), command=self.add)
        self.button_search = Button(self.frame_add, text="View a student's record",
                                    font=('Times New Roman', 13), command=self.view)
        self.button_add.pack(padx=5, pady=0, side='left')
        self.button_search.pack(padx=20, pady=0, side='left')
        self.frame_add.pack(anchor='w', pady=5)

        self.frame_delete = Frame(self.window)
        self.button_delete = Button(self.frame_delete, text="Delete a student's record",
                                    font=('Times New Roman', 13), command=self.delete)
        self.button_delete.pack(padx=5, pady=0, side='right')
        self.frame_delete.pack(anchor='w', pady=5)

        # Frame for creating close button
        self.frame_close = Frame(self.window)
        self.button_close = Button(self.frame_close, text='CLOSE',
                                    font=('Times New Roman', 12), command=self.window.destroy)
        self.button_close.pack(padx=25, pady=0, side='right')
        self.frame_close.pack(anchor='e', pady=5)



    def add(self):
        """
        Method to be called when a user clicks on the add a student's record button.
        This method creates a new window using tkinter library and passes it as an instance to a new class named ADD.
        """
        window = Toplevel()
        window.title("ADD A RECORD")
        window.geometry('290x290')
        window.resizable(False, False)
        widgets = ADD(window)
        window.mainloop()

    def view(self):
        """
        Method to be called when a user clicks on the view a student's record button.
        This method creates a new window using tkinter library and passes it as an instance to a new class named VIEW.
        """
        window = Toplevel()
        window.title("VIEW A RECORD")
        window.geometry('330x350')
        window.resizable(False, False)
        widgets = VIEW(window)
        window.mainloop()

    def delete(self):
        """
        Method to be called when a user clicks on the delete a student's record button.
        This method creates a new window using tkinter library and passes it as an instance to a new class named DELETE.
        """
        window = Toplevel()
        window.title("DELETE A RECORD")
        window.geometry('330x350')
        window.resizable(False, False)
        widgets = DELETE(window)
        window.mainloop()