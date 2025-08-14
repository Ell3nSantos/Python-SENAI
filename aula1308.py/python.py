import pygame
import sys


pygame.init()


WIDTH  = 500
LENGTH = 400



tela = pygame.display.set_mode((WIDTH, LENGTH))
pygame.display.set_caption('Teste')


#loop da página 


run =  True


while run:
    for event in pygame.event.get():


        if event.type == pygame.QUIT:
           run = False
           pygame.quit()
           sys.exit() 
        
        cor =  (240,230,140)
        tela.fill(cor)       
        pygame.draw.circle(tela, ('red'), (250,200), 50)
        pygame.draw.circle(tela, ('black'), (150,150), 20)
        pygame.draw.ellipse (tela, (255,0,0), (50,50,150,90))
        pygame.draw.rect (tela,(#0000), )

        # APLICAR UM 
        # RETANGULO ** 
        # ELIPSE ** 
        # DOCUMENTAÇÃO 
        # PESQUISA       


        pygame.display.flip()
        