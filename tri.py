    # Optimisé pour une taille d'écran de 1366x768(px)

from tkinter import*
from random import*
from tkinter.messagebox import*
from operator import*

nbpaquet=1

# listes des cartes avec les 2 variables de couleur et de numero associé
ListeCarte=[('h1',1,1),('h2',1,2),('h3',1,3),('h4',1,4),('h5',1,5),('h6',1,6),('h7',1,7),('h8',1,8),('h9',1,9),('h10',1,10),('hj',1,11),('hq',1,12),('hk',1,13),
            ('c1',2,1),('c2',2,2),('c3',2,3),('c4',2,4),('c5',2,5),('c6',2,6),('c7',2,7),('c8',2,8),('c9',2,9),('c10',2,10),('cj',2,11),('cq',2,12),('ck',2,13),
            ('d1',3,1),('d2',3,2),('d3',3,3),('d4',3,4),('d5',3,5),('d6',3,6),('d7',3,7),('d8',3,8),('d9',3,9),('d10',3,10),('dj',3,11),('dq',3,12),('dk',3,13),
            ('s1',4,1),('s2',4,2),('s3',4,3),('s4',4,4),('s5',4,5),('s6',4,6),('s7',4,7),('s8',4,8),('s9',4,9),('s10',4,10),('sj',4,11),('sq',4,12),('sk',4,13)]

paquet2=[('h1',1,1),('h2',1,2),('h3',1,3),('h4',1,4),('h5',1,5),('h6',1,6),('h7',1,7),('h8',1,8),('h9',1,9),('h10',1,10),('hj',1,11),('hq',1,12),('hk',1,13),
        ('c1',2,1),('c2',2,2),('c3',2,3),('c4',2,4),('c5',2,5),('c6',2,6),('c7',2,7),('c8',2,8),('c9',2,9),('c10',2,10),('cj',2,11),('cq',2,12),('ck',2,13),
        ('d1',3,1),('d2',3,2),('d3',3,3),('d4',3,4),('d5',3,5),('d6',3,6),('d7',3,7),('d8',3,8),('d9',3,9),('d10',3,10),('dj',3,11),('dq',3,12),('dk',3,13),
        ('s1',4,1),('s2',4,2),('s3',4,3),('s4',4,4),('s5',4,5),('s6',4,6),('s7',4,7),('s8',4,8),('s9',4,9),('s10',4,10),('sj',4,11),('sq',4,12),('sk',4,13)]

# initialisation en plein écran de tkinter et d'un canvas
fenetre=Tk()
fenetre.attributes('-fullscreen', 1)
fenetre.title('tri de cartes')
canvas=Canvas(fenetre,width=1366,height=768,highlightthickness=0)
canvas.pack()

# fond d'écran du canvas et initialisation des listes de stockage des gifs cartes
Fond=PhotoImage(file='cards_gif/fond.gif')
photo=[0]*52
photo2=[0]*52


# fonction appellée lors de la fermeture du programme    
def Quitter():
    if askyesno('Quitter', 'Voulez-vous quitter ce programme magnifique?'):
        showwarning('Quitter', 'Tant pis...')
        fenetre.destroy()
    else:
        showinfo('Quitter', 'Bonne Décision!')

# fonction appellée lors de la fermeture du programme avec le raccourci clavier
def QuitterR(event):
    if askyesno('Quitter', 'Voulez-vous quitter ce programme magnifique?'):
        showwarning('Quitter', 'Tant pis...')
        fenetre.destroy()
    else:
        showinfo('Quitter', 'Bonne Décision!')

# fonction mélanger aléatoirement
def Melanger():
    # variable global nbpaquet qui permet de savoir combien de paquet afficher
    global nbpaquet
    x=[1,2]
    # choix aléatoire d'un nombre de paquet
    nbpaquet=choice(x)
    # reset du canvas
    canvas.delete(ALL)
    canvas.create_image(0,0,anchor=NW,image=Fond)
    if nbpaquet==1 or nbpaquet==2:
        shuffle(ListeCarte)
        # affichager du 1er paquet mélangé
        for i in range(len(ListeCarte)):
            # stockage des gifs dans la liste photo
            photo[i]=PhotoImage(file='cards_gif/'+ListeCarte[i][0]+'.gif')
            if i<13:
                canvas.create_image(100+i*25,100,anchor=NW,image=photo[i])
            if i>12 and i<26:
                canvas.create_image(100+(i-13)*25,250,anchor=NW,image=photo[i])
            if i>25 and i<39:
                canvas.create_image(100+(i-26)*25,400,anchor=NW,image=photo[i])
            if i>38:
                canvas.create_image(100+(i-39)*25,550,anchor=NW,image=photo[i])
    if nbpaquet==2:
        shuffle(paquet2)
        # affichage du 2eme paquet mélangé
        for i in range(len(paquet2)):
            photo2[i]=PhotoImage(file='cards_gif/'+paquet2[i][0]+' - Copie.gif')
            if i<13:
                canvas.create_image(900+i*25,100,anchor=NW,image=photo2[i])
            if i>12 and i<26:
                canvas.create_image(900+(i-13)*25,250,anchor=NW,image=photo2[i])
            if i>25 and i<39:
                canvas.create_image(900+(i-26)*25,400,anchor=NW,image=photo2[i])
            if i>38:
                canvas.create_image(900+(i-39)*25,550,anchor=NW,image=photo2[i])

