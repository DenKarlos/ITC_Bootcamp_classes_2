class Zoo:
    def __init__(self):
        pass

Zoo = Zoo()
Zoo.animal_1 = 'Тигр'
Zoo.animal_2 = 'Бегемот'
Zoo.animal_3 = 'Жираф'
Zoo.animal_1 = 'Лев'
Zoo.animal_4 = [Zoo.animal_2, Zoo.animal_3]
Zoo.animal_3 = 'Змея'

print(Zoo.animal_4)



