import sys
import pygame
import random

WIDTH, HEIGHT = 640, 480
FPS = 60


def main() -> None:
  pygame.init()
  screen = pygame.display.set_mode((WIDTH, HEIGHT))
  pygame.display.set_caption("Blank Window")
  clock = pygame.time.Clock()
  font = pygame.font.SysFont(None, 36)

  running = True
  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

      if event.key == pygame.K_SPACE:
          if mode == "press":
              result = "60sec"
          else:
              result = "game over"
      elif event.key == pygame.K_r:
          mode = "wait"
      elif event.key == pygame.k_e:
          mode = "exit"
          running = False


    running = True
    mode = "wait"
    screen.fill((30, 32, 40))
    screen.blit(font.render("WAIT!", True, (255, 255, 255)), (280, 185))
    pygame.display.flip()
    clock.tick(FPS)

    if random.randint(0, 100) == 0:
        mode = "press"
    if mode == "press":
        screen.blit(font.render("PRESS BUTTON", True, (255, 255, 255)), (260, 200))
    else:
        screen.blit(font.render("WAIT", True, (255, 255, 255)), (260, 200))
  pygame.quit()
  sys.exit()


if __name__ == "__main__":
  main()