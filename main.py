# Project start: 19 Dec, 2020
# Create Config.py with API keys to use

import config

import wolframalpha
client = wolframalpha.Client(config.wfapi_key)

import wikipedia

import PySimpleGUI as sg
sg.theme('dark blue')
layout =[[sg.Text('On standby'), sg.InputText()],[sg.Button('Send Command'),sg.Button('Cancel')]]
window = sg.Window('Elis Bot', layout)

import pyttsx3
engine = pyttsx3.init()

while True:
    event, values = window.read()
    if event in (None, 'Cancel'):
        break
    try:
        wiki_res = wikipedia.summary(values[0], sentences=2)
        wolfram_res = next(client.query(values[0]).results).text
        engine.say(wolfram_res)
        sg.PopupNonBlocking("Wolfram Result: "+wolfram_res,"Wikipedia Result: "+wiki_res)
    except wikipedia.exceptions.DisambiguationError:
        wolfram_res = next(client.query(values[0]).results).text
        engine.say(wolfram_res)
        sg.PopupNonBlocking(wolfram_res)
    except wikipedia.exceptions.PageError:
        wolfram_res = next(client.query(values[0]).results).text
        engine.say(wolfram_res)
        sg.PopupNonBlocking(wolfram_res)
    except:
        wiki_res = wikipedia.summary(values[0], sentences=2)
        engine.say(wiki_res)
        sg.PopupNonBlocking(wiki_res)

    engine.runAndWait()

    print (values[0])

window.close()
