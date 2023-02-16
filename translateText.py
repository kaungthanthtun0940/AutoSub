from googletrans import Translator

translator = Translator()

def getTranslateText(text,input_lang,output_lang):
    translation = translator.translate(text, dest=output_lang,src=input_lang)

    print(translation.text)

    return translation.text