# fonction mélanger 1 paquet
def Melanger1():
    global nbpaquet
    nbpaquet=1
    canvas.delete(ALL) 
    canvas.create_image(0,0,anchor=NW,image=Fond)
    shuffle(ListeCarte)
    for i in range(len(ListeCarte)):
        photo[i]=PhotoImage(file='cards_gif/'+ListeCarte[i][0]+'.gif')
        if i<13:
            canvas.create_image(100+i*25,100,anchor=NW,image=photo[i])
        if i>12 and i<26:
            canvas.create_image(100+(i-13)*25,250,anchor=NW,image=photo[i])
        if i>25 and i<39:
            canvas.create_image(100+(i-26)*25,400,anchor=NW,image=photo[i])
        if i>38:
            canvas.create_image(100+(i-39)*25,550,anchor=NW,image=photo[i])

# fonction mélanger 2 paquets
def Melanger2():
    global nbpaquet
    nbpaquet=2
    shuffle(ListeCarte)
    shuffle(paquet2)
    for i in range(len(ListeCarte)):
        photo[i]=PhotoImage(file='cards_gif/'+ListeCarte[i][0]+'.gif')
        if i<13:
            canvas.create_image(100+i*25,100,anchor=NW,image=photo[i])
        if i>12 and i<26:
            canvas.create_image(100+(i-13)*25,250,anchor=NW,image=photo[i])
        if i>25 and i<39:
            canvas.create_image(100+(i-26)*25,400,anchor=NW,image=photo[i])
        if i>38:
            canvas.create_image(100+(i-39)*25,550,anchor=NW,image=photo[i])
    for i in range(len(paquet2)):
        photo2[i]=PhotoImage(file='cards_gif/'+paquet2[i][0]+' - Copie.gif')
        if i<13:
            canvas.create_image(900+i*25,100,anchor=NW,image=photo2[i])
        if i>12 and i<26:
            canvas.create_image(900+(i-13)*25,250,anchor=NW,image=photo2[i])
        if i>25 and i<39:
            canvas.create_image(900+(i-26)*25,400,anchor=NW,image=photo2[i])
        if i>38:
            canvas.create_image(900+(i-39)*25,550,anchor=NW,image=photo2[i])

# fonction tri par couleur croissante
def CCroissant():
    global nbpaquet
    # méthode de tri grâce aux variables associées aux nom des cartes
    ListeCarte.sort(key=itemgetter(1,2))
    paquet2.sort(key=itemgetter(1,2))
    if nbpaquet==2:
        for i in range(len(paquet2)):
            photo2[i]=PhotoImage(file='cards_gif/'+paquet2[i][0]+' - Copie.gif')
            if i<13:
                canvas.create_image(900+i*25,100,anchor=NW,image=photo2[i])
            if i>12 and i<26:
                canvas.create_image(900+(i-13)*25,250,anchor=NW,image=photo2[i])
            if i>25 and i<39:
                canvas.create_image(900+(i-26)*25,400,anchor=NW,image=photo2[i])
            if i>38:
                canvas.create_image(900+(i-39)*25,550,anchor=NW,image=photo2[i]) 
    for i in range(len(ListeCarte)):
        photo[i]=PhotoImage(file='cards_gif/'+ListeCarte[i][0]+'.gif')
        if i<13:
            canvas.create_image(100+i*25,100,anchor=NW,image=photo[i])
        if i>12 and i<26:
            canvas.create_image(100+(i-13)*25,250,anchor=NW,image=photo[i])
        if i>25 and i<39:
            canvas.create_image(100+(i-26)*25,400,anchor=NW,image=photo[i])
        if i>38:
            canvas.create_image(100+(i-39)*25,550,anchor=NW,image=photo[i])

