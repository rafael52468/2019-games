import pygame

pygame.init()
#jogador
x = 0
y = 130

#nave1
pos_x = 305
pos_y = -325
#nave2
pos2_x = -290
pos2_y = -325
#nave3
pos3_x = 10
pos3_y = -325

timer = 0
timer2 = 0

velocidade = 15
velocidaden1 = 10
velocidaden2 = 10
velocidaden3 = 12
fundo = pygame.image.load('fundo_espaço7.png')
jogador = pygame.image.load('navenova.png')
nave1 = pygame.image.load('nave1.png')
nave2 = pygame.image.load('nave2.png')
nave3 = pygame.image.load('nave3.png')

font = pygame.font.SysFont('arkanoid',50)
texto = font.render("Score: ",True, (255,255,255), (0,0,0))
pos_texto = texto.get_rect()
pos_texto.center = (415,15)

janela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Trap")

janela_aberta = True
while janela_aberta:
    pygame.time.delay(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP] and (y >= -253):
        y -= velocidade
    if comandos[pygame.K_DOWN] and (y <= 190):
        y += velocidade
    if comandos[pygame.K_RIGHT] and (x <= 311):
        x += velocidade
    if comandos[pygame.K_LEFT] and (x >= -320):
        x -= velocidade

    if (pos_y >= 600):
        pos_y = -500
        if velocidaden1<70:
            velocidaden1 += 2.4
    if (pos2_y >= 600):
        pos2_y = -500
        if velocidaden2<70:
           velocidaden2 += 1.8
    if (pos3_y >= 600):
        pos3_y = -500
        if velocidaden3<70:
           velocidaden3 += 2.2


    pos_y += velocidaden1
    pos2_y += velocidaden2
    pos3_y += velocidaden3

    if (timer <10):
        timer +=1
    else:
        timer2 +=1
        texto = font.render("Score: "+str(timer2), True, (255,255,255), (0,0,0))
        timer = 0;



    janela.blit(fundo, (0, 0))
    janela.blit(jogador, (x, y))
    janela.blit(nave1, (pos_x, pos_y))
    janela.blit(nave2, (pos2_x, pos2_y))
    janela.blit(nave3, (pos3_x, pos3_y))
    janela.blit(texto, pos_texto)

    pygame.display.update()

pygame.quit()






