class Human:
    def __init__(self,name,phone,age):
        self.name = name
        self.phone = phone
        self.age = age
    def get_phone(self):
        return self.phone
    def set_phone(self,phone_no):
        self.phone = phone_no
        return self.phone

i = Human('jagan',123,5)

print(i.name)
print(i.phone)
print(i.age)
i.phone = 456
print(i.phone)
print(i.get_phone())
print(i.set_phone(789))