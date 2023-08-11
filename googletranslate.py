import requests
import asyncio

def translate(text: str, targetLanguage: str, sourceLanguage: str = "auto"):

    # """
    # Função para traduzir um texto para um idioma alvo usando a API do Google Translate.
    # Args:
    #     text (str): O texto a ser traduzido.
    #     targetLanguage (str): O idioma alvo para a tradução.
    #     usedLanguage (str, optional): O idioma usado para identificar o idioma do texto de origem. Padrão é "auto".

    # Returns:
    #     str: O texto traduzido.
    # """

    if targetLanguage == "en" or targetLanguage == "english":
        return text

    targetLanguage = targetLanguage.lower()

    url = "https://translate.googleapis.com/translate_a/single"
    params = {
        "client": "gtx",
        "sl": sourceLanguage,
        "tl": targetLanguage,
        "dt": "t",
        "q": text
    }

    try:
        response = requests.get(url, params=params)
        response_data = response.json()
        translation = response_data[0][0][0] if response_data and len(response_data[0][0][0]) > 0 else ""
        return translation

    except Exception as error:
        print("An error has occurred", error)
        return error

async def async_translate(text, targetLanguage, sourceLanguage):
    return await asyncio.to_thread(translate, text, targetLanguage, sourceLanguage)
    # """
    # Função assíncrona para traduzir um texto para um idioma alvo usando a função de tradução.
    # Args:
    #     text (str): O texto a ser traduzido.
    #     target_language (str): O idioma alvo para a tradução.
    #     source_language (str): O idioma de origem do texto.

    # Returns:
    #     str: O texto traduzido.
    # """

if __name__ == "__main__":
    print(translate("Hy, that's my test", "pt-br"))
    # PARA TESTES