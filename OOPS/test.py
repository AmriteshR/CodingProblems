class XYZ:
    def __init__(self,name) -> None:
        self.__name = name

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,name):
        self.__name = name
    

x = XYZ("AR")
print(x.name)
x.name = "SH"
print(x.name)
