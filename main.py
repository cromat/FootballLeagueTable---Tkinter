import tkinter as tk
import pygubu
import team
import re
import json
from match import Match


class Application:
    def __init__(self, master):

        self.master = master
        self.teams = {}

        # Loading teams from file with points and stuff...

        team_names = ['Vatrogasac', 'Jasenovac', 'Podovi', 'Metalac', 'Sunjski', 'Lokomotiva', 'Sloga', 'Dinamo (O)',
                      'Stari Grad', 'Una-Mladost', 'Pešćenica', 'Zeleni Brijeg', 'Slavonac', 'Croatia']

        for name in team_names:
            tm = team.Team(1, name)
            self.teams[name] = tm

        #1: Create a builder
        self.builder = builder = pygubu.Builder()

        #2: Load an ui file
        builder.add_from_file('bla.ui')

        #3: Create the widget using a master as parent
        self.mainwindow = builder.get_object('main', master)


        callbacks = {
            'on_calculate': self.on_calculate,
            'on_open': self.on_open,
        }

        builder.connect_callbacks(self)


        # self.btn_calc = builder.get_object('calc')

    def on_calculate(self):
        playing = re.compile("^([A-Za-zčćžđšČĆŽŠĐ ()]+ - [A-Za-zčćžđšČĆŽŠĐ ()]+)")
        result = re.compile("^([0-9]+ : [0-9]+)")


        text = self.builder.get_object('text', self.master).get("1.0", tk.END).split('\n')
        text = list(filter(None, text))

        home = ''
        guest = ''
        ghome = ''
        gguest = ''

        for line in text:
            if playing.match(line):
                home, guest = line.split(' - ')
            elif result.match(line):
                ghome, gguest = line.split(' : ')
                self.teams = Match(home, guest, ghome, gguest, self.teams).play()
                print(self.teams[home])
                print(self.teams[guest])

                with open('data.txt', 'a') as outfile:
                    json.dump(self.teams[home].__dict__, outfile)
                    json.dump(self.teams[guest].__dict__, outfile)

    def on_open(self):
        return

if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    root.mainloop()