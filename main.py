import tkinter as tk
import pygubu


class Application:
    def __init__(self, master):

        self.master = master

        #1: Create a builder
        self.builder = builder = pygubu.Builder()

        #2: Load an ui file
        builder.add_from_file('bla.ui')

        #3: Create the widget using a master as parent
        self.mainwindow = builder.get_object('main', master)

        callbacks = {
            'on_calculate': self.on_calculate,
        }

        builder.connect_callbacks(self)


        # self.btn_calc = builder.get_object('calc')

    def on_calculate(self):
        text = self.builder.get_object('text', self.master).get("1.0", tk.END)
        print(text)





if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    root.mainloop()