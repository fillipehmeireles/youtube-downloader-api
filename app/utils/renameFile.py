from random import randint
import datetime

class RenameFile:
    def __generate(self, oldName):
        nameHashed = str(abs(hash(oldName)))        
        randomNum = str(randint(0, datetime.datetime.now().year))        
        return nameHashed + randomNum
    
    def rename(self, oldFileData):
        newName = f"{self.__generate(oldFileData)}"
        return newName
