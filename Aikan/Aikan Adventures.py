from gamelib import *

game = Game(800,600,"Aikan Adventures")
game.setMusic("sound//Dire_Dire_Docks.wav")

plat1 = Image("images//plat1.png",game)
plat2 = Image("images//plat2.png",game)
bullet = Image("images//Bullet.png",game)
shadow3 = Image("images//Shadow3.png",game)
logo = Image("images//logo1.png",game)
logo1 = Image("images//logo2.png",game)
logo2 = Image("images//logo3.png",game)
logo3 = Image("images//logo4.png",game)

bullet.resizeBy(100)
plat1.resizeBy(-20)
plat2.resizeBy(-20)

aikan_s = Animation("images//megaman_shoot.png",2,game,65/1,68/2,10)
aikan_s.moveTo(100,100)
aikan_s.resizeBy(125)

aikan = Animation("images//megaman_w.png",11,game,384/3,512/4,10)

Shadow1 = Animation("images//Shadow9.png",3,game,154/3,73,10)
Shadow2 = Animation("images//Shadow1.png",3,game,138/3,31,10)
Shadow3 = Animation("images//Shadow2.png",3,game,155/3,59,10)
Shadow4 = Animation("images//Shadow6.png",3,game,166/3,72,10)
time1 = Image("images\\time.png",game)
health1 = Image("images\\Health.png",game)


time = []
Time = []
Health = []
health = []
shadow1 = []
shadow2 = []
shadow3 = []
shadow4 = []
shadow5 = []
shadow6 = []
shadow7 = []
shadow8 = []
shadowkills = 0
shadowkills2 = 0
shadowkills3 = 0
shadowkills4 = 0
shadowkills5 = 0
shadowkills6 = 0
shadowkills7 = 0
shadowkills8 = 0
time = 2000

#Sound
shooting = Sound("sound//shootingsound.wav",1)
jump = Sound("sound//jump.wav",2)
power = Sound("sound//PowerUp.wav",3)
hurt = Sound("sound//necksnap.wav",4)
explosion = Sound("sound//Arcade Explo A.wav",5)

#ShadowImport
for times in range(5):
    shadow1.append(Animation("images//Shadow1.png",3,game,138/3,31,10) )

for times in range(6):
    shadow2.append(Animation("images//Shadow2.png",3,game,155/3,59,10) )

for times in range(5):
    shadow3.append(Animation("images//Shadow3.png",3,game,152/3,55,10) )

for times in range(6):
    shadow4.append(Animation("images//Shadow4.png",3,game,147/3,58,10) )

for times in range(5):
    shadow5.append(Animation("images//Shadow5.png",3,game,146/3,50,10) )

for times in range(5):
    shadow6.append(Animation("images//Shadow7.png",3,game,159/3,63,10) )

for times in range(5):
    shadow7.append(Animation("images//Shadow6.png",3,game,166/3,72,10) )

for times in range(5):
    shadow8.append(Animation("images//Shadow9.png",3,game,154/3,73,10) )

for num in range(20):
    Time.append( Image("images\\time.png",game) )

for num in range(20):
    Health.append( Image("images\\Health.png",game) )

#ShadowMovement
for a in shadow1:
    x = randint(720,780)
    y = randint(565,576)
    s = randint(1,4)
    a.moveTo(x,y)
    a.setSpeed(s,90)

for b in shadow2:
    x = randint(720,760)
    y = randint(560,575)
    s = randint(3,5)
    b.moveTo(x,y)
    b.setSpeed(s,90)

for c in shadow3:
    x = randint(720,760)
    y = randint(200,550)
    s = randint(3,5)
    c.moveTo(x,y)
    c.setSpeed(s,90)

for d in shadow4:
    x = randint(720,760)
    y = randint(200,550)
    s = randint(3,5)
    d.moveTo(x,y)
    d.setSpeed(s,90)

for e in shadow5:
    x = randint(720,760)
    y = randint(560,575)
    s = randint(4,6)
    e.moveTo(x,y)
    e.setSpeed(s,90)

for f in shadow6:
    x = randint(720,760)
    y = randint(560,575)
    s = randint(5,7)
    f.moveTo(x,y)
    f.setSpeed(s,90)

for g in shadow7:
    x = randint(720,760)
    y = randint(200,550)
    s = randint(5,7)
    g.moveTo(x,y)
    g.setSpeed(s,90)

for h in shadow8:
    x = randint(720,760)
    y = randint(560,575)
    s = randint(5,7)
    h.moveTo(x,y)
    h.setSpeed(s,90)


aikan.stop()

for t in Time:
    t.resizeBy(-25)
    x = game.width + randint(100 ,10500)
    y = randint(5 ,550)
    s = randint(4,8)
    t.moveTo(x,y)
    t.setSpeed(s,90)

