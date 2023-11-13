import os.path 

A = os.path.isfile('Contacts.txt') 
if A == False:
    f = open('Contacts.txt', 'w+')
    f.close()
    
def addContacts(i):
    with open('Contacts.txt', 'a') as file:
        file.write(i[0]+'~'+i[1]+'~'+i[2]+'~'+i[3]+'\n')
        
def view():
    element = []
    data = []
    with open('Contacts.txt', 'r') as file:
        for line in file:
            line = line[:-1]
            element = line.split('~')
            data.append(element)
        return data
    
def search(i):
    data = []
    sname = i
    elements = []
    
    with open('Contacts.txt', 'r') as file:
        for line in file:
            line = line[:-1]
            elements = line.split('~')
            for element in elements:
                if sname in element:
                    data.append(elements)
        return data
    
def remove(i):
    def save(i):
        with open('Contacts.txt', 'w') as file:
            for j in i:
                file.write(j[0]+'~'+j[1]+'~'+j[2]+'~'+j[3]+'\n')
    
    data = []
    rname = i
    with open('Contacts.txt', 'r') as file:
        for line in file:
            line = line[:-1]
            element = line.split('~')
            data.append(element)
            for row in element:
                if row == rname:
                    data.remove(element)
        save(data)

def update(i):
    def save(i):
        with open('Contacts.txt', 'w') as file:
            for j in i:
                file.write(j[0]+'~'+j[1]+'~'+j[2]+'~'+j[3]+'\n')
    
    data = []
    uname = i[0]
    ulist = []
    name = i[1]
    gender= i[2]
    telephone = i[3]
    email = i[4]
    ulist = [name, gender, telephone, email]
    
    with open('Contacts.txt', 'r') as file:
        for line in file:
            line = line[:-1]
            element = line.split('~')
            data.append(element)
            for row in element:
                if row == uname:
                    index = data.index(element)
                    data[index] = ulist
        save(data)