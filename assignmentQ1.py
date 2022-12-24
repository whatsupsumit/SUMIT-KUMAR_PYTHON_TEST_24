class Classy(object):
    def __init__(self):
        self.items = []
        self.classiness = 0

    def getClassiness(self):
        try:
            for i in self.items:
                if i == "tophat":
                    self.classiness += 2
                elif i == "bowtie":
                    self.classiness += 4
                elif i == "monocle":
                    self.classiness += 5
                self.items.pop(0)
            self.items.pop(0)
        except IndexError as e:
            pass
        return self.classiness

    def addItem(self, item):
        self.items.append(item)

# Test cases
me = Classy()

# Should be 0
print(me.getClassiness())

me.addItem("tophat")
# Should be 2
print (me.getClassiness())

me.addItem("bowtie")
me.addItem("jacket")
me.addItem("monocle")
# Should be 11
print (me.getClassiness())

me.addItem("bowtie")
# Should be 15
print(me.getClassiness())