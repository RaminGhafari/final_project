from program_options import *
from assign_grade import *
import tkinter.messagebox
from view_record import *
from tkinter import *
import csv


class ADD:
    """
    Class representing a window -- add a student's record window for adding a student's records to the file.
    """

    def __init__(self, window):
        """
        Constructor to create initial state of add window; for example, creating frames, labels, and entries for
        student's ID, first name, last name, and score. Also, creating frames and labels for save and close
        buttons.
        :param window: A window that already uses tkinter library
        """
        self.window = window

        # Frame for student's ID
        self.frame_ID = Frame(self.window)
        self.label_ID = Label(self.frame_ID, text='Student ID', font=('Times New Roman', 12))
        self.entry_ID = Entry(self.frame_ID)
        self.label_ID.pack(padx=5, side='left')
        self.entry_ID.pack(padx=5, side='left')
        self.frame_ID.pack(anchor='w', pady=10)

        # Frame for student's first name
        self.frame_firstname = Frame(self.window)
        self.label_firstname = Label(self.frame_firstname, text='First name',
                                     font=('Times New Roman', 12))
        self.entry_firstname = Entry(self.frame_firstname)
        self.label_firstname.pack(padx=5, side='left')
        self.entry_firstname.pack(padx=8, side='left')
        self.frame_firstname.pack(anchor='w', pady=10)

        # Frame for student's last name
        self.frame_lastname = Frame(self.window)
        self.label_lastname = Label(self.frame_lastname, text='Last name',
                                    font=('Times New Roman', 12))
        self.entry_lastname = Entry(self.frame_lastname)
        self.label_lastname.pack(padx=5, side='left')
        self.entry_lastname.pack(padx=9, side='left')
        self.frame_lastname.pack(anchor='w', pady=10)

        # Frame for student's score
        self.frame_score = Frame(self.window)
        self.label_score = Label(self.frame_score, text='Score', font=('Times New Roman', 12))
        self.entry_score = Entry(self.frame_score)
        self.label_score.pack(padx=5, side='left')
        self.entry_score.pack(padx=35, side='left')
        self.frame_score.pack(anchor='w', pady=10)

        # Frame for save button
        self.frame_button = Frame(self.window)
        self.button_save = Button(self.frame_button, text='SAVE',
                                  font=('Times New Roman', 12), command=self.save)
        self.button_save.pack()
        self.frame_button.pack(pady=10)

        # Frame for view and close buttons
        self.frame_view_close = Frame(self.window)
        self.button_view = Button(self.frame_view_close, text="VIEW",
                                  font=('Times New Roman', 12), command=self.view)
        self.button_close = Button(self.frame_view_close, text="CLOSE",
                                   font=('Times New Roman', 12),
                                   command=self.window.destroy)
        self.button_view.pack(padx=25, pady=0, side='left')
        self.button_close.pack(padx=15, pady=0, side='left')
        self.frame_view_close.pack(anchor='e', pady=10)

    def save(self):
        """
        Method to be called when save button is clicked by a user. It takes values from ID, first name, last name,
        and score entries and assign them to variables. Also, this method opens the file to check whether the student's
        ID exists inside the file or not, if not then it opens the file for writing and writes ID, first name,
        last name, score, and calls a function to calculate grade and write them to the file.
        """
        student_id = str(self.entry_ID.get())
        if len(student_id) < 2 or len(student_id) > 2:
            tkinter.messagebox.showerror('Error', 'Student ID must be length be 2')

        try:
            if student_id.isnumeric():
                found = False
                with open('records.csv', 'r', newline='') as input_file:
                    csv_reader = csv.DictReader(input_file)
                    csv_reader = csv.DictReader(input_file)
                    for line in csv_reader:
                        if str(student_id) in line['Student ID']:
                            tkinter.messagebox.showerror('Error', 'Student ID already exist')
                            found = True
                            self.entry_ID.delete(0, END)

                if found == False:
                    if len(student_id) == 2:
                        first_name = str(self.entry_firstname.get()).strip()
                        if first_name.isnumeric():
                            tkinter.messagebox.showerror('Error', 'First name cannot be a numeric value')
                            self.entry_firstname.delete(0, END)
                        else:
                            last_name = str(self.entry_lastname.get()).strip()
                            if last_name.isnumeric():
                                tkinter.messagebox.showerror('Error', 'Last name cannot be a numeric value')
                                self.entry_lastname.delete(0, END)
                            else:
                                score = self.entry_score.get()
                                try:
                                    score = float(score)
                                    if score < 0 or score > 100:
                                        tkinter.messagebox.showerror('Error',
                                                                     'Score cannot be less than 0 or greater than 100')
                                        self.entry_score.delete(0, END)
                                    else:
                                        grade = assign_grade(score)
                                        data = dict()
                                        data['Student ID'] = student_id
                                        data['First Name'] = first_name
                                        data['Last Name'] = last_name
                                        data['Score'] = score
                                        data['Grade'] = grade
                                        with open('records.csv', 'a', newline='') as out_file:
                                            field_names = ['Student ID', 'First Name', 'Last Name', 'Score', 'Grade']
                                            csv_writer = csv.DictWriter(out_file, fieldnames=field_names)
                                            csv_writer.writerow(data)

                                        self.entry_ID.delete(0, END)
                                        self.entry_firstname.delete(0, END)
                                        self.entry_lastname.delete(0, END)
                                        self.entry_score.delete(0, END)

                                except ValueError:
                                    tkinter.messagebox.showerror('Error', 'Score must be a numeric value')
                                    self.entry_score.delete(0, END)
            else:
                raise ValueError('Student ID must be 2 numeric value')

        except ValueError as e:
            tkinter.messagebox.showerror('Error', e)
            self.entry_ID.delete(0, END)

    def view(self):
        """
        Method to be called when view button is clicked by a user. This method creates a new window using tkinter
        library and passes it as an instance to a new class named VIEW.
        """
        window = Toplevel()
        window.title('Final Project')
        window.geometry('330x350')
        window.resizable(False, False)
        widgets = VIEW(window)
        window.mainloop()
