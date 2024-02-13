class String():
    def getstring(self):
        self.string_input = input("Enter string:")
    def printstring(self):
        print(self.string_input.upper())
        
str = String()
str.getstring()
str.printstring()
        
