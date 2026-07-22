# from cmu_graphics import * 
# import random

# class Bird:
#     def __init__(self, birdX, birdY, birdWidth, birdHeight): 
#         self.birdX = birdX
#         self.birdY = birdY
#         self.birdWidth = birdWidth
#         self.birdHeight = birdHeight
#         self.birdAngle = 0
#         self.dy = 0

#     def moveBird(self, dy): 
#         self.birdY += dy

#     def gravityMove(self, gravity):
#         self.dy += gravity

#     def updatePosition(self):
#         self.birdY += self.dy

#     def flap(self, move): 
#         self.dy = -move

# class Pipe:
#     def __init__(self, pipeX, pipeWidth, pipeHeight, pipeGap): 
#         self.pipeX = pipeX
#         self.pipeWidth = pipeWidth
#         self.pipeHeight = pipeHeight
#         self.pipeGap = pipeGap
#         self.pipeSize = 60
#         self.pipeColor = 'lightPink'
#         self.scored = False
    
#     def pipeMove(self, dx): 
#         self.pipeX -= dx


# class Game:
#     def __init__(self):
#         self.multiplayer = False 
#         self.width = 800
#         self.height = 650
#         self.dx = 10
#         self.lives = 3
#         self.lives2 = 3  
#         self.score = 0
#         self.gameOver = False
#         self.paused = True
#         self.startScreen = True
#         self.collision = False
#         self.pipeWidth = 60
#         self.pipeGap = 200
#         self.bird = Bird(200, self.height // 4, self.width // 15, self.height // 15)
#         self.bird.dy = 0
#         self.pipes = self.createPipes(self.height // 2)
#         self.collisionCooldown = 0
#         self.bird2 = None
#         self.pipes2 = []



#     def createPipes(self, availableHeight):
#         pipeList = []
#         spacing = 300
#         startX = self.width + 100
#         for i in range(4):
#             if self.multiplayer == True and self.bird2: 
#                 pipeX = startX + i * spacing
#                 maxPipeHeight = max(100, availableHeight - self.pipeGap - 100)
#                 minPipeHeight = 50
#                 if maxPipeHeight <= minPipeHeight:
#                     pipeHeight = minPipeHeight
#                 else:
#                     pipeHeight = random.randint(minPipeHeight, maxPipeHeight)
#                 pipeWidth = random.randint(40, 80)  
                
#                 pipe = Pipe(pipeX, pipeWidth, pipeHeight, self.pipeGap)
#                 pipeList.append(pipe)
#             else:
#                 pipeX = startX + i * spacing
#                 pipeHeight = random.randint(150, 400) 
#                 pipe = Pipe(pipeX, self.pipeWidth, pipeHeight, self.pipeGap)
#                 pipeList.append(pipe)
        
#         return pipeList

#     def resetApp(self):
#         self.multiplayer = False 
#         self.bird2 = None
#         self.lives2 = 3  
#         self.pipes2 = []
#         self.gameOver = False
#         self.score = 0
#         self.paused = True
#         self.startScreen = True
#         self.lives = 3
#         self.bird.birdY = self.height // 4
#         self.bird.dy = 0
#         self.pipes = self.createPipes(self.height // 2)
#         if self.multiplayer:  
#             self.bird2 = Bird(200, 3 * self.height // 4, 
#                               self.width // 15, self.height // 15) 
#             self.pipes2 = self.createPipes(self.height // 2)

#     def isCollision(self, bird, pipes):
#         birdLeft = bird.birdX - bird.birdWidth / 2
#         birdRight = bird.birdX + bird.birdWidth / 2
#         birdTop = bird.birdY - bird.birdHeight / 2
#         birdBottom = bird.birdY + bird.birdHeight / 2

#         for pipe in pipes:
#             cx = pipe.pipeX
#             h = pipe.pipeHeight
#             w = pipe.pipeWidth
#             gap = pipe.pipeGap

