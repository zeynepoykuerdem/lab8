from abc import ABC


class Address(ABC):
    address=""
    def init(self,ad):
            self.address=ad

    def calculateFreqs(self):
        pass


class ListCount(Address):
    def init(self, zeynep):

        super(ListCount, self).init(zeynep)

    def calculateFreqs(self ):
        with open(self.address)as f :
            lines=f.read()
        print(lines)



class DictCount(Address):

    def init(self):
        super(DictCount, self).init()

    def calculateFreqs(self):
        super().calculateFreqs()

myobj=ListCount("C:\\Users\\zeyne\\OneDrive\\Desktop\\strange.txt")
myobj.calculateFreqs()
