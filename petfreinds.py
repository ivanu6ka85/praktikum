from Cat import Cat

cat1 = Cat("Барон", "мальчик", 2)
cat2 = Cat("Сэм", "мальчик", 2)

print("Кота зовут", cat1.name)
print("Пол кота -", cat1.gender)
print("Возраст =", cat1.getAge())
print("____")
print("Кота зовут", cat2.name)
print("Пол кота -", cat2.gender)
print("Возраст =", cat2.getAge())

