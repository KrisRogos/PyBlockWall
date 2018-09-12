import os

import pygame


class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self.size = self.weight, self.height = 720, 1280

    def on_init(self):
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0, 30) # window origin
        pygame.init() # start the pygame engine
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE) # window, sized to 720x1280 by default
        pygame.display.set_caption("PyBlockWall") # window title
        self.clock = pygame.time.Clock()  # engine clock
        self._running = True # game state


        self._image_surf = pygame.image.load(os.path.join("res", "blockBackground64.png")).convert()

    def on_event(self, event): # event handler
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self): # game logic per frame
        pass

    def on_render(self): # render logic per frame
        self._display_surf.blit(self._image_surf, (0, 0))
        pygame.display.flip() # render the frame

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
                print(event)
            self.on_loop()
            self.on_render()
            self.clock.tick(60)

        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()