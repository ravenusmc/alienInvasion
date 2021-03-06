import pygame

class Tank():

  def __init__(self, screen):
    #init the ship and set its starting position.
    self.screen = screen

    #Load the ship image and gets its rect.
    self.image = pygame.image.load('image/tank.bmp').convert()
    self.rect = self.image.get_rect()
    self.screen_rect = screen.get_rect()

    #start each new ship at the bottom center of the screen
    self.rect.centerx = self.screen_rect.centerx
    self.rect.bottom = self.screen_rect.bottom

  def blitme(self):
    #Draw the ship at its current location
    self.screen.blit(self.image, self.rect)

