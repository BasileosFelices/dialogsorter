class TextModeler:
    def __new__(cls):
        raise TypeError("TextModeler is a static class used for holding functions for string editing. It cannot be instanced")
    
    @staticmethod
    def cleanSpaces(string):
        return " ".join(string.split())