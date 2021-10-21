import pygame

import Button
import Enemy

pygame.init()

height = 1400
weight = 900
image = pygame.image.load("media/wojna.jpg")
exit_button = Button.Button(619, 500, "media/button_exit")
play_button = Button.Button(619, 400, "media/button_graj")
next_button = Button.Button(619, 800, "media/button_next")
text_menu = pygame.image.load("media/Kill_hitler.png")
screen = pygame.display.set_mode((height, weight))
pygame.display.set_caption("Kill Hitler")
icon = pygame.image.load("media/icon.jpg")
pygame.display.set_icon(icon)
pygame.display.flip()

keys = pygame.key.get_pressed()


def game_run():
    i = 1
    time = 0
    pygame.mixer.music.load("media/Mortal_Kombat.mp3")
    pygame.mixer.music.play(-1)
    predkosc = 5
    score = 0
    clock = 0
    run = True
    enemas = []
    while run:
        time += pygame.time.Clock().tick(60) / 1000  # czas gry
        clock += pygame.time.Clock().tick(60) / 1000  # czas obliczajacy klatki i czestotliwosc pojawienia sie wroga
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        screen.blit(image, (0, 0))
        if clock >= 1:  # jesli zegar jest wiekszy od jeden stworz wroga
            enemas.append(Enemy.Enemy())  # Tworznie wroga
            clock = 0  # wyzeruj zegar

        for ene in enemas:
            ene.draw(screen)  # narysuj wroga
            if ene.hitbox.collidepoint(ene.x_cord, 1100):
                game_over(score)
                pygame.mixer.music.stop()
                run = False
        for ene in enemas:
            ene.tick_enemy(predkosc)  # poruszaj wrogiem
        for ene in enemas:
            if ene.hitbox.collidepoint(pygame.mouse.get_pos()):  # sprawdz czy gracz nacisnal na wroga
                if pygame.mouse.get_pressed()[0]:
                    enemas.remove(ene)
                    score += 1
                    predkosc += 1

        score_image = pygame.font.Font.render(pygame.font.SysFont("arial", 50), str(f"Wynik :{round(score, 0)}"), True,
                                              (0, 0, 0, 0))
        time_image = pygame.font.Font.render(pygame.font.SysFont("arial", 50), str(f"Czas :{round(time, None)}"), True,
                                             (252, 202, 3, 0))

        screen.blit(score_image, (0, 0))
        screen.blit(time_image, (1200, 0))

        pygame.display.update()


def main():
    run = True

    pygame.mixer.music.load("media/German.mp3")
    pygame.mixer.music.play(-1)
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        screen.blit(image, (0, 0))
        screen.blit(text_menu, (250, 0))
        exit_button.draw_button_play(screen)
        play_button.draw_button_play(screen)
        if play_button.tick():
            game_run()
        if exit_button.tick():
            run = False
        pygame.display.update()


def game_over(score):
    run = True

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif exit_button.hitbox.collidepoint(pygame.mouse.get_pos()):
                if pygame.mouse.get_pressed()[0]:
                    run = False
        end_score_image = pygame.font.Font.render(pygame.font.SysFont("arial", 70),
                                                  str(f"Twój Wynik :{round(score, 0)}"), True,
                                                  (0, 0, 0, 0))

        screen.blit(image, (0, 0))
        screen.blit(text_menu, (250, 0))
        screen.blit(end_score_image, (500, 600))

        next_button.draw_button_play(screen)
        if next_button.tick():
            main()
            run = False
        pygame.display.update()


if __name__ == "__main__":
    main()
