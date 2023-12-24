#Homework 1
class Cassa:
    cahs = 30590
    def top_up(self, pokup):
        self.pokup = pokup
        pokup += Cassa.cahs
        return f'В кассе {pokup}'
    
    def count_1000(self):
        return Cassa.cahs//1000
    
    def take_away(self, x):
        if x <= self.cahs:
            self.cahs -= x
            return f'Произведенно изъятие на сумму {x}.'
        else:
            return f'В кассе не достаточно денег.'

a = Cassa()
print(a.top_up(500))
print(f'В кассе {a.count_1000()} целых тысяч.')
print('Какую сумму хотите изъять? ')
print(a.take_away(int(input())))

#Homework 2
class Turtle:
    def __init__(self, x, y, s):
        self.x = x
        self.y = y
        self.s = s
    
    def go_up(self):
        self.y += self.s
        return self.y
    
    def go_down(self):
        self.y -= self.s
        return self.y
    
    def go_left(self):
        self.x -= self.s
        return self.x
    
    def go_right(self):
        self.y += self.s
        return self.y
    
    def evolve(self):
        self.s += 1
        return self.s
    
    def degrade(self):
        if self.s <= 0:
            return 's = 0'
        else:
            self.s -= 1
            return self.s

    def count_moves(self, x2, y2):
        return self.x - x2, self.y - y2

b = Turtle(6, 10, 20)
print(b.go_up())
print(b.go_down())
print(b.go_left())
print(b.go_right())
print(b.evolve())
print(b.degrade())
print(b.count_moves(11, 30))