#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk
import pygubu
import team
import re
import json
from match import Match
from tkinter import filedialog
from tkinter import *


class Application:
    def __init__(self, master):

        self.master = master
        self.teams = {}
        self.json_string = ''

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

        # Dialog
        self.dialog = builder.get_object('dialog_add_teams', master)

        # Text box

        def callback(event):
            text = self.text_box_input.get("1.0", tk.END).replace('\n', ' ')
            # print(text)
            if text == 'Enter results here in format: Team1 - Team2	X : X ':
                self.text_box_input.delete("1.0", tk.END)

        self.text_box_input = self.builder.get_object('text', self.master)
        self.text_box_input.bind("<Button-1>", callback)

        callbacks = {
            'on_calculate': self.on_calculate,
            'on_open': self.on_open,
            'show_dialog': self.show_dialog
        }

        builder.connect_callbacks(self)

    def show_dialog(self):
        self.mainwindow.update()
        # self.center_dialog()
        # self.center_dialog_desktop()
        # show dialog
        self.dialog.run()
        self.load_data()


    def on_calculate(self):
        playing = re.compile("^([A-Za-zčćžđšČĆŽŠĐ ()]+ - [A-Za-zčćžđšČĆŽŠĐ ()]+)")
        result = re.compile("^([0-9]+ : [0-9]+)")


        text = self.text_box_input.get("1.0", tk.END).split('\n')
        text = list(filter(None, text))

        home = ''
        guest = ''
        ghome = ''
        gguest = ''
        data = {}

        for line in text:
            print(line.encode('cp1250', 'ignore').decode('cp1250', 'ignore'))
            if playing.match(line):
                home, guest = line.split(' - ')
            elif result.match(line):
                ghome, gguest = line.split(' : ')
                self.teams = Match(home, guest, ghome, gguest, self.teams).play()
                # print(self.teams[home].to_JSON())
                # print(self.teams[guest].to_JSON())
                data[self.teams[home].name] = self.teams[home].to_JSON()
                data[self.teams[guest].name] = self.teams[guest].to_JSON()

        self.json_string = str(data).replace('\'', '\"').replace('\"{', '{').replace('}\"', '}')
        # print(data['Pešćenica'])


    def on_open(self):
        file = filedialog.askopenfilename(filetypes=(("JSON Files", "*.json"),))
        if file:
            try:
                with open(file) as data_file:
                    bam = json.load(data_file)

                print(bam)
            except:  # <- naked except is a bad idea
                tk.showerror("Open Source File", "Failed to read file\n'%s'" % file)
            return
        return

    def on_save(self):
        file = filedialog.asksaveasfile(mode='w', defaultextension=".json")
        if file is None:
            return
        else:
            file.write(self.json_string)
            file.close()
        return


if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    root.mainloop()