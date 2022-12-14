from pgzero.actor import Actor

class MyActor(Actor):
    speedx = 5
    speedy = 5

    def move(self):
        self.x = self.speedx 
        self.y = self.speedy

    def __init__(self, image, pos=..., anchor=..., speed=0, **kwargs):
        super().__init__(image, pos, anchor, **kwargs)
        self.speedx = self.speedy = speed

    def move(self):
        self.x += self.speedx
        self.y += self.speedy

#actor = MyActor('ironman',(100, 100), speed = 5)
#print(dir(MyActor))
print(filter(lambda i : not i.startswith('__') or i.startswith('_')), dir(MyActor)) 