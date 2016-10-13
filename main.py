#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import tkinter as tk
from tkinter import *
from tkinter import filedialog
import pygubu
import team
from match import Match
import tkinter.messagebox as msgbox


class Application:
    def __init__(self, master):

        self.master = master
        self.teams = {}
        self.json_string = ''

        # Loading teams from file with points and stuff...

        # Vatrogasac, Jasenovac, Podovi, Metalac, Sunjski, Lokomotiva, Sloga, Dinamo (O),Stari Grad, Una-Mladost, Pešćenica, Zeleni Brijeg, Slavonac, Croatia

        #1: Create a builder
        self.builder = builder = pygubu.Builder()

        #2: Load an ui file
        builder.add_from_file('bla.ui')

        #3: Create the widget using a master as parent
        self.mainwindow = builder.get_object('main', master)

        # Dialog
        self.dialog = builder.get_object('dialog_add_teams', master)

        # Text box
        def callback_text_box_input(event):
            text = self.text_box_input.get("1.0", tk.END).replace('\n', ' ')
            # print(text)
            if text == 'Enter results here in format: Team1 - Team2	X : X ':
                self.text_box_input.delete("1.0", tk.END)

        # Text box add teams
        def callback_text_box_add_teams(event):
            text = self.text_box_add_teams.get("1.0", tk.END).replace('\n', ' ')
            # print(text)
            if text == 'Example: Team1, Team2, Team3 ':
                self.text_box_add_teams.delete("1.0", tk.END)

        # Init elements
        self.text_box_add_teams = self.builder.get_object('add_teams_txt', self.master)
        self.text_box_add_teams.bind("<Button-1>", callback_text_box_add_teams)

        self.text_box_input = self.builder.get_object('text', self.master)
        self.text_box_input.bind("<Button-1>", callback_text_box_input)

        self.table = self.builder.get_object('table', self.master)

        callbacks = {
            'on_calculate': self.on_calculate,
            'on_open': self.on_open,
            'on_save': self.on_save,
            'show_dialog': self.show_dialog,
            'on_add_teams': self.on_add_teams,
            'on_append': self.on_append
        }

        builder.connect_callbacks(self)

    def show_dialog(self):
        self.mainwindow.update()
        self.text_box_add_teams.delete("1.0", END)
        self.text_box_add_teams.insert("1.0", "Example: Team1, Team2, Team3")
        self.dialog.run()

    def populate_table(self):
        # sorted(statuses, key=lambda x: )
        s = sorted(self.teams, key=lambda x: (self.teams[x].points, self.teams[x].gdiff), reverse=True)
        i = 1
        self.table.delete(*self.table.get_children())
        for tm in s:
            self.table.insert('', 'end', text="1", values=(str(i), self.teams[tm].name,
                                                           str(self.teams[tm].won), str(self.teams[tm].draw),
                                                           str(self.teams[tm].draw), str(self.teams[tm].lost),
                                                           str(self.teams[tm].gscored) + " : " +
                                                           str(self.teams[tm].gconceded), str(self.teams[tm].gdiff),
                                                           str(self.teams[tm].points)))
            i += 1


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

                data[self.teams[home].name] = self.teams[home].to_JSON()
                data[self.teams[guest].name] = self.teams[guest].to_JSON()

        self.json_string = str(data).replace('\'', '\"').replace('\"{', '{').replace('}\"', '}')
        self.populate_table()

    def on_open(self):
        file = filedialog.askopenfilename(filetypes=(("JSON Files", "*.json"),))
        if file:
            try:
                with open(file) as data_file:
                    json_data = json.load(data_file)

                print(json_data)
                self.teams = {}
                for tm in json_data:
                    self.teams[tm] = team.Team(json_data[tm]['name'],
                                               int(json_data[tm]['played']), int(json_data[tm]['won']),
                                               int(json_data[tm]['draw']), int(json_data[tm]['lost']),
                                               int(json_data[tm]['gscored']), int(json_data[tm]['gconceded']),
                                               int(json_data[tm]['gdiff']), int(json_data[tm]['points']))

                print(self.teams)
                self.populate_table()
            except:  # <- naked except is a bad idea
                msgbox.showerror("Open Source File", "Failed to read file\n'%s'" % file)
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

    def on_add_teams(self):
        self.teams = {}
        text_add_teams = self.text_box_add_teams.get("1.0", tk.END).rstrip()
        text_add_teams = text_add_teams.replace(', ', ',')
        team_names = re.split(',', text_add_teams)
        print(team_names)
        for name in team_names:
            tm = team.Team(name)
            print(tm)
            self.teams[name] = tm

        self.text_box_add_teams.delete("1.0", END)
        return

    def on_append(self):
        text_add_teams = self.text_box_add_teams.get("1.0", tk.END).rstrip()
        text_add_teams = text_add_teams.replace(', ', ',')
        team_names = re.split(',', text_add_teams)
        for name in team_names:
            tm = team.Team(name)
            self.teams[name] = tm

        self.text_box_add_teams.delete("1.0", END)
        return


if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
