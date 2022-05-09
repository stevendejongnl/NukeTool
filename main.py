import PySimpleGUI as Gui

layout = [[Gui.Button('Nuke everything!!!', size=(30, 4))]]

window = Gui.Window('Nuke Tool', layout, size=(620, 420))

event, values = window.read()