# fonction tri par couleur décroissante
def CDecroissant():
    global nbpaquet
    ListeCarte.sort(key=itemgetter(1,2), reverse=True)
    paquet2.sort(key=itemgetter(1,2), reverse=True)
    if nbpaquet==2:
        for i in range(len(paquet2)):
            photo2[i]=PhotoImage(file='cards_gif/'+paquet2[i][0]+' - Copie.gif')
            if i<13:
                canvas.create_image(900+i*25,100,anchor=NW,image=photo2[i])
            if i>12 and i<26:
                canvas.create_image(900+(i-13)*25,250,anchor=NW,image=photo2[i])
            if i>25 and i<39:
                canvas.create_image(900+(i-26)*25,400,anchor=NW,image=photo2[i])
            if i>38:
                canvas.create_image(900+(i-39)*25,550,anchor=NW,image=photo2[i]) 
    for i in range(len(ListeCarte)):
        photo[i]=PhotoImage(file='cards_gif/'+ListeCarte[i][0]+'.gif')
        if i<13:
            canvas.create_image(100+i*25,100,anchor=NW,image=photo[i])
        if i>12 and i<26:
            canvas.create_image(100+(i-13)*25,250,anchor=NW,image=photo[i])
        if i>25 and i<39:
            canvas.create_image(100+(i-26)*25,400,anchor=NW,image=photo[i])
        if i>38:
            canvas.create_image(100+(i-39)*25,550,anchor=NW,image=photo[i])

# fonction tri par numéro croissant
def NCroissant():
    global nbpaquet
    ListeCarte.sort(key=itemgetter(2,1))
    paquet2.sort(key=itemgetter(2,1))
    if nbpaquet==2:
        for i in range(len(paquet2)):
            photo2[i]=PhotoImage(file='cards_gif/'+paquet2[i][0]+' - Copie.gif')
            if i<4:
                canvas.create_image(10+i*25,400,anchor=NW,image=photo2[i])
            if i>3 and i<8:
                canvas.create_image(10+i*25,400,anchor=NW,image=photo2[i])
            if i>7 and i<12:
                canvas.create_image(10+i*25,400,anchor=NW,image=photo2[i])
            if i>11 and i<16:
                canvas.create_image(10+i*25,400,anchor=NW,image=photo2[i])
            if i>15 and i<20:
                canvas.create_image(10+i*25,400,anchor=NW,image=photo2[i])
            if i>19 and i<24:
                canvas.create_image(10+i*25,400,anchor=NW,image=photo2[i])
            if i>23 and i<28:
                canvas.create_image(10+i*25,400,anchor=NW,image=photo2[i])
            if i>27 and i<32:
                canvas.create_image(10+i*25,400,anchor=NW,image=photo2[i])
            if i>31 and i<36:
                canvas.create_image(10+i*25,400,anchor=NW,image=photo2[i])
            if i>35 and i<40:
                canvas.create_image(10+i*25,400,anchor=NW,image=photo2[i])
            if i>39 and i<44:
                canvas.create_image(10+i*25,400,anchor=NW,image=photo2[i])
            if i>43 and i<48:
                canvas.create_image(10+i*25,400,anchor=NW,image=photo2[i])
            if i>47:
                canvas.create_image(10+i*25,400,anchor=NW,image=photo2[i])
    for i in range(len(ListeCarte)):
        photo[i]=PhotoImage(file='cards_gif/'+ListeCarte[i][0]+'.gif')
        if i<4:
            canvas.create_image(10+i*25,200,anchor=NW,image=photo[i])
        if i>3 and i<8:
            canvas.create_image(10+i*25,200,anchor=NW,image=photo[i])
        if i>7 and i<12:
            canvas.create_image(10+i*25,200,anchor=NW,image=photo[i])
        if i>11 and i<16:
            canvas.create_image(10+i*25,200,anchor=NW,image=photo[i])
        if i>15 and i<20:
            canvas.create_image(10+i*25,200,anchor=NW,image=photo[i])
        if i>19 and i<24:
            canvas.create_image(10+i*25,200,anchor=NW,image=photo[i])
        if i>23 and i<28:
            canvas.create_image(10+i*25,200,anchor=NW,image=photo[i])
        if i>27 and i<32:
            canvas.create_image(10+i*25,200,anchor=NW,image=photo[i])
        if i>31 and i<36:
            canvas.create_image(10+i*25,200,anchor=NW,image=photo[i])
        if i>35 and i<40:
            canvas.create_image(10+i*25,200,anchor=NW,image=photo[i])
        if i>39 and i<44:
            canvas.create_image(10+i*25,200,anchor=NW,image=photo[i])
        if i>43 and i<48:
            canvas.create_image(10+i*25,200,anchor=NW,image=photo[i])
        if i>47:
            canvas.create_image(10+i*25,200,anchor=NW,image=photo[i])

