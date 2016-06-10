__author__ = 'Dr.S.Gowrishankar'

def greet(lang):
    if lang == 'es':
        return "Hola"
    elif lang == 'fr':
        return "Bonjour"
    else:
        return "Hello"

print greet("en"),'Glen'

print greet("es"),'Sally'

print greet("fr"),'Michael'