#             if (birdRight > cx and birdLeft < cx + w and birdBottom > 0 and birdTop < h): 
#                 return True
#             if (birdRight > cx and birdLeft < cx + w and birdBottom > h + gap):
#                 return True
#         return False

#     def update(self): 
#         self.bird.gravityMove(2)
#         self.bird.updatePosition()

#         for pipe in self.pipes:
#             pipe.pipeMove(self.dx)
#             if pipe.pipeX + pipe.pipeSize <= 0:
#                 lastPipe = max(self.pipes, key=lambda p: p.pipeX)
#                 pipe.pipeX = lastPipe.pipeX + 300
#                 maxPipeHeight = max(100, self.height // 2 - self.pipeGap - 100)
#                 if maxPipeHeight <= 50:
#                     pipe.pipeHeight = 50
#                 else:
#                     pipe.pipeHeight = random.randint(50, maxPipeHeight)
#                 pipe.scored = False

#         if self.collisionCooldown > 0:
#             self.collisionCooldown -= 1

#         if self.isCollision(self.bird, self.pipes):
#             if self.collisionCooldown == 0:
#                 self.lives -= 1
#                 self.collisionCooldown = 20

#         if self.multiplayer:
#             if (self.bird.birdY - self.bird.birdHeight <= 0 or 
#                 self.bird.birdY + self.bird.birdHeight >= self.height // 2):
#                 if self.collisionCooldown == 0:
#                     self.lives -= 1
#                     self.collisionCooldown = 20

#             if self.isCollision(self.bird2, self.pipes2):
#                 if self.collisionCooldown == 0:
#                     self.lives2 -= 1
#                     self.collisionCooldown = 20
#             if (self.bird2.birdY - self.bird2.birdHeight <= self.height // 2 or 
#                 self.bird2.birdY + self.bird2.birdHeight >= self.height):
#                 if self.collisionCooldown == 0:
#                     self.lives2 -= 1
#                     self.collisionCooldown = 20

#             if self.lives <= 0 or (self.multiplayer and self.lives2 <= 0):
#                 self.gameOver = True
#                 self.paused = True

#         else:
#             if (self.bird.birdY - self.bird.birdHeight <= 0 or 
#                 self.bird.birdY + self.bird.birdHeight >= self.height):
#                 if self.collisionCooldown == 0:
#                     self.lives -= 1
#                     self.collisionCooldown = 20

#         if self.lives <= 0:
#             self.gameOver = True
#             self.paused = True

#         for pipe in self.pipes:
#             pipeMid = pipe.pipeX + pipe.pipeWidth / 2
#             birdMid = self.bird.birdX
#             if not pipe.scored and birdMid > pipeMid:
#                 self.score += 1
#                 pipe.scored = True

#         if self.multiplayer and self.bird2:
#             self.bird2.gravityMove(2)
#             self.bird2.updatePosition()

#             for pipe in self.pipes2:
#                 pipe.pipeMove(self.dx)
#                 if pipe.pipeX + pipe.pipeSize <= 0:
#                     lastPipe = max(self.pipes2, key=lambda p: p.pipeX)
#                     pipe.pipeX = lastPipe.pipeX + 300
#                     maxPipeHeight = max(100, self.height // 2 - self.pipeGap - 100)
#                     if maxPipeHeight <= 50:
#                         pipe.pipeHeight = 50
#                     else:
#                         pipe.pipeHeight = random.randint(50, maxPipeHeight)
#                     pipe.scored = False


#     def onAppStart(app):
#         app.game = Game()
#         app.stepsPerSecond = 20
#         app.width = 800
#         app.height = 650

#     def redrawAll(app):
#         drawImage('candy background.jpg', app.width // 2, app.height // 2, 
#                 align='center', width=app.width, height=app.height)

#         if app.game.multiplayer:
#             drawLine(0, app.height // 2, app.width, app.height // 2, fill='black', lineWidth=4)

