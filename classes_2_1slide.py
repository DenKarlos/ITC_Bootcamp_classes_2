class Factory:
    def endgine(self):
        return "Двигатель создан"

    def bridge(self):
        return "Ходовая часть создана"


class Toyota(Factory):
    def wheels(self):
        return "Колёса готовы"

    def windows(self):
        return "Стёкла готовы"


commands = [Toyota().endgine(), Toyota().bridge(),
            Toyota().wheels(), Toyota().windows()]
print(commands)
