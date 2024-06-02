import tkinter as tk

class PageOne(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Page One")
        self.label.pack()

        self.next_button = tk.Button(self, text="Next Page", command=self.master.show_page_two)
        self.next_button.pack()

class PageTwo(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Page Two")
        self.label.pack()

        self.prev_button = tk.Button(self, text="Previous Page", command=self.master.show_page_one)
        self.prev_button.pack()



class CustomTkinterApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Multi-page Tkinter App")
        self.geometry("300x200")
        self.page_one = PageOne(self)
        self.page_two = PageTwo(self)
        self.show_page_one()

    def show_page_one(self):
        self.page_one.pack()
        self.page_two.pack_forget()

    def show_page_two(self):
        self.page_one.pack_forget()
        self.page_two.pack()


if __name__ == "__main__":
    app = CustomTkinterApp()
    app.mainloop()

