class Avtobus:
    def __init__(self, nomi, rangi, yoshi):
        self.nomi = nomi
        self.rangi = rangi
        self.yoshi = yoshi

    def avtobus_haqida(self):
        return f"Avtobus nomi: {self.nomi}, Avtobus rangi: {self.rangi}, Avtobus yoshi: {self.yoshi} yil"

class Avtobus_haydovchi:
    def __init__(self, ismi, familiyasi, yoshi):
        self.ismi = ismi
        self.familiyasi = familiyasi
        self.yoshi = yoshi

    def haydovchi_haqida(self):
        return f"Haydovchi ismi: {self.ismi}, Haydovchi familiyasi: {self.familiyasi}, Haydovchi yoshi: {self.yoshi} yil"

class Yo_l:
    def __init__(self, nomi, uzunligi):
        self.nomi = nomi
        self.uzunligi = uzunligi

    def yo_l_haqida(self):
        return f"Yo'l nomi: {self.nomi}, Yo'l uzunligi: {self.uzunligi} km"

avtobus1 = Avtobus("Avtobus-1", "Qizil", 10)
avtobus2 = Avtobus("Avtobus-2", "Ko'k", 5)

haydovchi1 = Avtobus_haydovchi("Ali", "Aliyev", 30)
haydovchi2 = Avtobus_haydovchi("Vali", "Valiyev", 25)

yol1 = Yo_l("Yo'l-1", 100)
yol2 = Yo_l("Yo'l-2", 50)

print(avtobus1.avtobus_haqida())
print(avtobus2.avtobus_haqida())

print(haydovchi1.haydovchi_haqida())
print(haydovchi2.haydovchi_haqida())

print(yol1.yo_l_haqida())
print(yol2.yo_l_haqida())

class Shaxar:
    def __init__(self, nomi, aholisi):
        self.nomi = nomi
        self.aholisi = aholisi

    def shaxar_haqida(self):
        return f"Shaxar nomi: {self.nomi}, Shaxar aholisi: {self.aholisi} kishi"

shaxar1 = Shaxar("Toshkent", 2500000)
shaxar2 = Shaxar("Samarkand", 500000)

print(shaxar1.shaxar_haqida())
print(shaxar2.shaxar_haqida())

class Universitet:
    def __init__(self, nomi, talabalar_soni):
        self.nomi = nomi
        self.talabalar_soni = talabalar_soni

    def universitet_haqida(self):
        return f"Universitet nomi: {self.nomi}, Universitet talabalar soni: {self.talabalar_soni} kishi"

universitet1 = Universitet("Toshkent Davlat Universiteti", 50000)
universitet2 = Universitet("Samarkand Davlat Universiteti", 20000)

print(universitet1.universitet_haqida())
print(universitet2.universitet_haqida())