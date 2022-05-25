from inquirer.themes import *


class Glitter(Theme):
    def __init__(self):
        super().__init__()
        self.Question.mark_color = term.aquamarine
        self.Question.brackets_color = term.lightsteelblue3
        self.Question.default_color = term.lightsteelblue3
        self.Checkbox.selection_color = term.black
        self.Checkbox.selection_icon = "-"
        self.Checkbox.selected_color = term.white
        self.Checkbox.selected_icon = '-'
        self.Checkbox.unselected_color = term.lightsteelblue3
        self.Checkbox.unselected_icon = "-"
        self.List.selection_color = term.aquamarine
        self.List.selection_cursor = ">"
        self.List.unselected_color = term.lightsteelblue3
