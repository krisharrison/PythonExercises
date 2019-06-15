from pathlib import Path

#Make directory
#path = Path("emails")
#print(path.mkdir())

#Remove Directory
#print(path.rmdir())

#Find out whether path exists
#path = Path("Ecommerce
#print(path.exists())

#Path directories
path = Path()#Curent path
#get all files the end in '.py' print(path.glob('*.py'))

#looping over and displaying all files that end in .py
path = Path()#Curent path

'''for file in path.glob('*.py'):
    print(file)'''


#looping over and displaying all files
for file in path.glob('*'):
    print(file)