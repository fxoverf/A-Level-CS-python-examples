#9618 w2023 p42 q3
import datetime

class Character:
    #self.__Speed int
    #self.__Intelligence float
    #self.__DateOfBirth date
    #self.__CharacterName str
    def __init__(self, characterName, dob, intel, speed):
        self.__CharacterName = characterName
        self.__DateOfBirth = dob
        self.__Intelligence = intel
        self.__Speed = speed
    def GetIntelligence(self):
        return self.__Intelligence
    def GetName(self):
        return self.__CharacterName
    def SetIntelligence(self, new_intel):
        self.__Intelligence = new_intel
    def Learn(self):
        self.__Intelligence += (self.__Intelligence / 100) * 10
    def ReturnAge(self):
        return (2023 - self.__DateOfBirth.year)

class MagicCharacter(Character):
    #self.__Element str
    def __init__(self, Elem, characterName, dob, intel, speed):
        super().__init__(characterName, dob, intel, speed)
        self.__Element = Elem
    def Learn(self):
        if self.__Element in ["fire", "water"]:
            super().SetIntelligence(super().GetIntelligence() + (super().GetIntelligence() / 100 * 20))
        elif self.__Element == "earth":
            super().SetIntelligence(super().GetIntelligence() + (super().GetIntelligence() / 100 * 30))
        else:
            super().Learn()

#main program

FirstCharacter = Character("Royal",(datetime.date(2019, 1, 1)) , 70, 30)
FirstCharacter.Learn()
print(f"Character Name: {FirstCharacter.GetName()}")
print(f"Age: {FirstCharacter.ReturnAge()}")
print(f"Intelligence: {FirstCharacter.GetIntelligence()}")

FirstMagic = MagicCharacter("fire", "Light", (datetime.date(2018, 3, 3)), 75, 22)
FirstMagic.Learn()
print(f"\nCharacter Name: {FirstMagic.GetName()}")
print(f"Age: {FirstMagic.ReturnAge()}")
print(f"Intelligence: {FirstMagic.GetIntelligence()}")