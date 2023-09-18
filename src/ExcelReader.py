from openpyxl import Workbook, load_workbook
from openpyxl.utils import get_column_letter

import configparser

class ExcelReader:
    header = {}
    def __init__(self, configinfo):
        # configfileread
        self.mHeaderIsRead = False
        self.mConfig = configinfo
        self.mConfigHeader = self.mConfig["excel header"]
        # excel file read 
        self.mExcelSource = load_workbook(self.mConfig["data"]["filename"])
        self.mExcelWorkSheet = self.mExcelSource.active
        # reading header definitions from config
        self.mHeaderDef = {}
        self.mHeaderDefReverse = {}
        for headerKey in self.mConfigHeader:
            self.mHeaderDef.update({headerKey : self.mConfigHeader.get(headerKey)})
            self.mHeaderDefReverse.update({self.mConfigHeader.get(headerKey) : headerKey})
        self.mHeaderCoord = {}

        self.readHeader()

        # for person reading
        self.mPersonReadCount = 0

    def readHeader(self):
        row = 1
        col = 0
        while True:
            col += 1
            coord = get_column_letter(col) + str(row)
            cellvalue = self.mExcelWorkSheet[coord].value
            
            # Stop at 'None' value - empty cell
            if not bool(cellvalue):
                break
            
            # print(cellvalue)
            if cellvalue in self.mHeaderDefReverse:
                print("LOCATED:", cellvalue, "as", self.mHeaderDefReverse[cellvalue])
                self.mHeaderCoord.update( {self.mHeaderDefReverse[cellvalue] : col} )
        # print(self.mHeaderCoord)
        for headerKey in self.mConfigHeader:
            if headerKey not in self.mHeaderCoord:
                print("Header:", headerKey, "not located!")
    def readPerson(self):
        pass