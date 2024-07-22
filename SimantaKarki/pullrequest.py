class House:
    window = 10
    door = 2
    color = "red"
    
    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color
    
oggy_house = House()
hari_house = House()

oggy_house.set_color("blue")
print(oggy_house.get_color())

# print(hari_house.color)
# print(oggy_house.color)

