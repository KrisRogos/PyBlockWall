import os

import pygame


class Block:
    def __init__(self, x, y, img, bx, by):
        self.position = self.x, self.y = x, y
        self.velocity = self.vx, self.vy = 0, 0
        self.size = self.sx, self.sy = 64, 64
        self.bounds = self.bx, self.by = bx, by
        self.image = img

    def on_draw(self, dispaly):
        dispaly.blit(self.image, (self.x, self.y))

    def set_vx(self, x):
        self.vx = x
        self.velocity = self.vx, self.vy

    def set_vy(self, y):
        self.vy = y
        self.velocity = self.vx, self.vy

    def set_velocity(self, x, y):
        self.vx = x
        self.vy = y
        self.velocity = self.vx, self.vy

    def on_update(self, time):
        self.x += self.vx * time
        self.y += self.vy * time

        # make sure is in bounds
        if self.x < 0:
            self.x = 0
        if self.y < 0:
            self.y = 0
        if self.x > self.bx - self.sx:
            self.x = self.bx - self.sx
        if self.y > self.by - self.sy:
            self.y = self.by - self.sy

        self.position = self.x, self.y


class App:
    def __init__(self):
        self._running = True  # game state
        self._display_surf = None  # window
        self.clock = None  # game clock
        self.size = self.width, self.height = 720, 1280
        self.fps = 120

        self.myBlock = None

        # colour definitions
        self.colBlack = (0,0,0)
        self.colWhite = (255,255,255)
        self.colRed = (255,0,0)
        self.colGreen = (0,255,0)
        self.colBlue = (0,0,255)

        # key definitions
        self.keyUp = pygame.K_w
        self.keyLeft = pygame.K_a
        self.keyRight = pygame.K_d
        self.keyDown = pygame.K_s
        self.keyQuit = pygame.K_ESCAPE

    def on_init(self):
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0, 30)  # window origin
        pygame.init()  # start the pygame engine
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE)  # window, sized to 720x1280 by default
        pygame.display.set_caption("PyBlockWall")  # window title
        self.clock = pygame.time.Clock()  # engine clock
        self._running = True  # game state

        # create the car
        self.myBlock = Block(self.width / 2 - 32, 0, pygame.image.load(os.path.join("res", "blockBackground64.png")).convert(), self.width, self.height)

    def on_event(self, event):  # event handler
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == self.keyQuit:
                self._running = False
            elif event.key == self.keyUp:
                self.myBlock.set_vy(-1000)
                print("Speed up")
            elif event.key == self.keyDown:
                self.myBlock.set_vy(1000)
            elif event.key == self.keyLeft:
                self.myBlock.set_vx(-1000)
            elif event.key == self.keyRight:
                self.myBlock.set_vx(1000)

        elif event.type == pygame.KEYUP:
            if event.key == self.keyUp:
                self.myBlock.set_vy(0)
            elif event.key == self.keyDown:
                self.myBlock.set_vy(0)
            elif event.key == self.keyLeft:
                self.myBlock.set_vx(0)
            elif event.key == self.keyRight:
                self.myBlock.set_vx(0)

    def on_loop(self):  # game logic per frame
        self.myBlock.on_update(1/self.fps)

    def on_render(self):  # render logic per frame
        self._display_surf.fill(self.colWhite)
        self.myBlock.on_draw(self._display_surf)
        pygame.display.flip() # render the frame

    def on_cleanup(self):
        pygame.quit()
        quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
            self.clock.tick(self.fps) # fps

        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()