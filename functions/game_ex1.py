import pgzrun 

HEIGHT = 600
WIDTH = 800

p = Actor('ironman', (500,300))
c = Actor('cookie_img')

def draw():
    screen.fill('light yellow')
    p.draw()
    c.draw()
    # print drawing

def update():
    p.x -=1
    p.angle =-30
    if p.x < 0:
        p.x = WIDTH
        #p.x =0
    print(p.x, p.y)


pgzrun.go()
