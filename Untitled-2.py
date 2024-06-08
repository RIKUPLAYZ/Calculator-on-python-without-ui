import pygame
import sys

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (200, 200, 200)

# Define font size
FONT_SIZE = 32

# Define screen dimensions
WIDTH = 400
HEIGHT = 500

# Define button size and margin
BUTTON_SIZE = (100, 50)
BUTTON_MARGIN = 10


def draw_text(text, font, color, surface, x, y):
  """
  Function to draw text on the surface
  """
  text_obj = font.render(text, 1, color)
  text_rect = text_obj.get_rect(topleft=(x, y))
  surface.blit(text_obj, text_rect)


def draw_button(text, font, color, surface, x, y):
  """
  Function to draw a button on the surface
  """
  pygame.draw.rect(surface, color, (x, y, BUTTON_SIZE[0], BUTTON_SIZE[1]))
  draw_text(text, font, BLACK, surface, x + BUTTON_SIZE[0] // 3, y + BUTTON_SIZE[1] // 3)


def check_button_click(mouse_pos, buttons):
  """
  Function to check if a button is clicked
  """
  for button in buttons:
    x, y = button[0]
    width, height = button[1]
    if mouse_pos[0] > x and mouse_pos[0] < x + width and mouse_pos[1] > y and mouse_pos[1] < y + height:
      return button[2]  # Return the button action
  return None  # No button clicked


def main():
  pygame.init()
  screen = pygame.display.set_mode((WIDTH, HEIGHT))
  pygame.display.set_caption("Calculator")
  font = pygame.font.SysFont(None, FONT_SIZE)

  # Define button positions
  button_positions = [
      (BUTTON_MARGIN, HEIGHT - BUTTON_MARGIN - BUTTON_SIZE[1]),
      (BUTTON_MARGIN + BUTTON_SIZE[0] + BUTTON_MARGIN, HEIGHT - BUTTON_MARGIN - BUTTON_SIZE[1]),
      (2 * BUTTON_MARGIN + 2 * BUTTON_SIZE[0], HEIGHT - BUTTON_MARGIN - BUTTON_SIZE[1]),
      (BUTTON_MARGIN, HEIGHT - 2 * BUTTON_MARGIN - 2 * BUTTON_SIZE[1]),
      (BUTTON_MARGIN + BUTTON_SIZE[0] + BUTTON_MARGIN, HEIGHT - 2 * BUTTON_MARGIN - 2 * BUTTON_SIZE[1]),
      (2 * BUTTON_MARGIN + 2 * BUTTON_SIZE[0], HEIGHT - 2 * BUTTON_MARGIN - 2 * BUTTON_SIZE[1]),
      (BUTTON_MARGIN, HEIGHT - 3 * BUTTON_MARGIN - 3 * BUTTON_SIZE[1]),
      (BUTTON_MARGIN + BUTTON_SIZE[0] + BUTTON_MARGIN, HEIGHT - 3 * BUTTON_MARGIN - 3 * BUTTON_SIZE[1]),
      (2 * BUTTON_MARGIN + 2 * BUTTON_SIZE[0], HEIGHT - 3 * BUTTON_MARGIN - 3 * BUTTON_SIZE[1]),
      (WIDTH - BUTTON_SIZE[0] - BUTTON_MARGIN, HEIGHT - 3 * BUTTON_MARGIN - 3 * BUTTON_SIZE[1]),
  ]

  # Define button labels and actions
  button_labels = ["7", "8", "9", "/", "4", "5", "6", "*", "1", "2", "3", "-"]
  button_actions = button_labels  # Default action is the button label
  button_actions.append("=")  # Add equals action for the last button


  # Define variables for calculation
  first_number = None
  second_number = None
  operation = None
  display_text = ("youtad")


  running = True
  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
      elif event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = pygame.mouse.get_pos()
        clicked_button = check_button_click(mouse_pos, button)