#             for pipe in app.game.pipes2:
#                 cx = pipe.pipeX
#                 h = pipe.pipeHeight
#                 gap = pipe.pipeGap
#                 size = pipe.pipeSize
#                 bottomY = h + gap
#                 bottomH = app.height // 2 - bottomY
#                 topY = app.height // 2
#                 bottomPipeY = topY + h
#                 bottomHeight = app.height - (bottomPipeY + gap)

#                 drawRect(cx, topY, size, h, fill='lightBlue', border='black', borderWidth=2)
#                 drawRect(cx - 5, topY + h - 2, size + 10, 30, fill='lightBlue', border='black', borderWidth=2)
#                 if bottomHeight > 0:
#                     drawRect(cx, bottomPipeY + gap, size, bottomHeight, fill='lightBlue', border='black', borderWidth=2)
#                     drawRect(cx - 5, bottomPipeY + gap, size + 10, 30, fill='lightBlue', border='black', borderWidth=2)
#                 drawRect(cx, 0, size, h, fill=pipe.pipeColor, border='black', borderWidth=2)
#                 drawRect(cx - 5, h - 2, size + 10, 30, fill=pipe.pipeColor, border='black', borderWidth=2)
#                 if bottomH > 0:
#                     drawRect(cx, bottomY, size, bottomH, fill=pipe.pipeColor, border='black', borderWidth=2)
#                     drawRect(cx - 5, bottomY, size + 10, 30, fill=pipe.pipeColor, border='black', borderWidth=2)

#             drawImage('flapping_bird_fixed-removebg-preview (2).png', app.game.bird.birdX,
#                     app.game.bird.birdY, align='center', width=app.game.bird.birdWidth, 
#                     height=app.game.bird.birdHeight)

#             drawImage('flapping_bird_fixed-removebg-preview (2).png', app.game.bird2.birdX,
#                     app.game.bird2.birdY, align='center', width=app.game.bird2.birdWidth, 
#                     height=app.game.bird2.birdHeight)

#             for i in range(app.game.lives):
#                 drawImage('pixel_heart-removebg-preview.png', 10 + 50 * i, 15, width=50, height=50)

#             for i in range(app.game.lives2):
#                 drawImage('pixel_heart-removebg-preview.png', 10 + 50 * i, app.game.height // 2 + 15, width=50, height=50)

#         else:
#             for pipe in app.game.pipes:
#                 cx = pipe.pipeX
#                 h = pipe.pipeHeight
#                 w = pipe.pipeWidth
#                 gap = pipe.pipeGap
#                 size = pipe.pipeSize

#                 bottomY = h + gap
#                 bottomHeight = app.game.height - bottomY

#                 if h > 0:
#                     drawRect(cx, 0, size, h, fill=pipe.pipeColor, border='black', borderWidth=3)
#                     drawRect(cx - 5, h - 2, size + 10, 30, fill=pipe.pipeColor, border='black', borderWidth=3)

#                 if bottomHeight > 0:
#                     drawRect(cx, bottomY, size, bottomHeight, fill=pipe.pipeColor, border='black', borderWidth=3)
#                     drawRect(cx - 5, bottomY, size + 10, 30, fill=pipe.pipeColor, border='black', borderWidth=3)

#             drawImage('flapping_bird_fixed-removebg-preview (2).png', app.game.bird.birdX,
#                     app.game.bird.birdY, align='center', width=app.game.bird.birdWidth, 
#                     height=app.game.bird.birdHeight)

#             # Draw hearts for Bird 1
#             for i in range(app.game.lives):
#                 drawImage('pixel_heart-removebg-preview.png', 10 + 50 * i, 15, width=50, height=50)

