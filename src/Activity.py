import configparser
from email.errors import ObsoleteHeaderDefect
from types import NoneType


class Activity:
    def __init__(self, name:str, slotNum:int, capacityConfig = None):
        self.mName = name
        self.mSlot = slotNum
        self.mApplicants = []
        if bool(capacityConfig) is False:
            return
        if name in capacityConfig:
            self.mCapacity = capacityConfig.getint(name)
        else:
            print("BEWARE! Capacity information for '" + name +"' not located in config")
            
            inputvalid = False
            while not inputvalid:
                try:
                    self.mCapacity = int(input("Please input the desired capacity:\n"))
                except:
                    print("Invalid input, please try again.")
                else:
                    inputvalid = True
    def __str__(self) -> str:
        # return self.mName
        return "(ACT" + str(self.mSlot) + ": " + self.mName + " -> " + str(self.mCapacity) + ")" 
    
    def __eq__(self, other) -> bool:
        return True if self.mName == other.mName else False

    def addPerson(self, person) -> bool:
        if len(self.mApplicants) >= self.mCapacity:
            return False
        self.mApplicants.append(person)
        return True
        
        
