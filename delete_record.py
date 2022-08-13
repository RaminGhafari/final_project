from assign_grade import *
import tkinter.messagebox
from tkinter import *
import csv


class DELETE:
    """
    Class representing a window -- delete a student's record window for deleting a student's records from the file.
    """
    def __init__(self, window):
        """
        Constructor to create initial state of delete window; for example, creating frames, labels, and entries for
        student ID, first name, last name, score, and grade. Also, creating frames and labels for delete and close
        buttons.
        :param window: A window that already uses tkinter library
        """
        self.window = window

        # Frame for student's ID
        self.frame_ID = Frame(self.window)
        self.label_ID = Label(self.frame_ID, text='Enter student ID', font=('Times New Roman', 12))
        self.entry_ID = Entry(self.frame_ID)
        self.label_ID.pack(padx=5, side='left')
        self.entry_ID.pack(padx=5, side='left')
        self.frame_ID.pack(anchor='w', pady=10)

        # Frame for search button
        self.frame_search = Frame(self.window)
        self.button_search = Button(self.frame_search, text='Search', font=('Times New Roman', 12),
                                  command=self.search)
        self.button_search.pack()
        self.frame_search.pack(pady=5)

        # Frame for student's first name
        self.frame_first = Frame(self.window)
        self.label_first = Label(self.frame_first, text='First Name', font=('Times New Roman', 12))
        self.entry_first = Entry(self.frame_first, state=DISABLED, font=('Times New Roman', 12))
        self.label_first.pack(padx=5, side='left')
        self.entry_first.pack(padx=5, side='left')
        self.frame_first.pack(anchor='w', pady=5)

        # Frame for student's last name
        self.frame_last = Frame(self.window)
        self.label_last = Label(self.frame_last, text='Last Name', font=('Times New Roman', 12))
        self.entry_last = Entry(self.frame_last, state=DISABLED, font=('Times New Roman', 12))
        self.label_last.pack(padx=5, side='left')
        self.entry_last.pack(padx=5, side='left')
        self.frame_last.pack(anchor='w', pady=5)

        # Frame for student's score
        self.frame_score = Frame(self.window)
        self.label_score = Label(self.frame_score, text='Score', font=('Times New Roman', 12))
        self.entry_score = Entry(self.frame_score, state=DISABLED, font=('Times New Roman', 12))
        self.label_score.pack(padx=5, side='left')
        self.entry_score.pack(padx=35, side='left')
        self.frame_score.pack(anchor='w', pady=5)

        # Frame for student's grade
        self.frame_grade = Frame(self.window)
        self.label_grade = Label(self.frame_grade, text='Grade', font=('Times New Roman', 12))
        self.entry_grade = Entry(self.frame_grade, state=DISABLED, font=('Times New Roman', 12))
        self.label_grade.pack(padx=5, side='left')
        self.entry_grade.pack(padx=33, side='left')
        self.frame_grade.pack(anchor='w', pady=5)

        # Frame for delete button
        self.frame_delete = Frame(self.window)
        self.button_delete = Button(self.frame_delete, text="DELETE",
                                  state=DISABLED, font=('Times New Roman', 12), command=self.delete)
        self.button_delete.pack()
        self.frame_delete.pack()

        # Frame for close button
        self.frame_close = Frame(self.window)
        self.button_close = Button(self.frame_close, text="CLOSE", font=('Times New Roman', 12),
                                   command=self.window.destroy)
        self.button_close.pack(padx=20, pady=0, side='left')
        self.frame_close.pack(anchor='e', pady=5)

    def search(self):
        """
        Method to be called when user clicks on the search button. This method first disables all the entries for
        student's ID, first name, last name, score, and grade, then it takes the student's ID and searches for
        the record of the student inside the file. Then, if it exists, it shows all the student's information such as
        first name, last name, score, and grade inside entries that are disabled.
        """
        self.button_delete.config(state=DISABLED)
        self.entry_first.config(state=NORMAL)
        self.entry_first.delete(0, END)
        self.entry_first.config(state=DISABLED)
        self.entry_last.config(state=NORMAL)
        self.entry_last.delete(0, END)
        self.entry_last.config(state=DISABLED)
        self.entry_score.config(state=NORMAL)
        self.entry_score.delete(0, END)
        self.entry_score.config(state=DISABLED)
        self.entry_grade.config(state=NORMAL)
        self.entry_grade.delete(0, END)
        self.entry_grade.config(state=DISABLED)

        student_id = self.entry_ID.get()
        if len(student_id) < 2 or len(student_id) > 2:
            tkinter.messagebox.showerror('Error', 'Student ID must be length be 2')
        try:
            if student_id.isnumeric():
                if len(student_id) == 2:
                    found = False
                    with open('records.csv', 'r', newline='') as input_file:
                        csv_reader = csv.DictReader(input_file)
                        csv_reader = csv.DictReader(input_file)
                        for line in csv_reader:
                            if str(student_id) in line['Student ID']:
                                self.button_delete.config(state=NORMAL)
                                self.entry_first.config(state=NORMAL)
                                self.entry_first.delete(0, END)
                                self.entry_first.insert(0, line['First Name'])
                                self.entry_first.config(state=DISABLED)
                                self.entry_last.config(state=NORMAL)
                                self.entry_last.delete(0, END)
                                self.entry_last.insert(0, line['Last Name'])
                                self.entry_last.config(state=DISABLED)
                                self.entry_score.config(state=NORMAL)
                                self.entry_score.delete(0, END)
                                self.entry_score.insert(0, line['Score'])
                                self.entry_score.config(state=DISABLED)
                                self.entry_grade.config(state=NORMAL)
                                self.entry_grade.delete(0, END)
                                self.entry_grade.insert(0, line['Grade'])
                                self.entry_grade.config(state=DISABLED)
                                found = True
                        if found == False:
                            tkinter.messagebox.showinfo('Exist', f'Student with ID#{student_id} does not exist')
                            self.entry_ID.delete(0, END)

            else:
                raise ValueError('Student ID must be 2 numeric value')

        except ValueError as e:
            tkinter.messagebox.showerror('Error', e)
            self.entry_ID.delete(0, END)

    def delete(self):
        """
        Method to be called when a user clicks on the delete button. This method opens the csv file that contents
        students information for reading to check if the student exists or not, then if the student exists, it opens
        the file for writing and deletes that student's information from the file.
        """
        first_name = self.entry_first.get()
        last_name = self.entry_last.get()
        response = tkinter.messagebox.askyesno('Delete', f"Do you want to delete {first_name} {last_name}'s records?")
        if response == 1:
            student_id = self.entry_ID.get()
            file = open('records.csv')
            reader = csv.reader(file)

            my_list = []
            found = False
            for row in reader:
                if row[0] == str(student_id):
                    found = True
                else:
                    my_list.append(row)
            file.close()

            file = open('records.csv', 'w', newline='')
            writer = csv.writer(file)
            writer.writerows(my_list)
            file.seek(0)

            self.entry_ID.delete(0, END)
            self.entry_first.config(state=NORMAL)
            self.entry_first.delete(0, END)

            self.entry_first.config(state=DISABLED)
            self.entry_last.config(state=NORMAL)
            self.entry_last.delete(0, END)

            self.entry_last.config(state=DISABLED)
            self.entry_score.config(state=NORMAL)
            self.entry_score.delete(0, END)

            self.entry_score.config(state=DISABLED)
            self.entry_grade.config(state=NORMAL)
            self.entry_grade.delete(0, END)

            self.entry_grade.config(state=DISABLED)
            self.button_delete.config(state=DISABLED)
            tkinter.messagebox.showinfo('Confirmation', f"{first_name} {last_name}'s records deleted")
            file.close()

