class Person:
    def __init__(self, personalInfo, preferences):
        # dictionaries with person information
        self.mPersonalInfo = personalInfo
        self.mPreferences = []
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

    def __str__(self) -> str:
        # return str(self.mPersonalInfo) + str(self.mPreferences)
        return str(self.mPersonalInfo["name"]) + " - " + str(self.mPersonalInfo["ordertime"])
    def __repr__(self):
        return str(self)
    def __lt__(self, other):
        return self.mPersonalInfo["ordertime"] < other.mPersonalInfo["ordertime"]