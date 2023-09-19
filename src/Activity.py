class Activity:
    def __init__(self, name, slotNum):
        self.mName = name
        self.mSlot = slotNum
    def __str__(self) -> str:
        return "(ACT" + str(self.mSlot) + ": " + self.mName + ")" 