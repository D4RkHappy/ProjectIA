from core import load_model_gpu, listen, findword, speak, clean_llm_answer
from chifoumi import chifoumi

if __name__ == '__main__':
    llm = load_model_gpu()
    init_prompt = """
    Tu es un assistant de conversation et tu dois répondre aux demandes de l'utilisateur en français avec des réponses 
    courtes et précises. Réponds uniquement en français aux prochaines questions !
    """
    test = llm(init_prompt)
    # print(test)
    print("initialisation OK")
    speak("Je suis prête !")

    text = ""
    while text != "stop":
        text = listen(True)

        # A CHANGER
        if findword("chifoumi")(text) is not None or findword("pierre-feuille-ciseaux")(text) is not None or findword(
                "Pierre feuille papier ciseau")(text) is not None:
            chifoumi()

        else:
            model_prompt: str = "Question: " + text + " ?"

            response: str = llm(model_prompt, max_tokens=64)
            print("LLAMA respond : " + response)

            answer = clean_llm_answer(response)
            print(answer)

            speak(answer)
