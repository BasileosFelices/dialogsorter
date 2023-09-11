from openpyxl import Workbook, load_workbook
from openpyxl.utils import get_column_letter
import datetime
import configparser

class TextModeler:
    def __new__(cls):
        raise TypeError("TextModeler is a static class used for holding functions for string editing. It cannot be instanced")
    
    @staticmethod
    def cleanSpaces(string):
        return " ".join(string.split())
    
    # @staticmethod
    # def readTime(string):
        
    #     date = str(string.split(" ")[0])
    #     year = date.split("-")[0]
    #     month = date.split("-")[1]
    #     day = date.split("-")[2]

    #     clock = string.split(" ")[1]
    #     hour = time.split(":")[0]
    #     minute = time.split(":")[1]
    #     second = time.split(":")[2]

    #     formatTime = time.struct_time(year, month, day, hour, minute, second)

    #     return time.mktime(formatTime)

class Person:
    def __init__(self, name, email, schoolclass, time, preferences):
        self.mName = name
        self.mEmail = email
        self.mSchoolClass = schoolclass
        self.mTime = time
        self.mPreferences = preferences
    def __str__(self):
        return " ".join([self.mName, self.mEmail, self.mSchoolClass, str(self.mTime), str(self.mPreferences)])

class Sorter:
    def __init__(self):
        self.mTest = "AhoJ svete"
        pass

class ExcelReader:
    header = {}
    def __init__(self, configinfo):
        self.mHeaderIsRead = False
        self.mConfigForExcelRead = configinfo
    def readHeader(source):
        pass

pers1 = Person("Petr", "pavpetr@fit.cvut.cz", "8.a", datetime.datetime(2022, 6, 23), ["Anna", "Zuzka", "Alzbeta"])

print(pers1.mPreferences)
print(pers1)

excelsource = load_workbook("dialog_data.xlsx")
ws = excelsource.active
print(ws["C3"].value)
print(type(ws["C3"].value))