# fonction tri par numéro décroissant
def NDecroissant():
    global nbpaquet
    ListeCarte.sort(key=itemgetter(2,1), reverse=True)
    paquet2.sort(key=itemgetter(2,1), reverse=True)
    if nbpaquet==2:
        for i in range(len(paquet2)):
            photo2[i]=PhotoImage(file='cards_gif/'+paquet2[i][0]+' - Copie.gif')
            if i<4:
                canvas.create_image(10+i*25,400,anchor=NW,image=photo2[i])
            if i>3 and i<8:
                canvas.create_image(10+i*25,400,anchor=NW,image=photo2[i])
            if i>7 and i<12:
                canvas.create_image(10+i*25,400,anchor=NW,image=photo2[i])
            if i>11 and i<16:
                canvas.create_image(10+i*25,400,anchor=NW,image=photo2[i])
            if i>15 and i<20:
                canvas.create_image(10+i*25,400,anchor=NW,image=photo2[i])
            if i>19 and i<24:
                canvas.create_image(10+i*25,400,anchor=NW,image=photo2[i])
            if i>23 and i<28:
                canvas.create_image(10+i*25,400,anchor=NW,image=photo2[i])
            if i>27 and i<32:
                canvas.create_image(10+i*25,400,anchor=NW,image=photo2[i])
            if i>31 and i<36:
                canvas.create_image(10+i*25,400,anchor=NW,image=photo2[i])
            if i>35 and i<40:
                canvas.create_image(10+i*25,400,anchor=NW,image=photo2[i])
            if i>39 and i<44:
                canvas.create_image(10+i*25,400,anchor=NW,image=photo2[i])
            if i>43 and i<48:
                canvas.create_image(10+i*25,400,anchor=NW,image=photo2[i])
            if i>47:
                canvas.create_image(10+i*25,400,anchor=NW,image=photo2[i])
    for i in range(len(ListeCarte)):
        photo[i]=PhotoImage(file='cards_gif/'+ListeCarte[i][0]+'.gif')
        if i<4:
            canvas.create_image(10+i*25,200,anchor=NW,image=photo[i])
        if i>3 and i<8:
            canvas.create_image(10+i*25,200,anchor=NW,image=photo[i])
        if i>7 and i<12:
            canvas.create_image(10+i*25,200,anchor=NW,image=photo[i])
        if i>11 and i<16:
            canvas.create_image(10+i*25,200,anchor=NW,image=photo[i])
        if i>15 and i<20:
            canvas.create_image(10+i*25,200,anchor=NW,image=photo[i])
        if i>19 and i<24:
            canvas.create_image(10+i*25,200,anchor=NW,image=photo[i])
        if i>23 and i<28:
            canvas.create_image(10+i*25,200,anchor=NW,image=photo[i])
        if i>27 and i<32:
            canvas.create_image(10+i*25,200,anchor=NW,image=photo[i])
        if i>31 and i<36:
            canvas.create_image(10+i*25,200,anchor=NW,image=photo[i])
        if i>35 and i<40:
            canvas.create_image(10+i*25,200,anchor=NW,image=photo[i])
        if i>39 and i<44:
            canvas.create_image(10+i*25,200,anchor=NW,image=photo[i])
        if i>43 and i<48:
            canvas.create_image(10+i*25,200,anchor=NW,image=photo[i])
        if i>47:
            canvas.create_image(10+i*25,200,anchor=NW,image=photo[i])

# fonction a propos qui affiche une fenetre d'explications
def Apropos():
    popup=Tk()
    popup.title('A propos')
    # ouverture du ficher a_propos en lecture
    fichier=open('a_propos.txt', 'r')
    content=fichier.read()
    fichier.close()


    Label(popup, justify='left', text=content).pack()
    popup.mainloop()


# début du programme avec l'affichage d'un paquet mélangé
Melanger1()
canvas.bind('<Control-Key-q>',QuitterR)
canvas.focus_set()

# menu du programme
menubar=Menu(fenetre)

menu1=Menu(menubar,tearoff=0)
menubar.add_cascade(label='Trier les cartes', menu=menu1)
menu1.add_command(label='Par couleur croissant', command=CCroissant)
menu1.add_command(label='Par couleur décroissant', command=CDecroissant)
menu1.add_separator()
menu1.add_command(label='Par numéro croissant', command=NCroissant)
menu1.add_command(label='Par numéro décroissant', command=NDecroissant)
menu1.add_separator()
menu1.add_separator()
menu1.add_command(label='Quitter',accelerator='Ctrl+Q', command=Quitter)

menu2=Menu(menubar,tearoff=0)
menubar.add_cascade(label='Mélanger les cartes', menu=menu2)
menu2.add_command(label='Mélanger 1 paquet', command=Melanger1)
menu2.add_command(label='Mélanger 2 paquets', command=Melanger2)
menu2.add_command(label='Choisir aléatoirement', command=Melanger)

menubar.add_command(label='A propos', command=Apropos)

fenetre.config(menu=menubar)


# fermeture de la fenetre tkinter
fenetre.mainloop()
