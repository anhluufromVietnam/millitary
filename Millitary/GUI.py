from cProfile import label
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from turtle import update
import Database

class GUI:
    def __init__(self, root, account):
        self.window = root
        self.window.title("Military Equipment Mangement Application")
        self.window.geometry("1000x700")
        self.window.grid()
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        # This variable to open different accounts
        self.account = account
        
        # Variable
        self.item = StringVar()
        self.type = StringVar()
        self.date = StringVar()        
        self.position = StringVar()
        self.status = StringVar()

        self.frame_left = Frame(self.window, bg="#DAE5D0")
        self.frame_left.place(x=0, y=0, width=242, height=700, relwidth=1, relheight=1)

        self.frame_right = Frame(self.window, bg="#FEFBE7")
        self.frame_right.place(x=242, y=0, relwidth=1, relheight=1)

        # Button in the left frame
        self.save_equipment = Button(self.frame_left, text="Save Equipment", highlightthickness=0, bg="#A0BCC2", command=self.save_data,bd=0).place(x=33, y=464, width=175, height=36)
        self.update_equipment = Button(self.frame_left, text="Update Equipment", highlightthickness=0, bg="#A0BCC2", command=self.update_data,bd=0).place(x=33, y=520, width=175, height=36)
        self.delete_equipment = Button(self.frame_left, text="Delete Equipment", highlightthickness=0, bg="#A0BCC2", command=self.delete_data,bd=0).place(x=33, y=577, width=175, height=36)
        self.reset_equipment = Button(self.frame_left, text="Reset", highlightthickness=0, bg="#A0BCC2",command=self.delete_all_data,bd=0).place(x=33, y=400, width=175, height=36)
        Button(self.frame_left, text="Logouts", highlightthickness=0, bg="#db6060",command=self.logout,bd=0).place(x=33, y=633, width=175, height=36)


        # Button in the right frame
        
        #This variable to choose what kind of search do you want to use
        self.type_of_search = StringVar()
        self.search = StringVar()
        
        self.search_equipment = Button(self.frame_right, text="Search", highlightthickness=0, bg="#db6060",fg="#000000", command=self.search_data,bd=0).place(x=80, y=76, width=70, height=30)
        Button(self.frame_right, text="Show all", highlightthickness=0, bg="#A0BCC2", command=self.display_data,bd=0).place(x=80, y=110, width=70, height=20)
        self.search_equipment_text = Entry(self.frame_right, font=('arial', 12, 'bold'), width=404, justify=LEFT, textvariable=self.search).place(x=270, y=76, width=411, height=30)

        self.search_choose = ttk.Combobox(self.frame_right, width=39, font=('Century Gothic', 12), state='readonly', textvariable=self.type_of_search)
        self.search_choose['values'] = ('Item', 'Type', 'Date','Option', 'Status')
        self.search_choose.current(0)
        self.search_choose.place(x=159, y=76, width=100, height=30)


        # Middle Frame that contain input information of the newspaper
        self.mid_frame = Frame(self.frame_right, bg="#C4C4C4")
        self.mid_frame.place(x=80, y=138, width=599, height=203)

        # Widget for the middle frame
        Label(self.frame_right, text="Military Equipment Mangement Application", highlightthickness=0, font=('Century Gothic', 20)).place(x=180, y=23)
        self.item_equipment = Label(self.mid_frame, text="Item", highlightthickness=0, bg="#A0BCC2").place(x=15, y=15, width=121, height=21)
        self.type_equipment = Label(self.mid_frame, text="Type", highlightthickness=0, bg="#A0BCC2").place(x=15, y=55, width=121, height=21)
        self.date_equipment = Label(self.mid_frame, text="Date: ", highlightthickness=0, bg="#A0BCC2").place(x=15, y=95, width=121, height=21)
        self.position_equipment = Label(self.mid_frame, text="Position: ", highlightthickness=0, bg="#A0BCC2").place(x=15, y=175, width=121, height=21)
        self.status_equipment = Label(self.mid_frame, text="Status: ", highlightthickness=0, bg="#A0BCC2").place(x=15, y=135, width=121, height=21)

        # Entry for the middle frame
        self.item_text = Entry(self.mid_frame, font=('arial', 12, 'bold'), width=404, justify=LEFT, textvariable=self.item)
        self.item_text.place(x=159, y=15, width=400, height=21)

        self.type_text = Entry(self.mid_frame, font=('arial', 12, 'bold'),  width=404, justify=LEFT, textvariable=self.type)
        self.type_text.place(x=159, y=55, width=400, height=21)

        self.date_text = Entry(self.mid_frame, font=('arial', 12, 'bold'), width=404, justify=LEFT, textvariable=self.date)
        self.date_text.place(x=159, y=95, width=400, height=21)

        #self.status_text = Entry(self.mid_frame, font=('arial', 12, 'bold'), width=404, justify=LEFT).place(x=159, y=135, width=400, height=21)
        self.status_choose = ttk.Combobox(self.mid_frame, width=39, font=('Century Gothic', 12), state='readonly', textvariable=self.status)
        self.status_choose['values'] = ('Available',
                                        'Unavailable')
        self.status_choose.current()
        self.status_choose.place(x=159, y=135, width=400, height=25)
        self.position_text = Entry(self.mid_frame, font=('arial', 12, 'bold'), width=404, justify=LEFT, textvariable=self.position)
        self.position_text.place(x=159, y=175, width=400, height=21)

        # Bottom Frame that list information of the newspaper
        self.bottom_frame = Frame(self.frame_right, bg="#A0BCC2")
        self.bottom_frame.place(x=80, y=351, width=599, height=301)

        # -------------------------------Treeview-------------------------------
        scroll_x = Scrollbar(self.bottom_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(self.bottom_frame, orient=VERTICAL)

        columns = ('ID', 'item', 'type', 'date', 'status', 'position')
        self.equipment_list = ttk.Treeview(self.bottom_frame, height=12,
                                           columns=columns,
                                           xscrollcommand=scroll_x.set,
                                           yscrollcommand=scroll_y.set,)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.equipment_list.heading('ID', text='ID')
        self.equipment_list.heading('item', text='Item')
        self.equipment_list.heading('type', text='Type')
        self.equipment_list.heading('date', text='Date')
        self.equipment_list.heading('status', text='Status')
        self.equipment_list.heading('position', text='Position')


        self.equipment_list['show'] = 'headings'

        self.equipment_list.column('ID', width=20)
        self.equipment_list.column('item', width=70)
        self.equipment_list.column('type', width=70)
        self.equipment_list.column('date', width=70)
        self.equipment_list.column('status', width=70)
        self.equipment_list.column('position', width=70)

        self.equipment_list.pack(fill=BOTH, expand=1)

        self.equipment_list.bind('<ButtonRelease-1>', self.clicker)
        self.display_data()

        self.choose_row()

    def save_data(self):
        if self.item.get() == "" or self.type.get() == "" or self.status.get() == "" or self.position.get() == "":
            tkinter.messagebox.askokcancel(title='Invalid',
                                           message='Please enter valid data')
        else:
            try:
                Database.add(self.account,
                             self.item.get(),
                             self.type.get(),
                             self.date.get(),
                             self.status.get(),
                             self.position.get())
                self.display_data()
                tkinter.messagebox.showinfo(title='Message',
                                            message='Sucessful')
                self.item_text.delete(0, END)
                self.type_text.delete(0, END)
                self.date_text.delete(0, END)
                self.position_text.delete(0, END)
            except Exception as es:
                tkinter.messagebox.showerror(title='ERROR',
                                             message=f'Because {str(es)}')

    def display_data(self):
        """Display all data by fetch data"""
        data = Database.display(account=self.account)
        if len(data) >= 0:
            self.equipment_list.delete(*self.equipment_list.get_children())
            for i in data:
                self.equipment_list.insert("", END, value=i)

    def choose_row(self):
        """Choose a row and return values into entries"""
        self.item_text.delete(0, END)
        self.type_text.delete(0, END)
        self.date_text.delete(0, END)
        self.position_text.delete(0, END)
        # Choose a value of a row
        choose_row = self.equipment_list.focus()
        # Grab the value of the chosen row
        self.data = self.equipment_list.item(choose_row, 'value')
        try:
            self.id = self.data[0]
            self.item.set(self.data[1])
            self.type.set(self.data[2])
            self.date.set(self.data[3])
            self.status.set(self.data[4])
            self.position.set(self.data[5])
        except:
            pass

    def clicker(self, event):
        """Click handler when you click into a row"""
        self.choose_row()

    def update_data(self):
        if self.item.get() == "" or self.type.get() == "" or self.status.get() == "" or self.position.get() == "":
            tkinter.messagebox.askretrycancel(title='ERROR', message='Please choose a data')
        else:
            try:
                answer = tkinter.messagebox.askyesno("Are you sure?", "Do you want to update information?")
                if answer:
                    Database.update(self.account,
                                    self.id,
                                    self.item.get(),
                                    self.type.get(),
                                    self.date.get(),
                                    self.status.get(), 
                                    self.position.get())
                else:
                    if not update:
                        return
                self.display_data()
            except Exception as e:
                tkinter.messagebox.showerror("ERROR", f"Because of {str(e)}")

        # Fill in empty into the entries
        self.item_text.delete(0, END)
        self.type_text.delete(0, END)
        self.date_text.delete(0, END)
        self.position_text.delete(0, END)
        
    def delete_data(self):
        if not self.equipment_list.selection():
            tkinter.messagebox.showwarning("ERROR", "Please choose a data you want to delete")
        else:
            answer = tkinter.messagebox.askyesno("Warning", "Do you really want to delete this?")
            if answer:
                Database.delete(self.account, self.id)
                self.display_data()
                self.item_text.delete(0, END)
                self.type_text.delete(0, END)
                self.date_text.delete(0, END)
                self.position_text.delete(0, END)
                tkinter.messagebox.showinfo("Delete", "You deleted the data")
            
    def delete_all_data(self):
        """A function to delete all data and drop table"""
        answer = tkinter.messagebox.askyesno("Warning", "Do You really want to delete all data!")
        if answer:
            Database.delete_all(self.account)
            self.display_data()
            # Fill in empty into the entries
            self.item_text.delete(0, END)
            self.type_text.delete(0, END)
            self.date_text.delete(0, END)
            self.position_text.delete(0, END)

    def logout(self):
        self.window.destroy()

    def on_closing(self):
        quit() 

    def search_data(self):
        if self.type_of_search == "Option" or self.search == "":
            tkinter.messagebox.showwarning("Opps", "Please choose the attribute?")
        else:
            try:
                data = Database.search(self.account, self.type_of_search.get(), self.search.get())
                if len(data) >= 0:
                    self.equipment_list.delete(*self.equipment_list.get_children())
                    for i in data:
                        self.equipment_list.insert("", END, value=i)
            except:
                tkinter.messagebox.showwarning("Warning", "Please choose the attribute?")
