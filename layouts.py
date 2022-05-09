from dataclasses import dataclass

import PySimpleGUI as Gui


@dataclass(frozen=True)
class Start:
    init = [[Gui.Button('Nuke everything!!!', size=(30, 4))]]
