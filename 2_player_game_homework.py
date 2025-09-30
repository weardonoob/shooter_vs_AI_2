import pygame, pyautogui, time, random, os
pygame.font.init()
pygame.mixer.init()
WIDTH, HEIGHT = pyautogui.size()
TITLE = "warzone"
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("warzone")
sw = WIDTH / 15
sh = HEIGHT / 15
bg = pygame.transform.scale(pygame.image.load("space_background.png"), (WIDTH,HEIGHT))
ship1 = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("millenium_falcon.png"), (sw,sh)),-90)
ship2 = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("x-wing.png"), (sw,sh)),90)
border = pygame.Rect(WIDTH / 2 - (WIDTH / 60), 0,WIDTH /30 , HEIGHT)
def draw(red, yellow, bullets_y, bullets_r):
    screen.blit(bg, (0,0))
    pygame.draw.rect(screen,"black", border)
    screen.blit(ship1, (yellow.x, yellow.y))
    screen.blit(ship2, (red.x, red.y))
    for i in bullets_y:
        pygame.draw.rect(screen, (0, 64, 255), i)
    for i in bullets_r:
        pygame.draw.rect(screen, "red",i)

    pygame.display.update()
def move_bullets(bullets_y, yellow, bullets_r,red):
    for i in bullets_y:
        i.x += 10
    for i in bullets_r:
        i.x -= 10


def handle_player(key_pressed,yellow):
    if key_pressed[pygame.K_w] and yellow.y > 0:
        yellow.y -= 10
    if key_pressed[pygame.K_s] and yellow.y + yellow.height < HEIGHT:
        yellow.y += 10
    if key_pressed[pygame.K_a] and yellow.x > 0:
        yellow.x -= 10
    if key_pressed[pygame.K_d] and yellow.x + yellow.width < border.x:
        yellow.x += 10

def move_ai(red):
    #red.x = random.randint(border.x+border.width,WIDTH)
    #red.y = random.randint(0,HEIGHT)
    if red.x > border.x + border.width + 50 and red.x + red.width < WIDTH - 50 and red.y > 50 and red.y + red.height < HEIGHT -50:
      red.x += random.randint(-50,50)
      red.y += random.randint(-50,50)
    else:
        red.x = WIDTH - 300
        red.y = HEIGHT / 2


def main():
    yellow = pygame.Rect(WIDTH/4, HEIGHT/2,sh,sw)
    red = pygame.Rect(WIDTH * (7/10), HEIGHT / 2,sh,sw)
    bullets_y = []
    bullets_r = []
    y_health,r_health = 3,3
    run = True
    while run:
       for event in pygame.event.get():
           #print(event)
           if event.type == pygame.QUIT:
               pygame.quit()
           if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_e and len(bullets_y)<21:
                   bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height / 2, 20,10) 
                   bullets_y.append(bullet)  
       key_pressed = pygame.key.get_pressed()
       handle_player(key_pressed,yellow)
       if random.randint(1,50) < 10:
          print("moving")
          move_ai(red)
       if random.randint(1,50) < 5 and len(bullets_r) < 21 :
         bullet = pygame.Rect(red.x , red.y + red.height / 2, 20,10) 
         bullets_r.append(bullet) 
       draw(red, yellow, bullets_y, bullets_r)
       move_bullets(bullets_y, yellow, bullets_r,red)

main()



