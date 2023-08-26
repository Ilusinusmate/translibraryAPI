import apertium

# NOT IMPLEMENTED

# Biblioteca deixou de receber suporte


def translate(text:str, targetLanguage:str, usedLanguage:str="en"):
    targetLanguage = targetLanguage.lower()
    try:
        return apertium.translation.translate(lang1=usedLanguage, lang2=targetLanguage, text=text)
        
    except Exception as error:
        print("An error has ocurred", error)
        return error

if __name__ == "__main__":
    print(translate("Hey, that's my first test", "es"))
    #  Para teste.