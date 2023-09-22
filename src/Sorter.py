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
        # print(self.mPeople)
    def readActivities(self):
        slotNum = 0
        for slot in self.mExReader.readPerson(1).mPreferences:
            for activity in slot:
                self.mActivities.append( Activity.Activity(activity, slotNum, self.mConfigInfo["capacity"]) )
            slotNum += 1
        print("="*7 + "LOCATED ACTIVITIES"+"="*7)
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
            # print(person)
            slotNumber = 0
            for slot in person.mPreferences:
                slotNumber += 1
                foundActivity = False
                for preference in slot:
                    try:
                        activityIndex = self.mActivities.index(Activity.Activity(preference, slotNumber))
                        if self.mActivities[activityIndex].addPerson(person) is True:
                            person.writeActivity( {slotNumber: preference} )
                            foundActivity = True
                            break
                    # except mActivities.index fails to locate the activity
                    except ValueError as identifier:
                        print(identifier)
                        print("! Activity '", preference, "' not located!!")
                        print("Preference is ignored!!!")
                if foundActivity is False:
                    print("!!", person, "has no allocated activity in slot", slotNumber)
            # print(person.mActivities)
    def printActivityAttendance(self):
        print("="*7 + "ACTIVITY ATTENDANCE"+"="*7)
        for activity in self.mActivities:
            print("\n" + activity.mName)
            print("---------")
            for person in activity.mApplicants:
                print(person)

    
