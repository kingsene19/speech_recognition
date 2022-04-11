import operator
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
from tkinter import *
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import requests
from PIL import ImageTk, Image
import sys


user = ""


print('Chargement de votre assistante virtuelle - Jappsi')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', 'voices[0].id')


def Jappsi_voix(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    global user
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        Jappsi_voix("Bonjour utilisateur, quel est votre nom?")
        print("Bonjour utilisateur, quel est votre nom?")
    elif hour >= 12 and hour < 18:
        Jappsi_voix("Bon après midi utilisateur,quel est votre nom?")
        print("Bon après midi utilisateur, quel est votre nom?")
    else:
        Jappsi_voix("Bonsoir utilisateur, quel est votre nom?")
        print("Bonsoir utilisateur, quel est votre nom?")
    user = ecouter().capitalize()
    Jappsi_voix("Bienvenue " + user)


def get_operator_fn(op):
    return {
        '+': operator.add,
        '-': operator.sub,
        'x': operator.mul,
        'divisé': operator.__truediv__,
        'diviser': operator.__truediv__,
        'modulo': operator.mod,
        'Modulo': operator.mod,
    }[op]


def eval_binary_expr(op1, oper, op2):
    op1, op2 = int(op1), int(op2)
    return get_operator_fn(oper)(op1, op2)


def ecouter(ask=False):
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        if ask:
            Jappsi_voix(ask)
        r.adjust_for_ambient_noise(source=source)
        r.energy_threshold = 150
        audio = r.listen(source)
        commande = ""
        try:
            commande = r.recognize_google(audio, language='fr-FR')
            print("{} a dit {}".format(user, commande))
        except Exception:
            print("Je n'ai pas bien saisi, veuillez repeter")
            Jappsi_voix("Je n'ai pas bien saisi, veuillez répéter")
    return commande


def repondre(statement):

    if "changer utilisateur" in statement:
        global user
        Jappsi_voix("Quel est votre nom?")
        print("Quel est votre nom?")
        user = ecouter().capitalize()
        Jappsi_voix("Bienvenue "+user)

    if "au revoir" in statement or "ok bye" in statement or "stop" in statement:
        Jappsi_voix(
            'Votre assistant personnel Jappsi se met en veille, au revoir')
        print('Votre assistant personnel Jappsi se met en veille, au revoir')
        exit()

    if 'wikipedia' in statement:
        Jappsi_voix('Recherche Wikipedia...')
        statement = statement.replace("wikipedia", "")
        results = wikipedia.summary(statement, sentences=3)
        Jappsi_voix("D'apres wikipedia")
        Jappsi_voix(results)
        Jappsi_voix(results)

    if "calculer" in statement:
        Jappsi_voix(eval_binary_expr(*(statement.split()[1:])))

    elif 'youtube' in statement:
        webbrowser.open_new_tab("https://www.youtube.com")
        Jappsi_voix("Youtube est ouvert")
        time.sleep(3)

    elif 'google' in statement:
        webbrowser.open_new_tab("https://www.google.com")
        Jappsi_voix("Google chrome est ouvert maintenant")
        time.sleep(3)

    elif 'gmail' in statement:
        webbrowser.open_new_tab("gmail.com")
        Jappsi_voix("Google Mail est ouvert")
        time.sleep(3)

    elif "météo" in statement:
        api_key = "8ef61edcf1c576d65d836254e11ea420"
        base_url = "https://api.openweathermap.org/data/2.5/weather?"
        Jappsi_voix("Quelle est le nom de la ville")
        city_name = ecouter()
        complete_url = base_url+"appid="+api_key+"&q="+city_name
        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"]
            current_humidiy = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            Jappsi_voix(" Temperature en degre Kelvin est " +
                        str(current_temperature) +
                        "\n l'humidité en pourcentage est " +
                        str(current_humidiy) +
                        "\n description  " +
                        str(weather_description))
            print(" Temperature en degre Kelvin =" +
                  str(current_temperature) +
                  "\n l'humidité en pourcentage = " +
                  str(current_humidiy) +
                  "\n description = " +
                  str(weather_description))

        else:
            Jappsi_voix(" Ville non trouve ")

    elif 'heure' in statement:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        Jappsi_voix(f"L'Heure est {strTime}")

    elif 'qui es-tu' in statement:
        Jappsi_voix('Je suis Jappsi votre assistant personnel. Je suis programmé pour des tâches mineures comme '
                    "ouverture de youtube,effectuer des calculs simples donner les nouvelles en ouvrant seneweb, google chrome, gmail, prédire l'heure, prendre une photo, rechercher wikipedia, prédire la météo"
                    'dans différentes villes et vous pouvez également me poser des questions informatiques ou géographiques!')

    elif "camera" in statement or "prendre une photo" in statement:
        ec.capture(0, "robo camera", "img.jpg")

    elif 'rechercher' in statement:
        statement = statement.replace("rechercher", "")
        webbrowser.open_new_tab(statement)
        time.sleep(3)

    elif 'nouvelle' in statement:
        news = webbrowser.open_new_tab("https://www.seneweb.com/")
        Jappsi_voix('Voici les gros titres de Seneweb,bonne lecture')
        time.sleep(3)

    elif 'demander' in statement:
        Jappsi_voix(
            'Je peux répondre à des questions informatiques et géographiques et quelle question voulez-vous poser maintenant')
        question = ecouter()
        app_id = "R2K75H-7ELALHR35X"
        client = wolframalpha.Client('R2K75H-7ELALHR35X')
        res = client.query(question)
        answer = next(res.results).text
        Jappsi_voix(answer)
        print(answer)

    elif "eteindre la machine" in statement:
        Jappsi_voix(
            "Ok , votre pc s'eteindra dans 10 sec, soyez sûr de fermer toutes les applications")
        subprocess.call(["shutdown", "/l"])

    else:
        Jappsi_voix("Veuillez répéter")


class Widget:

    def __init__(self):
        root = Tk()
        root.title('Jappsi')
        root.geometry('840x520')

        img = ImageTk.PhotoImage(Image.open(
            r"C:/Users/Massamba Sene/Documents/GIT/DIC1/Projets/speech_recognition/Originalite-PersonalVoiceAssistant-Rama/stockphoto.jpg"))
        panel = Label(root, image=img)
        panel.pack(side="right", fill="both", expand="no")

        toolbar = LabelFrame(root, text="Jappsi")
        toolbar.pack(fill="both", expand="yes")
        text = Text(toolbar, wrap="word")
        text.pack(side="top", fill="both", expand="yes")
        text.tag_configure("stderr", foreground="#b22222")

        sys.stdout = TextRedirector(text, "stdout")
        sys.stderr = TextRedirector(text, "stderr")

        btn = Button(root, text="Parler", font=(
            "railways", 10, "bold"), bg="red", fg="white", command=self.clicked)
        btn.pack(fill="x", expand="no")
        btn2 = Button(root, text="Fermer", font=("railways", 10, "bold"), bg="yellow",
                      fg="black", command=root.destroy)
        btn2.pack(fill="x", expand="no")

        Jappsi_voix("Chargement de votre assistante virtuelle - Jappsi")
        wishMe()

        root.mainloop()

    def clicked(self):
        print("Working...")
        Jappsi_voix("Comment puis-je vous aider?")
        print("Comment puis-je vous aider?")
        commande = ecouter().lower()
        print(commande)
        repondre(commande)


class TextRedirector(object):
    def __init__(self, widget, tag="stdout"):
        self.widget = widget
        self.tag = tag

    def write(self, str):
        self.widget.configure(state="normal")
        self.widget.insert("end", str, (self.tag,))
        self.widget.configure(state="disabled")


if __name__ == '__main__':
    widget = Widget()

time.sleep(1)
