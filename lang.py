import googletrans

def getcode(s):
    for key,value in googletrans.LANGUAGES.items():
        if (s==value):
            return key

