class Animal:
    def __init__(self, blooded = "unknown", appearance = "unknown",
                 birthType="unknown"):
        self.blooded = blooded
        self.appearance = appearance
        self.birthType = birthType

    @property
    def blooded(self):
        return self.__blooded

    @blooded.setter
    def blooded(self,blooded):
        self.__blooded = blooded

    @property
    def nurseYoung(self):
        return self.__nurseYoung

    @nurseYoung.setter
    def nurseYoung(self, nurseYoung):
        self.__nurseYoung = nurseYoung

    @property
    def appearance(self):
        return self.__appearance

    @appearance.setter
    def appearance(self,appearance):
        self.__appearance = appearance

class Mammal(Animal):
    def __init__(self, blooded="warm blooded", appearance="hair or fur",
                 nurseYoung="True"):
        Animal.__init__(self, nurseYoung, appearance, blooded)

        self.__birthType = birthType

    @property
    def birthType(self):
        return self.__birthType

    @birthType.setter
    def birthType(self, birthType):
        self.__birthType = birthType