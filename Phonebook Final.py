import tkinter as tk                
from tkinter import font as tkfont  

white = "#ffffff" #white 
black = "#000000" #black 
seafoam = "#3EA99F" #seafoam


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Login, Application, Registration):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Login")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class Login(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg=white)
        
        Title = tk.Label(self, text="Login", font=('Verdana 17 bold'), height = 1, width=20, anchor='nw', bg=seafoam, fg=white)
        Title.pack(side="top", fill="x", pady=10)

        t_name = tk.Label(self, text="Name", width=5, height=1, font=('Ivy 10'), bg=white, anchor='nw')
        t_name.place(x=10, y=50)
        e_name = tk.Entry(self, width=25, justify='left', highlightthickness=1, relief="solid")
        e_name.place(x=80, y=50)
        
        l_password = tk.Label(self, text="Password *", height=1, font=('Ivy 10'), bg=white, anchor='nw')
        l_password.place(x=10, y=110)
        e_password = tk.Entry(self, width=25, justify='left', highlightthickness=1, relief="solid", show = "*")
        e_password.place(x=80, y=110)

        button1 = tk.Button(self, text="Login",
                             command=lambda: controller.show_frame("Application"), bg=seafoam, fg=white, font=('Ivy 10'))
        button1.place(x=10, y=170)

        button2 = tk.Button(self, text="Register here",
                           command=lambda: controller.show_frame("Registration"), bg=seafoam, fg=white, font=('Ivy 10'), relief='ridge')
        button2.place(x=350, y=15)


class Application(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 1", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("Login"))
        button.pack()


class Registration(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg=white)
        
        Title = tk.Label(self, text="Registration", font=('Verdana 17 bold'), height = 1, width=20, anchor='nw', bg=seafoam, fg=white)
        Title.pack(side="top", fill="x", pady=10)
        
        l_name = tk.Label(self, text="Userame *", width=20, height=1, font=('Ivy 10'), bg=white, anchor='nw')
        l_name.place(x=10, y=50)
        e_name = tk.Entry(self, width=25, justify='left', highlightthickness=1, relief="solid")
        e_name.place(x=150, y=50)

        l_telephone = tk.Label(self, text="Telephone *", width=20, height=1, font=('Ivy 10'), bg=white, anchor='nw')
        l_telephone.place(x=10, y=110)
        e_telephone = tk.Entry(self, width=25, justify='left', highlightthickness=1, relief="solid")
        e_telephone.place(x=150, y=110)

        l_email = tk.Label(self, text="Email *", height=1, font=('Ivy 10'), bg=white, anchor='nw')
        l_email.place(x=10, y=170)
        e_email = tk.Entry(self, width=25, justify='left', highlightthickness=1, relief="solid")
        e_email.place(x=150, y=170)

        l_password = tk.Label(self, text="Password *", height=1, font=('Ivy 10'), bg=white, anchor='nw')
        l_password.place(x=10, y=230)
        e_password = tk.Entry(self, width=25, justify='left', highlightthickness=1, relief="solid", show = "*")
        e_password.place(x=150, y=230)

        l_cpassword = tk.Label(self, text="Re-enter Password *", height=1, font=('Ivy 10'), bg=white, anchor='nw')
        l_cpassword.place(x=10, y=290)
        e_cpassword = tk.Entry(self, width=25, justify='left', highlightthickness=1, relief="solid", show = "*")
        e_cpassword.place(x=150, y=290)

        b_register = tk.Button(self, text="Login",
                             command=lambda: controller.show_frame("Application"), bg=seafoam, fg=white, font=('Ivy 10'))
        b_register.place(x=10, y=350)

        button2 = tk.Button(self, text="Login here",
                           command=lambda: controller.show_frame("Login"), bg=seafoam, fg=white, font=('Ivy 10'), relief='ridge')
        button2.place(x=350, y=15)


if __name__ == "__main__":
    app = SampleApp()
    app.geometry('485x450')
    app.resizable(width='false', height='false')
    app.mainloop()