#         if app.game.startScreen:
#             drawLabel('FlappyBird112!', app.game.width // 2, 75, font='fantasy', size=50, bold=True)
#             drawLabel('press any key to start', app.game.width // 2, app.game.height * 3/4, font='orbitron', size=20)
#             drawLabel('press M for multiplayer', app.game.width // 2, app.game.height * 3/4 + 40, font='orbitron', size=18)
#         else:
#             drawLabel(f'{app.game.score}', app.width // 2, 50, size=40, fill='black')

#         if app.game.gameOver:
#             drawLabel('GAME OVER', app.game.width // 2, app.game.height // 2, size=30, fill='red')
#             drawLabel('Press r to restart!', app.game.width // 2, (app.game.height // 2) + 100, size=20, fill='black', bold=True)

#     def onKeyPress(app, key):
#         if app.game.startScreen:
#             if key == 'm': #
#                 app.game.multiplayer = True
#                 app.game.startScreen = False
#                 app.game.paused = False
#                 app.game.bird2 = Bird(200, 3 * app.height // 4, app.width // 15, app.height // 15)
#                 app.game.pipes2 = app.game.createPipes(app.height // 2)
#             else:
#                 app.game.startScreen = False
#                 app.game.paused = False
#         elif key == 'r' and app.game.gameOver:
#             app.game.resetApp()
#         elif key == 'space' and not app.game.paused:
#             app.game.bird.flap(12)
#         elif key == 'w' and app.game.multiplayer and app.game.bird2:
#             app.game.bird2.flap(12)

#     def onStep(app):
#         if not app.game.paused:
#             app.game.update()

# runApp()


























from cmu_graphics import * 
import random

class Bird:
    def __init__(self, birdX, birdY, birdWidth, birdHeight): 
        self.birdX = birdX
        self.birdY = birdY
        self.birdWidth = birdWidth
        self.birdHeight = birdHeight
        self.birdAngle = 0
        self.dy = 0

    def moveBird(self, dy): 
        self.birdY += dy

    def gravityMove(self, gravity):
        self.dy += gravity

    def updatePosition(self):
        self.birdY += self.dy

    def flap(self, move): 
        self.dy = -move

class Pipe:
    def __init__(self, pipeX, pipeWidth, pipeHeight, pipeGap): 
        self.pipeX = pipeX
        self.pipeWidth = pipeWidth
        self.pipeHeight = pipeHeight
        self.pipeGap = pipeGap
        self.pipeSize = 60
        self.pipeColor = 'lightPink'
        self.scored = False
    
    def pipeMove(self, dx): 
        self.pipeX -= dx

