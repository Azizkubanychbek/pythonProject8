class JunDev:
    def __init__(self, name, salary, proglang):
        self.name = name
        self.salary = salary
        self.proglang = proglang

    def copypaste(self, resourse):
        print(f'this proger can copy paste from - {resourse}')

    def __str__(self):
        return f'name - {self.name}\n' \
               f'salary - {self.salary}\n' \
               f'proglang - {self.proglang}'





class MidDev(JunDev):
    def __init__(self, name, salary, proglang, age, gender, height):
        JunDev.__init__(self, name, salary, proglang)
        self.age = age
        self.gender = gender
        self.height = height

    def blabla(self, blal):
        print(f'this proger can  - {blal}')


class SenDev(MidDev):
    def __init__(self, name, salary, proglang, age, gender, height, weight):
        MidDev.__init__(self, name, salary, proglang, age, gender, height)
        self.weight = weight

    def nvswguwk(self, gopf):
        print(f'aaaaaaaaaaaaaa - {gopf}')


jun1 = SenDev(name='Aziz', salary=300, proglang='pyhon', age=35, gender='male', height=180)
print(jun1)
j = JunDev('', '', '')
j.copypaste('blBLlbs')
g = MidDev('Aziz', 300, 'pyhon', 35, 'male', 180)
g.blabla("fujfnkjfn")
k = SenDev('Aziz', 300, 'pyhon', 35, 'male', 180, 100)
k.nvswguwk=("gourehgreoiuhgw")
