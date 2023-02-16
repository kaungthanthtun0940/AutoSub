from googletrans import LANGUAGES

switched_dict = {value: key for key, value in LANGUAGES.items()}

switched_dict['myanmar'] = 'my'
switched_dict['burmese'] = 'my'
switched_dict['kurdish'] = 'ku'
switched_dict['kurmanji'] = 'ku'
switched_dict['chinese'] = 'zh-tw'

def getLanguageData(lang):
    return switched_dict[lang]

keys_list = list(switched_dict.keys())

def getKeyList():
    return keys_list