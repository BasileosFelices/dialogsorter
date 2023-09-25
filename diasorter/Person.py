class Person:
    """Person class for holding information regarding one person

    Attributes:
        mPersonalInfo: dict {property : value} of personal information regarding the person
        mPreferences: preferences for activities in order of timeslots
        mActivities: asigned activities, dictionary with {slotnumber: name of activity - str}
        mPriority (str): name of personal info property used for comparison and sorting
    """

    mPersonalInfo = dict()
    mPreferences = list()
    mActivities = dict()
    mPriority = str()

    def __init__(self, personalInfo: list, preferences: list, priorityTag: str) -> None:
        """Construction of Person

        Preferences are passed in crude form gotten from the excel file. Constructor crunches them into a prettier form.
        List of lists of preferences per slot.

        Args:
            personalInfo (list): personal information {property:value}
            preferences (list): preferences for activities in order of timeslots
            priorityTag (str): ame of personal info property used for comparison and sorting
        """
        self.mPersonalInfo = personalInfo
        self.mPreferences = []
        self.mActivities = {}
        self.mPriority = priorityTag

        slotNum = 0
        for slot in preferences.values():
            self.mPreferences.append([])
            for activity in slot.split(";"):
                if activity == "":
                    continue
                self.mPreferences[slotNum].append(activity)
            slotNum += 1

    def writeActivity(self, activity: dict) -> None:
        """Adds an asigned slot and activity information to person

        Args:
            activity (dict): { slotnumber (int) : activityName }
        """
        self.mActivities.update(activity)

    def __str__(self) -> str:
        """debugprinting setting of Person class

        Returns:
            str: name and parameter used for sorting
        """
        # return str(self.mPersonalInfo) + str(self.mPreferences)
        return (
            str(self.mPersonalInfo["name"])
            + " - "
            + str(self.mPersonalInfo[self.mPriority])
        )

    def __repr__(self) -> str:
        """basicly __str__ but more broad, works for printing lists of persons and so on"""
        return str(self)

    def __lt__(self, other) -> bool:
        """Sorting specification, uses mPriority

        Returns:
            _type_: True if less, False otherwise
        """
        return self.mPersonalInfo[self.mPriority] < other.mPersonalInfo[self.mPriority]

    def outputHeaderInfo(self) -> list:
        """Generates list of headers based on personal information and number of slots.

        Number of slots is derived from number of preferences instead of asigned activities.
        The reasoning is a person used for header output may not necceserily be asigned in all slots.

        Returns:
            list: list of strings for header, order corresponds to outputPersonalInfo()
        """
        headerInfo = []
        # header stats with personal info
        for personinfoheader in self.mPersonalInfo.keys():
            headerInfo.append(personinfoheader)
        # follows slot headers
        for i in range(len(self.mPreferences)):
            headerInfo.append("Slot " + str(i + 1))
        return headerInfo

    def outputPersonalInfo(self) -> list:
        """Generates a list of personal data coresponding to headers from .outputHeaderInfo()

        Returns:
            list: list of strings with all given personal info
        """
        datalist = []
        for data in self.mPersonalInfo.values():
            datalist.append(data)
        return datalist

    def outputAsignedSlots(self) -> list:
        """Generates a list of asigned activities, lists "NOTASIGNED" if slot is not asigned

        Number of slots is derived from number of preferences instead of asigned activities.
        The reasoning is a person used for header output may not necceserily be asigned in all slots.

        Returns:
            list: list of strings with activities name in order
        """
        slotinfo = []
        # +1 as slots are one-indexed
        for slotNumber in range(1, len(self.mPreferences) + 1):
            slotinfo.append(self.mActivities.get(slotNumber, "NOT ASIGNED"))
        return slotinfo
