import configparser as cp

from Person import Person


class Activity:
    """Activity class for holding a lecture information as well as attendance list

    Attributes:
        mName (str): required attribute, used for searching, activities with same name are considered eq
        mSlot (int): slot number the activity belongs to
        mCapacity (int): maximum number or attendants
        mApplicants (list): list of people asigned to the activity
    """

    mName = str()
    mSlot = int()
    mCapacity = int()
    mApplicants = list()

    def __init__(
        self, name: str, slotNum: int, capacityConfig: cp.ConfigParser = None
    ) -> None:
        """constructs an Activity, without passing capacityconfig, the capacity is set to 0

        This behaviour is mainly for creating temporary activities used only for searching or sorting.

        When capacity is not located in config file, user is asked to input the capacity manually. Until integer is 
        inputed, the program refuses to advance.

        Args:
            name (str): Required parameter, used for searching, activities with same name are considered eq
            slotNum (int): slot number the activity belongs to
            capacityConfig (cp.ConfigParser, optional): configfile with view of ["capacity"], for loading capacity. Defaults to None.
        """

        self.mName = name
        self.mSlot = slotNum
        self.mApplicants = []
        if bool(capacityConfig) is False:
            self.mCapacity = 0
            return
        if name in capacityConfig:
            self.mCapacity = capacityConfig.getint(name)
        else:
            print(
                "BEWARE! Capacity information for '" + name + "' not located in config"
            )

            inputvalid = False
            while not inputvalid:
                try:
                    self.mCapacity = int(input("Please input the desired capacity:\n"))
                    if self.mCapacity < 0: raise ValueError("Capacity cannot be negative")
                except ValueError as valueer:
                    print(valueer)
                    print("Invalid input, please try again.")
                except:
                    print("Invalid input, please try again.")
                else:
                    inputvalid = True

    def __str__(self) -> str:
        """debug printing settings for activity class

        Returns:
            str: slot, name and capacity information
        """

        return (
            "(ACT"
            + str(self.mSlot)
            + ": "
            + self.mName
            + " -> "
            + str(self.mCapacity)
            + ")"
        )

    def __eq__(self, other) -> bool:
        """compares equality of Activity based on name

        Returns:
            bool: True if equal names
        """

        return True if self.mName == other.mName else False

    def __lt__(self, other) -> bool:
        """compares two Activity based on name

        Returns:
            bool: True if name is less
        """

        return True if self.mName < other.mName else False

    def addPerson(self, person: Person) -> bool:
        """Adds a person to the attendance list if the capacity is not filled

        Args:
            person (Person): Person to be added to attendance list, Person class expected

        Returns:
            bool: True if applicant is written to list, False if the activity is full
        """
        if len(self.mApplicants) >= self.mCapacity:
            return False
        self.mApplicants.append(person)
        return True