for h in Health:
    h.resizeBy(-25)
    x = game.width + randint(100 ,10500)
    y = randint(5 ,550)
    s = randint(4,8)
    h.moveTo(x,y)
    h.setSpeed(s,90)

bk = Image("images\\Aikan Background.png",game)
bk.resizeTo(game.width,game.height)
game.setBackground(bk)

x = game.width +100
y = randint(150,250)
plat1.moveTo(x,y)
plat1.setSpeed(3,90)

x = game.width +100
y = randint(400,500)
plat2.moveTo(x,y)
plat2.setSpeed(5,90)

bullet.visible = False
landed = False
jumping = False
factor = 1

logo.resizeBy(-30)
logo1.resizeBy(-60)
logo2.resizeBy(20)
logo3.resizeBy(-60)
game.playMusic()
aikan.health = 200
game.over = False

while not game.over:
    game.processInput()

    game.scrollBackground("left",2)
    aikan.moveTo(100,255)
    logo.moveTo(425,100)
    logo1.moveTo(420,200)
    plat1.moveTo(100,350)
    Shadow1.moveTo(600,400)
    Shadow2.moveTo(500,550)
    Shadow3.moveTo(400,550)
    Shadow4.moveTo(100,100)
    health1.moveTo(400,300)
    time1.moveTo(700,205)
    if keys.Pressed[K_SPACE]:
        game.over = True
    game.update(30)
    
