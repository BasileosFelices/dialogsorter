class Person:
    def __init__(self, personalInfo, preferences, priorityTag):
        # dictionaries with person information
        self.mPersonalInfo = personalInfo
        self.mPreferences = []
        self.mActivities = {}
        self.mPriority = priorityTag
        # processing preferences
        slotNum = 0
        for slot in preferences.values():
            self.mPreferences.append([])
            for activity in slot.split(';'):
                if activity == "":
                    continue
                self.mPreferences[slotNum].append(activity)
            slotNum += 1
        # print(self.mPreferences)

    def writeActivity(self, activity):
        self.mActivities.update( activity )

    def __str__(self) -> str:
        return str(self.mPersonalInfo["name"])
        # return str(self.mPersonalInfo) + str(self.mPreferences)
        return str(self.mPersonalInfo["name"]) + " - " + str(self.mPersonalInfo[self.mPriority])
    def __repr__(self):
        return str(self)
    def __lt__(self, other):
        return self.mPersonalInfo[self.mPriority] < other.mPersonalInfo[self.mPriority]
    
    def outputHeaderInfo(self) -> list:
        headerInfo = []
        # header stats with personal info
        for personinfoheader in self.mPersonalInfo.keys():
            headerInfo.append(personinfoheader)
        # follows assingned activities
        for i in range(len(self.mActivities)):
            headerInfo.append( "Slot " + str(i + 1) )
        return headerInfo
    def outputPersonalInfo(self) -> list:
        datalist = []
        for data in self.mPersonalInfo.values():
            datalist.append(data)
        return datalist