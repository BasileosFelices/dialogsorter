import configparser


class Activity:
    def __init__(self, name:str, slotNum:int, capacityConfig):
        self.mName = name
        self.mSlot = slotNum
        if name in capacityConfig:
            self.mCapacity = capacityConfig[name]
        else:
            print("BEWARE! Capacity information for '" + name +"' not located in config")
            
            try:
                self.mCapacity = int(input("Please input the desired capacity:\n"))
            except:
    def __str__(self) -> str:
        # return self.mName
        return "(ACT" + str(self.mSlot) + ": " + self.mName + " -> " + self.mCapacity + ")" 