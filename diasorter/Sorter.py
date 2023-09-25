from ExcelPrinter import ExcelPrinter
from ExcelReader import ExcelReader
from Person import Person
from TextModeler import TextModeler
from Activity import Activity

import configparser as cp


class Sorter:
    """Main script class, runs everything

    The app is basicly run from here.

    Attributes:
        mConfigInfo: read configparser file, handles almost all user input
        mPeople: People loaded into memory
        mActivities: Activities people sort into
        mExcelReader: helper class for loading people and activities
        mExcelPrinter: helper class for outputting the result
    """

    def __init__(self) -> None:
        """Constructs Sorter, loads config file and starts mExcelReader

        Raises:
            ImportError: Config is tested for having all compulsory attributes
        """
        self.mConfigInfo = cp.ConfigParser()
        self.mConfigInfo.read("config.ini")
        self.mPeople = []
        self.mActivities = []

        if not self.testConfigFile(self.mConfigInfo):
            raise ImportError(
                "Invalid config.ini file. Please make sure all compulsory parameters are specified."
            )

        self.mExReader = ExcelReader(self.mConfigInfo)

    def run(self) -> None:
        """Main function of the script, runs everything in the desired order"""
        self.readPeople()
        self.readActivities()
        self.sortPeoplePriority()
        self.asignAskers()

        self.mExPrinter = ExcelPrinter(self.mConfigInfo)

        self.mExPrinter.outputPeopleSheet(self.mPeople)
        self.mExPrinter.outputActivitySheets(self.mActivities)
        self.mExPrinter.saveFile()

        return

    def readPeople(self) -> None:
        """Commands loading people into memory, uses ExcelReader, saves its outout into mPeople"""
        while True:
            newPerson = self.mExReader.readPerson()
            if bool(newPerson) is False:
                break
            # print(newPerson)
            self.mPeople.append(newPerson)
        # print(self.mPeople)
        return

    def readActivities(self) -> None:
        """Reads activities from the first person in source files

        We expect first person will mention all possible activities in their preferences. There are warnings later
        if that is not the case.

        Prints the located activities with their loaded capacities, if capacity loading fails, input is required.
        See Activity constructor for more info.
        """

        slotNum = 0
        for slot in self.mExReader.readPerson(1).mPreferences:
            for activity in slot:
                self.mActivities.append(
                    Activity(activity, slotNum, self.mConfigInfo["capacity"])
                )
            slotNum += 1
        print("=" * 7 + "LOCATED ACTIVITIES" + "=" * 7)
        for act in self.mActivities:
            print(act)
        return

    def sortPeoplePriority(self) -> None:
        """Sorts people into order defined by priority.

        Order is determined in Person class with __lt__. See there for more details.
        """
        self.mPeople.sort()
        return

    def testConfigFile(self, config: cp.ConfigParser) -> bool:
        """Checks the given configfile has all compulsory parameters

        Todo:
            return or raise exception specifiing where the test failed

        Args:
            config (cp.ConfigParser): configparses file

        Returns:
            bool: True if everything is in order, False otherwise
        """
        if "data" not in config:
            return False
        if "person" not in config:
            return False
        if "slot" not in config:
            return False
        if "priority" not in config:
            return False
        if "output" not in config:
            return False
        if "capacity" not in config:
            return False
        if config.has_option("data", "filename") is False:
            return False
        if config.has_option("person", "name") is False:
            return False
        if config.has_option("priority", "orderby") is False:
            return False
        if config.has_option("output", "peoplesheetname") is False:
            return False
        if config.has_option("person", config["priority"]["orderby"]) is False:
            return False
        return True

    def asignAskers(self) -> None:
        """Assigns mPeople to mActivities

        Main Sorter process. Tries to asign people to activities based on their preferences.
        However, places are limited by the capacities of said activities. Who comes first (in mPeople),
        loots the best spots first.

        In the end Activities have people inside and people have activities name inside them.

        Be sure to check output log as warnigns are only printed here when no valid activity is asigned to someone
        or activity in preference is not found at all (a deeper problem in data is propable cause).
        """
        print("=" * 7 + "ASIGNPROCESS" + "=" * 7)
        for person in self.mPeople:
            slotNumber = 0
            for slot in person.mPreferences:
                slotNumber += 1
                foundActivity = False
                for preference in slot:
                    try:
                        activityIndex = self.mActivities.index(
                            Activity(preference, slotNumber)
                        )
                        if self.mActivities[activityIndex].addPerson(person) is True:
                            person.writeActivity({slotNumber: preference})
                            foundActivity = True
                            break
                    # except mActivities.index fails to locate the activity
                    except ValueError as identifier:
                        print(identifier)
                        print("! Activity '", preference, "' not located!!")
                        print("Preference is ignored!!!")
                if foundActivity is False:
                    print("!!", person, "has no allocated activity in slot", slotNumber)
        return

    def printActivityAttendance(self) -> None:
        "Debug printing functions, prints attendance lists to console"
        print("=" * 7 + "ACTIVITY ATTENDANCE" + "=" * 7)
        for activity in self.mActivities:
            print("\n" + activity.mName + "(" + str(len(activity.mApplicants)) + ")")
            print("---------")
            for person in activity.mApplicants:
                print(person)
        return
