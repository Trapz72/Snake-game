import pygame, random

pygame.init()

blue=(0,0,255)
red=(255,0,0)
black=(0,0,0)

dis_width=800
dis_height=600

block=10
snake_speed=30

dis=pygame.display.set_mode((dis_width,dis_height))
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont(None, 35)
clock = pygame.time.Clock()

def score(score):
  value= score_font.render("Score: " + str(score), True, red)
  dis.blit(value, [0,0])

def snake(block, snake_list):
  for x in snake_list:
    pygame.draw.rect(dis, blue, [x[0], x[1], block, block])
 
def message(msg,color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [0,0])

def game():

  game_over=False
  game_replay=False
  x1=dis_width/2
  y1=dis_height/2
  x1_change = 0       
  y1_change = 0
  snake_list=[]
  snake_length=1

  foodx= round(random.randint(0, dis_width - block) / 10.0) * 10.0
  foody= round(random.randint(0, dis_height - block) / 10.0) * 10.0

  while not game_over:

      while game_replay:

        dis.fill(black)
        message("Q-Quit             C-Play Again", red)
        pygame.display.update()

        for event in pygame.event.get():
          if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_q:
              game_over=True
              game_replay=False
            if event.key == pygame.K_c:
              game()

      for event in pygame.event.get():
          if event.type==pygame.QUIT:
            game_over=True
          if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_a:
                  x1_change = -block
                  y1_change = 0
              elif event.key == pygame.K_d:
                  x1_change = block
                  y1_change = 0
              elif event.key == pygame.K_w:
                  x1_change = 0
                  y1_change = -block
              elif event.key == pygame.K_s:
                  x1_change = 0
                  y1_change = block

      if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
        game_replay = True

      x1 += x1_change
      y1 += y1_change
      dis.fill(black)

      pygame.draw.rect(dis,red,[foodx,foody,block,block])

      snake_head=[x1,y1]
      snake_list.append(snake_head)
      if len(snake_list) > snake_length:
        del snake_list[0]

      for x in snake_list[:-1]:
        if x == snake_head:
          game_replay = True

      snake(block, snake_list)
      score(snake_length-1)

      pygame.display.update()

      if x1 == foodx and y1 == foody:
        foodx= round(random.randint(0, dis_width - block) / 10.0) * 10.0
        foody= round(random.randint(0, dis_height - block) / 10.0) * 10.0
        snake_length += 1

      clock.tick(snake_speed)


  pygame.quit()
  quit()

game()