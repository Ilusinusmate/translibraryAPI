import openai
import json

#NOT IMPLEMENTED

# Este código não é utilizado na aplicação pois não é gratuito
# Entretanto seria uma forma mais eficiente e precisa de traduzir


# Esse código necessita de uma chave paga da OpenAI
# Para o código rodar precisa preencher com alguma chave válida.
CHAVE = ""

def translate(text, language):
    try:
        answer = openai.Completion.create(
            api_key=CHAVE,
            model="davinci",
            prompt= f"Translate the following text to {language}\n\\n{text}",
            max_tokens=round(len(text)*1.5)
        )

        data = answer.json()

        if "choices" in data:
            return data["choices"][0]["message"]["content"]

        return None

    except openai.error.OpenAIError as error:
        print("OpenAI API Error:", error)
        return None

    except Exception as e:
        print("An error occurred:", e)
        return e
        
if __name__ == "__main__":
    print(translate("Hey, that's my first test", "portuguese"))
    #  Para teste.