game.over = False
while not game.over:
    game.processInput()
    game.scrollBackground("left", 2)

    if time > 0:
        time -= 1

    bk.draw()
    plat1.move()
    plat2.move()
    bullet.move()
    
    #Shadow
    for a in shadow1:
        a.move(True)
        if a.collidedWith(bullet,"rectangle"):
            a.visible = False
            game.score += 1
            shadowkills += 1
            bullet.visible = False
            explosion.play()
        if aikan.collidedWith(a,"rectangle"):
            aikan.health -= 1
    
    for b in shadow2:
        b.move(True)
        if b.collidedWith(bullet,"rectangle"):
            b.visible = False
            game.score += 2
            shadowkills2 += 1
            bullet.visible = False
            explosion.play()
        if aikan.collidedWith(b,"rectangle"):
            aikan.health -= 1

    if (shadowkills >= 30 or shadowkills >= 25):
        for c in shadow3:
            c.move(True)
            if c.collidedWith(bullet,"rectangle"):
                c.visible = False
                game.score += 2
                shadowkills3 += 1
                bullet.visible = False
                explosion.play()
            if aikan.collidedWith(c,"rectangle"):
                aikan.health -= 1

    if (shadowkills2 >= 30 or shadowkills2 >= 25):
        for d in shadow4:
            d.move(True)
            if d.collidedWith(bullet,"rectangle"):
                d.visible = False
                game.score += 2
                shadowkills4 += 1
                bullet.visible = False
                explosion.play()
            if aikan.collidedWith(d,"rectangle"):
                aikan.health -= 1
                
        if (shadowkills3 >= 30 or shadowkills3 >= 25):
            for e in shadow5:
                e.move(True)
                if e.collidedWith(bullet,"rectangle"):
                    e.visible = False
                    game.score += 2
                    shadowkills5 += 1
                    bullet.visible = False
                    explosion.play()
                if aikan.collidedWith(e,"rectangle"):
                    aikan.health -= 1

        if (shadowkills4 >= 30 or shadowkills4 >= 25):
            for f in shadow6:
                f.move(True)
                if f.collidedWith(bullet,"rectangle"):
                    f.visible = False
                    game.score += 2
                    shadowkills6 += 1
                    bullet.visible = False
                    explosion.play()
                if aikan.collidedWith(f,"rectangle"):
                    aikan.health -= 1

        if (shadowkills5 >= 30 or shadowkills5 >= 25):
            for g in shadow7:
                g.move(True)
                if g.collidedWith(bullet,"rectangle"):
                    g.visible = False
                    game.score += 2
                    shadowkills6 += 1
                    bullet.visible = False
                    explosion.play()
                if aikan.collidedWith(f,"rectangle"):
                    aikan.health -= 1

        if (shadowkills6 >= 30 or shadowkills6 >= 25):
            for h in shadow8:
                h.move(True)
                if h.collidedWith(bullet,"rectangle"):
                    h.visible = False
                    game.score += 2
                    shadowkills6 += 1
                    bullet.visible = False
                    explosion.play()
                if aikan.collidedWith(f,"rectangle"):
                    aikan.health -= 1
        if shadowkills6 > 35:
            shadowkills = 0
            for a in shadow1:
                a.visible = True
            for b in shadow2:
                b.visible = True
                
    #ShadowKills
    if shadowkills in [5,10,15,20]:
        for a in shadow1:
            x = randint(720,780)
            y = randint(565,576)
            s = randint(2,6)
            a.moveTo(x,y)
            a.setSpeed(s,90)
            a.visible = True

    if shadowkills2 in [6,12,18,24]:
        for b in shadow2:
            x = randint(720,760)
            y = randint(560,575)
            s = randint(3,5)
            b.moveTo(x,y)
            b.setSpeed(s,90)
            b.visible = True

    if (shadowkills >= 30 or shadowkills >= 25) and shadowkills3 in [5,10,15,20]:
        for c in shadow3:
            x = randint(720,760)
            y = randint(200,550)
            s = randint(3,5)
            c.moveTo(x,y)
            c.setSpeed(s,90)
            c.visible = True

    if (shadowkills2 >= 30 or shadowkills2 >= 25) and shadowkills4 in [5,10,15,20]:
        for d in shadow4:
            x = randint(720,760)
            y = randint(200,550)
            s = randint(3,5)
            d.moveTo(x,y)
            d.setSpeed(s,90)
            d.visible = True

    if (shadowkills3 >= 30 or shadowkills3 >= 25) and shadowkills5 in [5,10,15,20]:
        for e in shadow5:
            x = randint(720,760)
            y = randint(560,575)
            s = randint(4,6)
            e.moveTo(x,y)
            e.setSpeed(s,90)
            e.visible = True

    if (shadowkills4 >= 30 or shadowkills4 >= 25) and shadowkills6 in [5,10,15,20]:
        for e in shadow6:
            x = randint(720,760)
            y = randint(560,575)
            s = randint(4,6)
            e.moveTo(x,y)
            e.setSpeed(s,90)
            e.visible = True

    if (shadowkills5 >= 30 or shadowkills5 >= 25) and shadowkills7 in [5,10,15,20]:
        for g in shadow7:
            x = randint(720,760)
            y = randint(200,550)
            s = randint(4,6)
            g.moveTo(x,y)
            g.setSpeed(s,90)
            g.visible = True

    if (shadowkills6 >= 30 or shadowkills6 >= 25) and shadowkills8 in [5,10,15,20]:
        for h in shadow8:
            x = randint(720,760)
            y = randint(560,575)
            s = randint(4,6)
            h.moveTo(x,y)
            h.setSpeed(s,90)
            h.visible = True
            
    #CollidedWith
    if aikan.collidedWith(plat1,"rectangle"):
            landed = True

    if aikan.collidedWith(plat2,"rectangle"):
            landed = True

    #PowerUps
    for t in Time:
        t.move()
        if aikan.collidedWith(t):
            time += 50
            t.visible = False
            power.play()

    for h in Health:
        h.move()
        if aikan.collidedWith(h):
            aikan.health += 10
            h.visible = False
            power.play()

    #Moving
    if (keys.Pressed[K_a] or keys.Pressed[K_LEFT]) and aikan.left > 0 :
        aikan.prevFrame()
        aikan.x -= 8
    elif keys.Pressed[K_d] or keys.Pressed[K_RIGHT]:
        aikan.nextFrame()
        aikan.x += 8
    else:
        aikan.move(True)
        
    #isOffScreen
    if plat1.isOffScreen("left"):
        x = game.width +100
        y = randint(150,250)
        plat1.moveTo(x,y)
        
    if plat2.isOffScreen("left"):
        x = game.width +100
        y = randint(400,500)
        plat2.moveTo(x,y)

    #Shooting
    if keys.Pressed[K_SPACE] and not bullet.visible:
        bullet.moveTowards(mouse,15)
        bullet.setSpeed(15)
        bullet.visible = True
        bullet.moveTo(aikan.x,aikan.y)
        shooting.play()

    if bullet.isOffScreen():
        bullet.visible = False
        
    #Jumping = Start
    if aikan.y < 550:
        landed = False
    else:
        landed = True

    if aikan.collidedWith(plat1,"rectangle"):
            landed = True

    if aikan.collidedWith(plat2,"rectangle"):
            landed = True
        
    if jumping:
        aikan.y -= 30 * factor
        factor *= .95
        landed = False

        if factor < .18:
            jumping = False
            factor = 1
            
    if keys.Pressed[K_w] and landed and not jumping:
            jumping = True
            jump.play()

    if keys.Pressed[K_UP] and landed and not jumping:
            jumping = True
            jump.play()
            
    if not landed:
        aikan.y += 9
    #Jumping = Over

    #Ending Game
    if aikan.health < 1:
        game.over =  True

    if time < 1:
        game.over = True
        
    game.displayScore(150,5)
    game.drawText("Time: " + str(time),250,5)
    game.drawText("Health:" + str(aikan.health), 5,5)
    game.update(60)
    
logo2.moveTo(400,200)
logo3.moveTo(500,550)
game.update()
game.wait(K_SPACE)
game.quit()
