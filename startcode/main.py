from pygame.display import update

import breakout_module
import pygame
import sys

from startcode.breakout_module import *

#variabelen
venster_breedte = 590
venster_hoogte = 480
bal_positie = [venster_breedte/2, venster_hoogte/2]
bal_grootte = 10
blok_breedte = 60
blok_hoogte = 20
blok_rijen = 5
blok_kolommen = venster_breedte//(blok_breedte + 5)
peddel_positie = [venster_breedte/2, venster_hoogte - 20]
peddel_breedte = 60
peddel_hoogte = 10
peddel_snelheid = 5
klok = pygame.time.Clock()
spel_voorbij = False

venster = setup_venster(venster_breedte,venster_hoogte)
bal_snelheid = initialiseer_bal()
blokken = initialiseer_blokken(blok_rijen, blok_kolommen, blok_breedte, blok_hoogte)
wit = (255, 255, 255)
zwart = (0, 0, 0)

def teken_spell():
    venster.fill(zwart)
    pygame.draw.rect(venster, wit,
                     (peddel_positie[0] - (peddel_breedte//2), peddel_positie[1], peddel_breedte, peddel_hoogte))
    pygame.draw.circle(venster, wit, bal_positie, bal_grootte)
    for blok in blokken:
        pygame.draw.rect(venster, wit, blok)

    pygame.display.update()

links = pygame.key.get_pressed()

#def beweeg_pebbel():


while spel_voorbij is False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    bal_positie, bal_snelheid = update_bal()
    teken_spell()

    klok.tick(60)