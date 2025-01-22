#openfile
file = open("profile.dart","r")
print(file.read())

#create file
newfile =open("vall","w")
newfile.write("raoré was part of the group of army officers that supported the January 2022 Burkina Faso coup d'état and brought the Patriotic Movement for Safeguard and Restoration military junta to power.[6][5] From March 2022, he served as the head of an artillery regiment in Kaya.[3][5] Whether he was ever associated with the "Cobra" special forces, a counterterrorist unit founded in 2019, is disputed. According to the BBC, Al Jazeera, and Die Tageszeitung, he was part of the unit at some point.[10][4][11] However, news magazine Jeune Afrique stated that he was never associated with the "Cobras".[5]
")
#error
Fie.open("profile.text","r")
print(file.read())
except FileNotFoundError:
print("this file not found")
finally:
print("welcome again")