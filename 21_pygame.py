import pygame
import random

loga_platums = 1280
loga_augstums = 768

# nevar double down uz split
# neradas J Q K A tā vietā r vnk vērtība 10
# toties strada, ka A ir 11 un 1

menuColor = (136, 29, 78)
isMenu = True
FadeMenu = False
fade_surface = pygame.Surface((loga_platums, loga_augstums))
fade_surface.fill((0, 0, 0))
fade_surface.set_alpha(0) 
fade_alpha_value = 0

dileris_summa=0
tava_summa=0
split_summa=0
nauda=500
kartis=[0,1,2,3,4,5,6,7,8,9,10,10,10,10,11]

pygame.init()
ekrans = pygame.display.set_mode((loga_platums, loga_augstums))
pygame.display.set_caption("BlackJack")
clock = pygame.time.Clock()
running = True
dt = 0

logoImg = pygame.image.load('logo.png')
logo_rect = logoImg.get_rect()
logo_rect.centerx = ekrans.get_rect().centerx
logo_rect.centery = -ekrans.get_rect().centery / 2
speed = 250
stop = False

fonts = pygame.font.SysFont("comicsansms", 52)
play_text = fonts.render("Press any button to play", True, "black")
play_text_x = (ekrans.get_width() / 2) - (play_text.get_width() // 2)
play_text_y = ((ekrans.get_height() / 2) * 1.5) - (play_text.get_height() // 2) + ((ekrans.get_height() / 2) * 1.5) - (play_text.get_height() // 2)
fade_in = True
alpha = 0
alpha_change = 2.5

background_image = pygame.image.load('background.png')
background_image = pygame.transform.scale(background_image, (loga_platums, loga_augstums))

while running:
    
    # pygame.QUIT notikums nozīmē, ka lietotājs noklikšķināja uz X, lai aizvērtu logu
    for pasakums in pygame.event.get():
        if pasakums.type == pygame.QUIT:
            running = False
        elif pasakums.type == pygame.MOUSEBUTTONUP:
            pass
        elif pasakums.type == pygame.MOUSEBUTTONDOWN:
            if stop: FadeMenu = True
        elif pasakums.type == pygame.KEYDOWN:
            if stop: FadeMenu = True
    
    if isMenu:
    
        ekrans.fill(menuColor)

        # Update the alpha value
        if fade_in:
            alpha += alpha_change if alpha < 255 else 0
            fade_in = False if alpha >= 255 else True
        else:
            alpha -= alpha_change if alpha > 0 else 0
            fade_in = True if alpha <= 0 else False
            
        if not stop: 
            logo_reached = logo_rect.centery >= ekrans.get_rect().centery / 2
            play_text_reached = play_text_y <= ((ekrans.get_height() / 2) * 1.5) - (play_text.get_height() // 2)
            
            if not logo_reached:
                logo_rect.centery += speed * dt
            if not play_text_reached:
                play_text_y -= speed * dt
            
            if logo_reached and play_text_reached:
                stop = True
                
        play_text.set_alpha(alpha)

        ekrans.blit(logoImg, logo_rect)
        ekrans.blit(play_text, (play_text_x, play_text_y))
        
        if FadeMenu:
            fade_alpha_value += 5
            if fade_alpha_value > 255:
                fade_alpha_value = 255 
                isMenu = False
                FadeMenu = False
            fade_surface.set_alpha(fade_alpha_value)
            ekrans.blit(fade_surface, (0, 0))

    else: ekrans.blit(background_image, (0, 0))

    # flip() apgriezt displeju, lai parādītu savu darbu ekrānā
    pygame.display.flip()

    # Limitē FPS līdz 60
    # dt ir delta laiks sekundēs kopš pēdējā kadra, ko izmanto kadru ātrumam
    # Neatkarīga fizika
    dt = clock.tick(60) / 1000
    # pygame.time.Clock().tick(60)

pygame.quit()