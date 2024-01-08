import fitz
from googletrans import Translator
from icecream import ic

def get_available_languages() -> dict:
    languages_dict = {
        'af': 'Afrikaans',
        'sq': 'Albanian',
        'am': 'Amharic',
        'ar': 'Arabic',
        'hy': 'Armenian',
        'az': 'Azerbaijani',
        'eu': 'Basque',
        'be': 'Belarusian',
        'bn': 'Bengali',
        'bs': 'Bosnian',
        'bg': 'Bulgarian',
        'ca': 'Catalan',
        'ceb': 'Cebuano',
        'ny': 'Chichewa',
        'zh-cn': 'Chinese (Simplified)',
        'co': 'Corsican',
        'hr': 'Croatian',
        'cs': 'Czech',
        'da': 'Danish',
        'nl': 'Dutch',
        'en': 'English',
        'eo': 'Esperanto',
        'et': 'Estonian',
        'tl': 'Filipino',
        'fi': 'Finnish',
        'fr': 'French',
        'fy': 'Frisian',
        'gl': 'Galician',
        'ka': 'Georgian',
        'de': 'German',
        'el': 'Greek',
        'gu': 'Gujarati',
        'ht': 'Haitian Creole',
        'ha': 'Hausa',
        'haw': 'Hawaiian',
        'iw': 'Hebrew',
        'hi': 'Hindi',
        'hmn': 'Hmong',
        'hu': 'Hungarian',
        'is': 'Icelandic',
        'ig': 'Igbo',
        'id': 'Indonesian',
        'ga': 'Irish',
        'it': 'Italian',
        'ja': 'Japanese',
        'jw': 'Javanese',
        'kn': 'Kannada',
        'kk': 'Kazakh',
        'km': 'Khmer',
        'ko': 'Korean',
        'ku': 'Kurdish (Kurmanji)',
        'ky': 'Kyrgyz',
        'lo': 'Lao',
        'la': 'Latin',
        'lv': 'Latvian',
        'lt': 'Lithuanian',
        'lb': 'Luxembourgish',
        'mk': 'Macedonian',
        'mg': 'Malagasy',
        'ms': 'Malay',
        'ml': 'Malayalam',
        'mt': 'Maltese',
        'mi': 'Maori',
        'mr': 'Marathi',
        'mn': 'Mongolian',
        'my': 'Burmese',
        'ne': 'Nepali',
        'no': 'Norwegian',
        'ps': 'Pashto',
        'fa': 'Persian',
        'pl': 'Polish',
        'pt': 'Portuguese',
        'pa': 'Punjabi',
        'ro': 'Romanian',
        'ru': 'Russian',
        'sm': 'Samoan',
        'gd': 'Scots Gaelic',
        'sr': 'Serbian',
        'st': 'Sesotho',
        'sn': 'Shona',
        'sd': 'Sindhi',
        'si': 'Sinhala',
        'sk': 'Slovak',
        'sl': 'Slovenian',
        'so': 'Somali',
        'es': 'Spanish',
        'su': 'Sundanese',
        'sw': 'Swahili',
        'sv': 'Swedish',
        'tg': 'Tajik',
        'ta': 'Tamil',
        'te': 'Telugu',
        'th': 'Thai',
        'tr': 'Turkish',
        'uk': 'Ukrainian',
        'ur': 'Urdu',
        'ug': 'Uyghur',
        'uz': 'Uzbek',
        'vi': 'Vietnamese',
        'cy': 'Welsh',
        'xh': 'Xhosa',
        'yi': 'Yiddish',
        'yo': 'Yoruba',
        'zu': 'Zulu'
    }

    return languages_dict
        

def translate_text(text: str, target_lang: str) -> str:
    try:
        translator = Translator()
        translated = translator.translate(text=text, src="auto", dest=target_lang)
        return translated.text

    except Exception as e:
        raise e
    
    
def translate_file(file_path: str, target_lang: str) -> str:
    try:
        
        if file_path.lower().endswith(".txt"):
            output_path = file_path.replace(".txt", f"_{target_lang}.txt")
            with open(file_path, "r", encoding="utf-8") as file:
                with open(output_path, "w", encoding="utf-8") as output_file:
                    translated_line = translate_text(file.read(),target_lang)
                    output_file.write(translated_line)

            print(f"Arquivo traduzido salvo em: {output_path}")
            return output_path

        elif file_path.lower().endswith(".pdf"):
            doc = fitz.open(file_path)
            output_path = file_path.replace(".pdf", f"_{target_lang}.pdf")

            for page_number in range(doc.page_count):
                page = doc.load_page(page_number)
                text = page.get_text("text")
                translated_text = translate_text(text, target_lang)

                # Adiciona texto traduzido a uma nova página
                new_page = doc.new_page(width=page.rect.width, height=page.rect.height)
                new_page.insert_text((10, 10), translated_text, fontsize=12)

            doc.save(output_path)
            doc.close()

            print(f"Arquivo traduzido salvo em: {output_path}")
            return output_path

        else:
            raise ValueError("Formato de arquivo não suportado. Apenas .txt e .pdf são permitidos.")

    except Exception as e:
        raise e
    
if __name__ == "__main__":
#   UNIT TESTS
    from icecream import ic
    ic(get_available_languages())
    ic(translate_text("Hi mom, my name is antony.\nIt's nice to see you here.", target_lang="pt"))