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
red_hit = pygame.USEREVENT + 1
yellow_hit = pygame.USEREVENT + 2
font_small = pygame.font.SysFont("calibrie", 40)
font_big = pygame.font.SysFont("calibrie", 80)
a = 0
direction = []
def draw(red, yellow, bullets_y, bullets_r,winner, y_health, r_health):
    screen.blit(bg, (0,0))
    pygame.draw.rect(screen,"black", border)
    screen.blit(ship1, (yellow.x, yellow.y))
    screen.blit(ship2, (red.x, red.y))
    for i in bullets_y:
        pygame.draw.rect(screen, "blue", i)
    for i in bullets_r:
        pygame.draw.rect(screen, "red",i)
    
   # pygame.draw.rect(screen,"red", red)
   # pygame.draw.rect(screen,"yellow", yellow)
    y_health_text = font_small.render("yellows hp ->" + str(y_health),True, "white")
    r_health_text = font_small.render("reds hp ->" + str(r_health),True, "white")
    screen.blit(y_health_text, (20,20))
    screen.blit(r_health_text,(WIDTH - 150, 20))
    if winner:
        winner_text = font_big.render("the winner is " + winner, True, "white" )
        screen.blit(winner_text,(WIDTH / 3,HEIGHT / 3))

    pygame.display.update()
def move_bullets(bullets_y, yellow, bullets_r,red):
    global a
    for i in bullets_y:
        i.x += 10
        if i.x > WIDTH:
            bullets_y.remove(i)
        for r in bullets_r:
            if i.colliderect(r):
                print("bullet_hit", a)
                a += 1
                bullets_r.remove(r)
                bullets_y.remove(i)
        if i.colliderect(red):
            bullets_y.remove(i)
            pygame.event.post(pygame.event.Event(red_hit))

    for i in bullets_r:
        i.x -= 10
        if i.x < 0:
            bullets_r.remove(i)
        if i.colliderect(yellow):
            bullets_r.remove(i)
            pygame.event.post(pygame.event.Event(yellow_hit))

def handle_player(key_pressed,yellow):
    global direction
    if key_pressed[pygame.K_w] and yellow.y > 0:
        yellow.y -= 10
        direction.append("up")
    if key_pressed[pygame.K_s] and yellow.y + yellow.height < HEIGHT:
        yellow.y += 10
        direction.append("down")
    if key_pressed[pygame.K_a] and yellow.x > 0:
        yellow.x -= 10
        direction.append("left")
    if key_pressed[pygame.K_d] and yellow.x + yellow.width < border.x:
        yellow.x += 10
        direction.append("up")

def move_ai(red):
    #red.x = random.randint(border.x+border.width,WIDTH)
    #red.y = random.randint(0,HEIGHT)
    if red.x > border.x + border.width + 50 and red.x + red.width < WIDTH - 50 and red.y > 50 and red.y + red.height < HEIGHT -50:
      # if direction(int(0),int(1)) == ["up", "up"]:
       #  print("working")
       
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
               if event.key == pygame.K_e:
                   bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height / 2, 20,10) 
                   bullets_y.append(bullet)  
           if event.type == red_hit:
               r_health -= 1
           if event.type == yellow_hit:
               y_health -= 1
       key_pressed = pygame.key.get_pressed()
       handle_player(key_pressed,yellow)
       winner = None
       if r_health <1:
           winner = "yellow"
       if y_health < 1:
           winner = "red"

       if random.randint(1,50) < 10:
          print("moving")
          move_ai(red)
       bullet = pygame.Rect(red.x , red.y + red.height / 2, 20,10) 
       bullets_r.append(bullet) 
       draw(red, yellow, bullets_y, bullets_r,winner, y_health, r_health)
       move_bullets(bullets_y, yellow, bullets_r,red)

main()




