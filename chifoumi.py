import random

import re

from core import listen
from core import speak
from core import findword


def chifoumi():
    speak("Très bien ! Jouons ! Combiens de parties voulez-vous jouer ?")
    tmpround = ""
    while isinstance(tmpround, str):
        tmpround = listen(True)
        try:
            tmpround = re.search(r'\d+', tmpround).group()
            tmpround = int(tmpround)
        except ValueError:
            speak("Ce n'est pas un nombre valide, réessaye")
        except AttributeError:
            speak("Ce n'est pas un nombre valide, réessaye")
    speak("Super ! On va jouer " + str(tmpround) + " parties !")
    currentround = 0
    scoreuser = 0
    scoreoppo = 0
    while currentround < tmpround:
        speak("Prépare toi ! Pierre feuille")
        opponentplay = random.randint(1, 3)  # 1 = pierre, 2 = feuille, 3 = ciseau
        userplay = ""
        goodplay = False
        while not goodplay:
            userplay = listen(False)
            # if findword("pierre")(userplay) is not None or findword("feuille")(userplay) is not None or findword("ciseaux")(userplay) is not None:
            if userplay == "pierre" or userplay == "feuille" or userplay == "ciseaux":
                goodplay = True
            else:
                print("Recommence. Tu as dis :" + userplay)
                speak("Recommence. Tu as dis :" + userplay)

        # Pierre
        if opponentplay == 1:
            speak("J'ai joué pierre !")
            if userplay == "pierre":
                print(str(scoreuser) + " - " + str(scoreoppo))
                speak("Egalité, on recommence !")
            if userplay == "feuille":
                speak("Mince ! J'ai perdu ! Un point pour toi.")
                currentround = currentround + 1
                scoreuser = scoreuser + 1
                print(str(scoreuser) + " - " + str(scoreoppo))
                speak("Le score est de " + str(scoreuser) + "pour toi contre " + str(scoreoppo) + "pour moi !")
            if userplay == "ciseaux":
                speak("J'ai gagné ! Un point pour moi")
                currentround = currentround + 1
                scoreoppo = scoreoppo + 1
                print(str(scoreuser) + " - " + str(scoreoppo))
                speak("Le score est de " + str(scoreuser) + "pour toi contre " + str(scoreoppo) + "pour moi !")

        # Feuille
        if opponentplay == 2:
            speak("J'ai joué feuille !")
            if userplay == "pierre":
                speak("J'ai gagné ! Un point pour moi")
                currentround = currentround + 1
                scoreoppo = scoreoppo + 1
                print(str(scoreuser) + " - " + str(scoreoppo))
                speak("Le score est de " + str(scoreuser) + "pour toi contre " + str(scoreoppo) + "pour moi !")
            if userplay == "feuille":
                print(str(scoreuser) + " - " + str(scoreoppo))
                speak("Egalité, on recommence !")
            if userplay == "ciseaux":
                speak("Mince ! J'ai perdu ! Un point pour toi.")
                currentround = currentround + 1
                scoreuser = scoreuser + 1
                print(str(scoreuser) + " - " + str(scoreoppo))
                speak("Le score est de " + str(scoreuser) + "pour toi contre " + str(scoreoppo) + "pour moi !")

        # Ciseaux
        if opponentplay == 3:
            speak("J'ai joué ciseaux !")
            if userplay == "pierre":
                speak("Mince ! J'ai perdu ! Un point pour toi.")
                currentround = currentround + 1
                scoreuser = scoreuser + 1
                print(str(scoreuser) + " - " + str(scoreoppo))
                speak("Le score est de " + str(scoreuser) + "pour toi contre " + str(scoreoppo) + "pour moi !")
            if userplay == "feuille":
                speak("J'ai gagné ! Un point pour moi")
                currentround = currentround + 1
                scoreoppo = scoreoppo + 1
                print(str(scoreuser) + " - " + str(scoreoppo))
                speak("Le score est de " + str(scoreuser) + "pour toi contre " + str(scoreoppo) + "pour moi !")
            if userplay == "ciseaux":
                print(str(scoreuser) + " - " + str(scoreoppo))
                speak("Egalité, on recommence !")

    if scoreuser > scoreoppo:
        speak("Bravo ! Tu as gagné")
    if scoreuser == scoreoppo:
        speak("Mince ! Egalité parfaite !")
    if scoreuser < scoreoppo:
        speak("J'ai gagné ! Bouh ! Tu es nul !")
