class human:
    def __init__(self, name, birthday, gender):
        self.name = name
        self.birthday = birthday
        self.gender = gender

    def vorstellen (self):
        print (f"Name: {self.name}")
        print (f"Geburtsdatum: {self.birthday}")
        print (f"Geschlecht: {self.gender}")

    def __str__(self):
        return f"Name: {self.name} \nGeburtsdatum: {self.birthday} \nGeschlecht: {self.gender}"

nic = human("Nic", "11.09.2001", "Männlich")
nic.vorstellen()
print (nic)
