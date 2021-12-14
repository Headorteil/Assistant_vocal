#! /usr/bin/env python3

"""
Install Pocketsphinx en français :
https://drive.google.com/file/d/0Bw_EqP-hnaFNN2FlQ21RdnVZSVE/view?resourcekey=0-CEkuW10BcLuDdDnKDbzO4w
"""

from datetime import datetime
from threading import Thread

import pyttsx3
import speech_recognition as sr
from rich.console import Console
from rich import bprint


engine = pyttsx3.init('espeak')
voices = engine.getProperty('voices')
engine.setProperty('voice', 'french')
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)
console = Console()

template = """[bold blue]User said : {}
[bold green]Threads : {}"""
last_said = ""
nbthreads = 0


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def handle_query(query):
    if "quel" in query and "eur" in query:
        a = datetime.now()
        hour = "une" if a.hour == 1 else a.hour
        today = f"Il est {hour} heures {a.minute}"
        speak(today)


def recognize(audio, status):
    global nbthreads
    global last_said
    nbthreads += 1
    status.update(template.format(last_said, nbthreads))
    try:
        query = reco.recognize_sphinx(audio, language="fr-FR")
        if query == "":
            nbthreads -= 1
            status.update(template.format(last_said, nbthreads))
            return
        last_said = query
        status.update(template.format(last_said, nbthreads))
        handle_query(query.lower())
    except Exception:
        pass

    nbthreads -= 1
    status.update(template.format(last_said, nbthreads))


def takeCommand(reco, source, status):
    audio = reco.listen(source)
    thread = Thread(target=recognize, args=(audio, status))
    thread.start()


if __name__ == '__main__':
    reco = sr.Recognizer()
    with sr.Microphone() as source:
        with console.status("[bold red]Ajusting noise ...") as status:
            reco.pause_threshold = 0.5
            reco.adjust_for_ambient_noise(source, duration=10)

        bprint("[bold red]Ajusting noise Ok")

        with console.status("[bold green]Running ...") as status:
            while True:
                takeCommand(reco, source, status)
                date = datetime.now().strftime("%H:%M:%S")
                console.bprint(f"[grey][{date}] [magenta]Switching")
