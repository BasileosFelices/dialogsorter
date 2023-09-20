import ExcelReader
import Person
import TextModeler
import Activity

import configparser

class Sorter:
    def __init__(self):
        self.mTest = "AhoJ svete"
        self.mConfigInfo = configparser.ConfigParser()
        self.mConfigInfo.read("config.ini")
        self.mPeople = []
        self.mActivities = []
        
        if not self.testConfigFile(self.mConfigInfo):
            raise ImportError("Invalid config.ini file.")

        self.mExReader = ExcelReader.ExcelReader(self.mConfigInfo)

    def run(self):
        self.readPeople()
        self.readActivities()
        self.sortPeoplePriority()
        self.asignAskers()

    def readPeople(self):
        while True:
            newPerson = self.mExReader.readPerson()
            if bool(newPerson) is False:
                break
            # print(newPerson)
            self.mPeople.append(newPerson)
        print(self.mPeople)
    def readActivities(self):
        slotNum = 0
        for slot in self.mExReader.readPerson(1).mPreferences:
            for activity in slot:
                self.mActivities.append( Activity.Activity(activity, slotNum, self.mConfigInfo["capacity"]) )
            slotNum += 1
        for act in self.mActivities:
            print(act)

    def sortPeoplePriority(self):
        self.mPeople.sort()

    def testConfigFile(self, config):
        if "data" not in config:
            return False
        if "person" not in config:
            return False
        if "slot" not in config:
            return False
        if "priority" not in config:
            return False
        return True
    
    def asignAskers(self):
        print("="*7 + "ASIGNPROCESS"+"="*7)
        for person in self.mPeople:
            print(person)
    
