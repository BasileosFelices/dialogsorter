from ExcelReader import *

import configparser

class Sorter:
    def __init__(self):
        self.mTest = "AhoJ svete"
        self.mConfigInfo = configparser.ConfigParser()
        self.mConfigInfo.read("config.ini")
        
        if not self.testConfigFile(self.mConfigInfo):
            raise ImportError("Invalid config.ini file.")

        self.mExReader = ExcelReader(self.mConfigInfo)

    def testConfigFile(self, config):
        if "data" not in config:
            return False
        if "excel header" not in config:
            return False
        return True