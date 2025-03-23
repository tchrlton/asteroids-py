import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()
  dt = 0
  
  print("Starting Asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")
  
  shots = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  
  Player.containers = (updatable, drawable)
  Asteroid.containers = (asteroids, updatable, drawable)
  AsteroidField.containers = (updatable)
  Shot.containers = (shots, updatable, drawable)
  
  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
  asteroidField = AsteroidField()
  
  while True:
    for event in pygame.event.get():
      
      if event.type == pygame.QUIT:
        
          return
      
    screen.fill("black")
    
    for item in drawable:
      item.draw(screen)
    
    pygame.display.flip()
    dt = clock.tick(60) / 1000
    
    updatable.update(dt)
    
    for asteroid in asteroids:
      if asteroid.has_collided(player):
        sys.exit("Game Over!")
      else:
        for bullet in shots:
          if bullet.has_collided(asteroid):
            bullet.kill()
            asteroid.split()
    

if __name__ == "__main__":
    main()