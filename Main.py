# -*- coding: utf-8 -*-
import locale
locale.setlocale(locale.LC_ALL, "")

import random
import calendar
import pygame

cmd = str(input("Please, enter command 'help' for output information about all commands:"))
while cmd != 'help':
	cmd = str(input("Please, enter command 'help' for output information about all commands:"))
	if cmd == 'help':
		print('create avatar \nsingle play \nmultiplayer \nsettings \nmissions \nsaves' 
			'\nЧтобы начать игру создайте аватара или выберите крайнее сохранение')
		cmd = str(input("Please, enter command 'help' for output information about all commands:"))
		if cmd == 'create avatar':
			name = str(input("Please, enter nickname your avatar's: "))
			age = int(input("Please, enter age your avatar's (15-60): "))
			while age != [15..60]: #try-except
				age = int(input("Please, enter age your avatar's: "))
				if age == [15..60]:
					break
			while sex != (female or male): #try-except
				sex = str(input("Please, enter sex your avatar's: "))
				if sex == (female or male):
					break
			h = 100 #health		
#условия возраста: если возраст X1-X2 и female, то характеристики одни, 
#если возраст X1-X2 и male, то характеристики вторые,
#если возраст X2-X3 и female, то характеристики третьи,
#и соответственно, если X2-X3 и male, то характеристики четвёртые
			if (age == [15..20]) and (sex == 'female'):
				f = random.randint(100, 175) #force
				s = int(10) #skills
				e = int(0) #enemy [0..100000]
				fr = int(0) #friends [0..100]
				l = int(e)+int(fr) #links with NPC and other players (l = e+fr)

'''
h = random.randint(100, 1000) #health
f = random.randint(100, 1000) #force
l = random.randint(0, 1000) #links with NPC and other players (l = e+fr)
s = random.randint(10, 1000) #skills
e = random.randint(0, 100) #enemy
fr = random.randint(0, 100) #friends
'''
if sex = female:
    f = random.randint(100, 800):
    if 100>=f>170:
        age = random.randint(15, 20)
'''
///    
#print(h, f, l, s, fr)
'''

    