class Game:
    def __init__(self): 
        self.width = 800
        self.height = 650
        self.dx = 10
        self.lives = 3
        self.score = 0
        self.gameOver = False
        self.paused = True
        self.startScreen = True
        self.collision = False
        self.pipeWidth = 60
        self.pipeGap = 200
        self.multiplayer = False
        self.bird = Bird(200, self.height // 4, self.width // 15, self.height // 15)
        self.bird2 = None
        self.bird.dy = 0
        self.pipes = self.createPipes(self.height // 2)
        self.pipes2 = []
        self.collisionCooldown = 0

    def createPipes(self, availableHeight):
        pipeList = []
        spacing = 300
        startX = self.width + 100
        for i in range(4):
            pipeX = startX + i * spacing
            if self.multiplayer and self.bird2: 
                maxPipeHeight = max(100, availableHeight - self.pipeGap - 100)
                minPipeHeight = 50
                pipeHeight = max(minPipeHeight, random.randint(minPipeHeight, maxPipeHeight))
                pipeWidth = random.randint(40, 80)  
                pipe = Pipe(pipeX, pipeWidth, pipeHeight, self.pipeGap)
            else:
                pipeHeight = random.randint(150, 400) 
                pipe = Pipe(pipeX, self.pipeWidth, pipeHeight, self.pipeGap)
            pipeList.append(pipe)
        return pipeList

    def resetApp(self):
        self.multiplayer = False 
        self.bird2 = None
        self.pipes2 = []
        self.gameOver = False
        self.score = 0
        self.paused = True
        self.startScreen = True
        self.lives = 3
        self.bird.birdY = self.height // 4
        self.bird.dy = 0
        self.pipes = self.createPipes(self.height // 2)

    def isCollision(self, bird, pipes):
        birdLeft = bird.birdX - bird.birdWidth / 2
        birdRight = bird.birdX + bird.birdWidth / 2
        birdTop = bird.birdY - bird.birdHeight / 2
        birdBottom = bird.birdY + bird.birdHeight / 2

        for pipe in pipes:
            cx = pipe.pipeX
            h = pipe.pipeHeight
            w = pipe.pipeWidth
            gap = pipe.pipeGap

            if (birdRight > cx and birdLeft < cx + w and birdBottom > 0 and birdTop < h): 
                return True
            if (birdRight > cx and birdLeft < cx + w and birdBottom > h + gap):
                return True
        return False

    def update(self): 
        self.bird.gravityMove(2)
        self.bird.updatePosition()

        for pipe in self.pipes:
            pipe.pipeMove(self.dx)
            if pipe.pipeX + pipe.pipeSize <= 0:
                lastPipe = max(self.pipes, key=lambda p: p.pipeX)
                pipe.pipeX = lastPipe.pipeX + 300
                pipe.pipeHeight = random.randint(50, max(100, self.height // 2 - self.pipeGap - 100))
                pipe.scored = False

        if self.collisionCooldown > 0:
            self.collisionCooldown -= 1

        if self.isCollision(self.bird, self.pipes):
            if self.collisionCooldown == 0:
                self.lives -= 1
                self.collisionCooldown = 20

        if ((self.bird.birdY + self.bird.birdHeight >= self.height // 2) or 
            (self.bird.birdY - self.bird.birdHeight <= 0)):
            if self.collisionCooldown == 0:
                self.lives -= 1
                self.collisionCooldown = 20

        if self.lives <= 0:
            self.gameOver = True
            self.paused = True

        for pipe in self.pipes:
            pipeMid = pipe.pipeX + pipe.pipeWidth / 2
            birdMid = self.bird.birdX
            if not pipe.scored and birdMid > pipeMid:
                self.score += 1
                pipe.scored = True

        if self.multiplayer and self.bird2:
            self.bird2.gravityMove(2)
            self.bird2.updatePosition()

            for pipe in self.pipes2:
                pipe.pipeMove(self.dx)
                if pipe.pipeX + pipe.pipeSize <= 0:
                    lastPipe = max(self.pipes2, key=lambda p: p.pipeX)
                    pipe.pipeX = lastPipe.pipeX + 300
                    pipe.pipeHeight = random.randint(50, max(100, self.height // 2 - self.pipeGap - 100))
                    pipe.scored = False

def onAppStart(app):
    app.game = Game()
    app.stepsPerSecond = 20
    app.width = 800
    app.height = 650

def redrawAll(app):
    drawImage('candy background.jpg', app.width // 2, app.height // 2, 
              align='center', width=app.width, height=app.height)

    if app.game.multiplayer:
        drawLine(0, app.height // 2, app.width, app.height // 2, fill='black', lineWidth=4)

    if app.game.multiplayer and app.game.bird2:
        for pipe in app.game.pipes2:
            cx = pipe.pipeX
            h = pipe.pipeHeight
            gap = pipe.pipeGap
            size = pipe.pipeSize
            bottomY = h + gap
            bottomH = app.height // 2 - bottomY
            topY = app.height // 2
            bottomPipeY = topY + h
            bottomHeight = app.height - (bottomPipeY + gap)

            drawRect(cx, topY, size, h, fill='lightBlue', border='black', borderWidth=2)
            drawRect(cx - 5, topY + h - 2, size + 10, 30, fill='lightBlue', border='black', borderWidth=2)
            if bottomHeight > 0:
                drawRect(cx, bottomPipeY + gap, size, bottomHeight, fill='lightBlue', border='black', borderWidth=2)
                drawRect(cx - 5, bottomPipeY + gap, size + 10, 30, fill='lightBlue', border='black', borderWidth=2)
            drawRect(cx, 0, size, h, fill=pipe.pipeColor, border='black', borderWidth=2)
            drawRect(cx - 5, h - 2, size + 10, 30, fill=pipe.pipeColor, border='black', borderWidth=2)
            if bottomH > 0:
                drawRect(cx, bottomY, size, bottomH, fill=pipe.pipeColor, border='black', borderWidth=2)
                drawRect(cx - 5, bottomY, size + 10, 30, fill=pipe.pipeColor, border='black', borderWidth=2)

        drawImage('flapping_bird_fixed-removebg-preview (2).png', app.game.bird.birdX,
                  app.game.bird.birdY, align='center', width=app.game.bird.birdWidth, 
                  height=app.game.bird.birdHeight)

        drawImage('flapping_bird_fixed-removebg-preview (2).png', app.game.bird2.birdX,
                  app.game.bird2.birdY, align='center', width=app.game.bird2.birdWidth, 
                  height=app.game.bird2.birdHeight)
    else:
        for pipe in app.game.pipes:
            cx = pipe.pipeX
            h = pipe.pipeHeight
            gap = pipe.pipeGap
            size = pipe.pipeSize
            bottomY = h + gap
            bottomHeight = app.game.height - bottomY

            if h > 0:
                drawRect(cx, 0, size, h, fill=pipe.pipeColor, border='black', borderWidth=3)
                drawRect(cx - 5, h - 2, size + 10, 30, fill=pipe.pipeColor, border='black', borderWidth=3)

            if bottomHeight > 0:
                drawRect(cx, bottomY, size, bottomHeight, fill=pipe.pipeColor, border='black', borderWidth=3)
                drawRect(cx - 5, bottomY, size + 10, 30, fill=pipe.pipeColor, border='black', borderWidth=3)

        drawImage('flapping_bird_fixed-removebg-preview (2).png', app.game.bird.birdX,
                  app.game.bird.birdY, align='center', width=app.game.bird.birdWidth, 
                  height=app.game.bird.birdHeight)

    if app.game.startScreen:
        drawLabel('FlappyBird112!', app.game.width // 2, 75, font='fantasy', size=50, bold=True)
        drawLabel('press any key to start', app.game.width // 2, app.game.height * 3/4, font='orbitron', size=20)
        drawLabel('press M for multiplayer', app.game.width // 2, app.game.height * 3/4 + 40, font='orbitron', size=18)
    else:
        drawLabel(f'{app.game.score}', app.width // 2, 50, size=40, fill='black')
        for i in range(app.game.lives):
            drawImage('pixel_heart-removebg-preview.png', 10 + 50 * i, 15, width=50, height=50)

    if app.game.gameOver:
        drawLabel('GAME OVER', app.game.width // 2, app.game.height // 2, size=30, fill='red')
        drawLabel('Press r to restart!', app.game.width // 2, (app.game.height // 2) + 100, size=20, fill='black', bold=True)

def onKeyPress(app, key):
    if app.game.startScreen:
        if key == 'm':
            app.game.multiplayer = True
            app.game.startScreen = False
            app.game.paused = False
            app.game.bird2 = Bird(200, 3 * app.height // 4, app.width // 15, app.height // 15)
            app.game.pipes2 = app.game.createPipes(app.height // 2)
        else:
            app.game.startScreen = False
            app.game.paused = False
    elif key == 'r' and app.game.gameOver:
        app.game.resetApp()
    elif key == 'space' and not app.game.paused:
        app.game.bird.flap(12)
    elif key == 'w' and app.game.multiplayer and app.game.bird2:
        app.game.bird2.flap(12)

def onStep(app):
    if not app.game.paused:
        app.game.update()

runApp()
