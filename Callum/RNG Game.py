import pygame
pygame.init()

clock = pygame.time.Clock()
start_ticks = pygame.time.get_ticks()

WINDOW_SIZE = (800, 600)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("RNG Game")

sound = pygame.mixer.Sound("glitch.mp3")
glitch = 0

BG_COLOR = (204, 41, 27)

wpop = 0
home = 1
lpds = 0
abcd = 0
gdps = 0
wiiu = 0
snkw = 0
dkwu = 0
running = True
common = 0
uncommon = 0
rare = 0
epic = 0
legendary = 0
mythic = 0
divine = 0
godlike = 0
impossible = 0
luck = 0
rolls = 0
status_message = ""
while running == True:
    mouse_pos = pygame.mouse.get_pos()
    click = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            click = True
            print("Mouse clicked at:", mouse_pos[0], mouse_pos[1])

    if glitch == 0 :
        elapsed_seconds = (pygame.time.get_ticks() - start_ticks) // 1000
        timevar3 = elapsed_seconds
        hours = elapsed_seconds // 3600
        minutes = (elapsed_seconds % 3600) // 60
        seconds = elapsed_seconds % 60
        time_text = f"Time {hours:02d}:{minutes:02d}:{seconds:02d}"
    if glitch == 1:
        elapsed_seconds = (pygame.time.get_ticks() - start_ticks) // 1000 - 1
        timevar2 = elapsed_seconds - 11
        hours = elapsed_seconds // 3600
        minutes = (elapsed_seconds % 3600) // 60
        seconds = elapsed_seconds % 60
        time_text = f"Time {hours:02d}:{minutes:02d}:{seconds:02d}"

    if click and home == 1 and 370 < mouse_pos[0] < 490 and 0 < mouse_pos[1] < 50:
        print("You clicked the shop button!")
        snkw = 1
        gdps = 1
        lpds = 1
        home = 2
        dkwu = 1
        status_message = ""

    if click and home == 2 and 390 < mouse_pos[0] < 585 and 135 < mouse_pos[1] < 180:
        print("You clicked the RNG Upgrades Button!")
        status_message = "RNG upgrades are currently at Lvl 0. Upgrading luck needs a divine roll."
        lpds = 0
        wpop = 1
    
    if click and wpop == 1 and 5 < mouse_pos[0] < 785 and 30 < mouse_pos[1] < 105:
        print("You clicked upgrade!")
        if divine == 0:
            status_message = "You have not met the requirements."
        if divine > 0:
            status_message = "Luck upgraded!"
            luck = 1

    if click and home == 2 and 400 < mouse_pos[0] < 590 and 450 < mouse_pos[1] < 490:
        print("You clicked Leave shop")
        status_message = "You have left the shop."
        snkw = 0
        gdps = 0
        home = 1

    if click and home == 1 and 390 < mouse_pos[0] < 485 and 130 < mouse_pos[1] < 180:
        print("You viewed stats")
        status_message = "Welcome to RNG Game Statistics!"
        home = 3

    if click and home == 3 and 390 < mouse_pos[0] < 485 and 290 < mouse_pos[1] < 330:
        print("You left stats")
        status_message = "You have left statistics"
        home = 1

    if click and home == 1 and 285 < mouse_pos[0] < 555 and 280 < mouse_pos[1] < 350:
        print("You clicked the roll button!")
        dkwu = 1
        import random
        returned = random.randint(1, 2)
        if luck == 0:
            if returned == 1:
                abcd = 1
                common += 1
                rolls += 1
                status_message = "You got common! (1 in 2)"
            else:
                returned = random.randint(1, 2)
                if returned == 1:
                    uncommon += 1
                    rolls += 1
                    status_message = "You got uncommon! (1 in 4)"
                else:
                    returned = random.randint(1, 2)
                    if returned == 1:
                        rare += 1
                        rolls += 1
                        status_message = "You got rare! (1 in 8)"
                    else:
                        returned = random.randint(1, 2)
                        if returned == 1:
                            epic += 1
                            rolls += 1
                            status_message = "You got epic! (1 in 16)"
                        else:
                            returned = random.randint(1, 2)
                            if returned == 1:
                                legendary += 1
                                rolls += 1
                                status_message = "You got legendary! (1 in 32)"
                            else:
                                returned = random.randint(1, 2)
                                if returned == 1:
                                    mythic += 1
                                    rolls += 1
                                    status_message = "You got mythic! (1 in 64)"
                                else:
                                    returned = random.randint(1, 2)
                                    if returned == 1:
                                        divine += 1
                                        rolls += 1
                                        status_message = "You got divine! (1 in 128)"
                                    else:
                                        if godlike == 0:
                                            godlike += 1
                                            rolls += 1
                                            status_message = "You got godlike! (1 in 256)"
                                        else:
                                            returned = random.randint(1, 2)
                                            if returned == 1:
                                                godlike += 1
                                                rolls += 1
                                                status_message = "You got godlike! (1 in 256)"
                                            else:
                                                impossible += 1
                                                rolls += 1
                                                status_message = "??? ??? ???????? ?? ?? ????"
                                                glitch = 1
        else:
            if returned == 1:
                rare += 1
                rolls += 1
                status_message = "You got rare! (1 in 8)"
            else:
                returned = random.randint(1, 2)
                if returned == 1:
                    epic += 1
                    rolls += 1
                    status_message = "You got epic! (1 in 16)"
                else:
                    returned = random.randint(1, 2)
                    if returned == 1:
                        legendary += 1
                        rolls += 1
                        status_message = "You got legendary! (1 in 32)"
                    else:
                        returned = random.randint(1, 2)
                        if returned == 1:
                            mythic += 1
                            rolls += 1
                            status_message = "You got mythic! (1 in 64)"
                        else:
                            returned = random.randint(1, 2)
                            if returned == 1:
                                divine += 1
                                rolls += 1
                                status_message = "You got divine! (1 in 128)"
                            else:
                                if godlike == 0:
                                    godlike += 1
                                    rolls += 1
                                    status_message = "You got godlike! (1 in 256)"
                                else:
                                    returned = random.randint(1, 2)
                                    if returned == 1:
                                        godlike += 1
                                        rolls += 1
                                        status_message = "You got godlike! (1 in 256)"
                                    else:
                                        impossible += 1
                                        rolls += 1
                                        status_message = "??? ??? ???????? ?? ?? ????"
                                        timevar = elapsed_seconds
                                        timevar2 = timevar3
                                        glitch = 1
                                        if timevar == elapsed_seconds:
                                            print("Stage 1")
                                            BG_COLOR = (0, 0, 0)
                                        if timevar2 == timevar3:
                                            print("Stage 2")
                                            sound.play()


                                            


    screen.fill(BG_COLOR)
    font = pygame.font.Font(None, 36)
    if home == 1 and glitch == 0:
        text = font.render("Welcome to the RNG game!", True, (255, 255, 255))
        screen.blit(text, (10, 10))
        text = font.render("SHOP", True, (255, 255, 255))
        screen.blit(text, (400, 0))
        text = font.render("ROLL", True, (255, 255, 255))
        screen.blit(text, (400, 300))
        text = font.render("STATS", True, (255, 255, 255))
        screen.blit(text, (400, 150))
    elif home == 2 and glitch == 0:
        text = font.render("RNG Upgrades", True, (255, 255, 255))
        screen.blit(text, (400, 150))
        text = font.render("Leave shop", True, (255, 255, 255))
        screen.blit(text, (400, 450))
        if lpds == 1:
            text = font.render("Welcome to the shop!", True, (255, 255, 255))
            screen.blit(text, (400, 0))
    elif home == 3 and glitch == 0:
        if common > 0:
            text = font.render("Common: " + str(common), True, (255, 255, 255))
            screen.blit(text, (400, 0))
        else:
            text = font.render("???", True, (255, 255, 255))
            screen.blit(text, (400, 0))
        if uncommon > 0:    
            text = font.render("Uncommon: " + str(uncommon), True, (255, 255, 255))
            screen.blit(text, (400, 20))
        else:
            text = font.render("???", True, (255, 255, 255))
            screen.blit(text, (400, 20))
        if rare > 0:    
            text = font.render("Rare: " + str(rare), True, (255, 255, 255))
            screen.blit(text, (400, 40))
        else:
            text = font.render("???", True, (255, 255, 255))
            screen.blit(text, (400, 40))
        if epic > 0:    
            text = font.render("Epic: " + str(epic), True, (255, 255, 255))
            screen.blit(text, (400, 60))
        else: 
            text = font.render("???", True, (255, 255, 255))
            screen.blit(text, (400, 60))
        if legendary > 0:    
            text = font.render("Legendary: " + str(legendary), True, (255, 255, 255))
            screen.blit(text, (400, 80))
        else:
            text = font.render("???", True, (255, 255, 255))
            screen.blit(text, (400, 80))
        if mythic > 0:    
            text = font.render("Mythic: " + str(mythic), True, (255, 255, 255))
            screen.blit(text, (400, 100))
        else:
            text = font.render("???", True, (255, 255, 255))
            screen.blit(text, (400, 100))
        if divine > 0:    
            text = font.render("Divine: " + str(divine), True, (255, 255, 255))
            screen.blit(text, (400, 120))
        else:
            text = font.render("???", True, (255, 255, 255))
            screen.blit(text, (400, 120))
        if godlike > 0:    
            text = font.render("Godlike: " + str(godlike), True, (255, 255, 255))
            screen.blit(text, (400, 140))
        else:
            text = font.render("???", True, (255, 255, 255))
            screen.blit(text, (400, 140))
        if impossible > 0:
            text = font.render("Impossible: " + str(impossible), True, (255, 255, 255))
            screen.blit(text, (400, 160))
        else:
            text = font.render("Coming soon!", True, (255, 255, 255))
            screen.blit(text, (400, 160))
        text = font.render("Leave", True, (255, 255, 255))
        screen.blit(text, (400, 300))
    elif home == 1 and glitch == 1:
        text = font.render("????", True, (255, 255, 255))
        screen.blit(text, (400, 0))
        text = font.render("????", True, (255, 255, 255))
        screen.blit(text, (400, 300))
        text = font.render("?????", True, (255, 255, 255))
        screen.blit(text, (400, 150))
    if status_message:
        text = font.render(status_message, True, (255, 255, 255))
        screen.blit(text, (10, 50))

    time_surface = font.render(time_text, True, (255, 255, 255))
    screen.blit(time_surface, (10, 560))

    pygame.display.flip()