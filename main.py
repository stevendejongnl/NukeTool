import PySimpleGUI as Gui

from settings import WindowSettings
from layouts import Start

layout = Start().init

window = Gui.Window(WindowSettings.title, layout, size=(WindowSettings.width, WindowSettings.height))

event, values = window.read()
