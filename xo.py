# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.





from asyncio import constants
import pygame
import random
import sys
import time




pygame.init()
screen=pygame.display.set_mode((600,600))
grey=(255, 255, 255, 255)
gold =(255, 215, 0, 255)
aqua=(0,255,255)
screen.fill(aqua)
plateau=[0,0,0,0,0,0,0,0,0]
font1=pygame.font.SysFont("verdana",60)
text1=font1.render("Game Over",True,(0,0,0))
font2=pygame.font.SysFont("verdana",25)
text2=font2.render("press space to restart",True,(0,0,0))
pygame.draw.line(screen,grey,(0,200),(600,200),10)
pygame.draw.line(screen,grey,(0,400),(600,400),10)
pygame.draw.line(screen,grey,(200,0),(200,600),10)
pygame.draw.line(screen,grey,(400,0),(400,600),10)


class noeud:
    def __init__(self,fils,plateau,valeur,turn,profondeur):
        self.fils=fils
        self.plateau=plateau
        self.valeur=valeur
        self.turn=turn
        self.profondeur=profondeur




def vainqueur(P):
    for i in range(3):
        if P[3*i]==P[3*i+1]==P[3*i+2] and P[3*i] in [1,2] :
            if P == plateau:
               pygame.draw.line(screen, gold, (i * 200 + 100, 0), (i * 200 + 100, 600), 7)
            return P[3*i]
        if P[i]==P[i+3]==P[i+6] and P[i] in [1,2] :
            if P == plateau:
               pygame.draw.line(screen, gold, (0, i * 200 + 100), (600, i * 200 + 100), 7)
            return P[i]
    if P[0]==P[4]==P[8] and P[0] in [1,2] :
        if P == plateau:
           pygame.draw.line(screen,gold,(0,0),(600,600),7)
        return P[4]
    if P[6]==P[4]==P[2] and P[4] in [1,2] :
        if P==plateau:
           pygame.draw.line(screen, gold, (600,0), (0, 600), 7)
        return P[4]


def finjeu(plateau):
    for i in range(9):
            if plateau[i]==0:
                return False
    return True

def case(plateau):
    L=[]
    F=finjeu(plateau)
    V1=vainqueur(plateau)
    if F or V1 :
        return L
    for i in range (9):
            if plateau[i]==0:
                L.append(i)
    return L


def new_minimax(pere):
    L=case(pere.plateau)
    n=len(L)
    if L:
        pere.profondeur+=1
        for i in range(n) :
            C=pere.plateau.copy()
            C[i]=pere.turn
            d=(pere.turn+1)%2
            if d==0 :
                d=2
            pere.fils.append(noeud([],C,"?",d,0))
            if vainqueur(C) == 2:
                pere.fils[i].valeur=1
            elif vainqueur(C) ==1:
                pere.fils[i].valeur=-1
            elif finjeu(C):
                pere.fils[i].valeur=0
            else:
                new_minimax(pere.fils[i])

        m=len(pere.fils)
        M=pere.fils[0].valeur
        k=1
        choix=[]
        for i in range (1,m) :
            if pere.fils[i].valeur==M :
                choix.append(pere.fils[i])
            if pere.turn==2:
                if pere.fils[i].valeur>M :
                    M=pere.fils[i].valeur
                    choix=[]
            else :
                if pere.fils[i].valeur<M :
                    M=pere.fils[i].valeur
                    choix=[]
    
        return random.sample(choix,1)[0]
    

            
                    


            



        
                





def minimax(plateau):
    A = [[plateau, '?']]
    L = case(plateau)
    if L:
        for i in L:
            C = plateau.copy()
            C[i] = 2
            if vainqueur(C) == 2:
                A.append([[C, 1]])
            elif vainqueur(C) ==1:
                A.append([[C, -1]])
            elif finjeu(C):
                A.append([[C, 0]])
            else:
                D = [[C, '?']]
                I = case(C)
                for k in I:
                    B = C.copy()
                    B[k] = 1
                    if vainqueur(B) == 2:
                        D.append([[B, 1]])
                    elif vainqueur(B) == 1:
                        D.append([[B, -1]])
                    elif finjeu(B):
                        D.append([[B, 0]])
                    else:
                        D.append(minimax(B)[0])
                k = len(D)
                m = D[1][0][1]
                for i in range(2, k):
                    if m == '?' or D[i][0][1] == '?':
                        m = '?'
                        break
                    else:
                        if m > D[i][0][1]:
                            m = D[i][0][1]
                if m != '?':
                    D[0][1] = m
                A.append(D)
        n = len(A)
        M = A[1][0][1]
        k = 1
        for i in range(2, n):
            if M == '?' or A[i][0][1] == '?':
                M = '?'
                break
            else:
                if M < A[i][0][1]:
                    M = A[i][0][1]
                    k = i

        if M != '?':
            A[0][1] = M

        return A, k


def remplissage(k,jouc):
    i=k//3
    j=k%3
    if plateau[3*i+j]==0:
        plateau[3*i+j]=jouc
        if jouc==1 :
            pygame.draw.circle(screen,grey,(i*200+100,j*200+100),80,10)
        else :
            pygame.draw.line(screen,grey , (i*200+20,j*200+20),(i*200+180,j*200+180),10)
            pygame.draw.line(screen,grey , (i * 200 +180, j * 200 + 20), (i * 200 +20 ,j * 200 + 180), 10)
    return True
turn=1
D=True
f=0
d=0
running=True
F=False
V=False
while running :
    if f-d<2 :
        pygame.display.update()
        if vainqueur(plateau) :
            V=True
        F = finjeu(plateau)
        if not  F and not V :
                if turn==1 :
                    for event in pygame.event.get():
                        if event.type==pygame.QUIT:
                            running=False
                            pygame.quit()
                        if event.type==pygame.MOUSEBUTTONDOWN :
                            X=int(event.pos[0]/200)
                            Y= int(event.pos[1]/200)
                            L = case(plateau)
                            if 3*X+Y in L :
                                remplissage(3*X+Y,turn)
                                plateau[3*X+Y]=turn
                                turn=2

                else :
                        racine=noeud([],plateau,"?",turn,0)
                        if minimax(plateau) :
                          A,k= minimax(plateau)
                        plateau2=A[k][0][0]
                        for i in range(9) :
                                if plateau2[i]!=plateau[i] :
                                    remplissage(i,2)
                        turn=1
        else :
            if D==True :
              d=time.time()
              D=False
            f=time.time()
    else :
        screen.fill(aqua)
        screen.blit(text1,(130,220))
        screen.blit(text2,(165,300))
        pygame.display.flip()
        for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running=False
                    pygame.quit()
                if event.type ==pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE :
                        F=False
                        V=False
                        D=True
                        f=0
                        d=0
                        plateau=[0,0,0,0,0,0,0,0,0]
                        screen.fill(aqua)
                        pygame.draw.line(screen,grey,(0,200),(600,200),10)
                        pygame.draw.line(screen,grey,(0,400),(600,400),10)
                        pygame.draw.line(screen,grey,(200,0),(200,600),10)
                        pygame.draw.line(screen,grey,(400,0),(400,600),10)








