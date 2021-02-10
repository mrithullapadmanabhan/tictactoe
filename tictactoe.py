import pygame
import math
pygame.init()

win = pygame.display.set_mode((550, 550))

pygame.display.set_caption('Tic Tac Toe')

first = pygame.draw.rect(win, (255, 255, 255), (25, 25, 150, 150)) #(for the color, for the size and position)
second = pygame.draw.rect(win, (255, 255, 255), (200, 25, 150, 150))
third = pygame.draw.rect(win, (255, 255, 255), (370, 25, 150, 150))

fourth = pygame.draw.rect(win, (255, 255, 255), (25, 200, 150, 150))
fifth = pygame.draw.rect(win, (255, 255, 255), (200, 200, 150, 150))
sixth = pygame.draw.rect(win, (255, 255, 255), (375, 200, 150, 150))

seventh = pygame.draw.rect(win, (255, 255, 255), (25, 375, 150, 150))
eighth = pygame.draw.rect(win, (255, 255, 255), (200, 375, 150, 150))
ninth = pygame.draw.rect(win, (255, 255, 255), (375, 375, 150, 150))
run = True

draw_object = 'rect'

first_open = True
sec_open = True
third_open = True
fourth_open = True
fif_open = True
six_open = True
sev_open = True
eighth_open = True
nin_open = True

while run:

	pygame.time.delay(100)

	#for the keyboard...notices the mouse pointer(to exit the game when clicked on the close option)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False


        #To check if any key is pressed
		if event.type == pygame.KEYDOWN:
			#To check if the key pressed is a space
			if event.key == pygame.K_SPACE:

				first_open = True
				sec_open = True
				third_open = True
				fourth_open = True
				fif_open = True
				six_open = True
				sev_open = True
				eighth_open = True
				nin_open = True

				first = pygame.draw.rect(win, (255, 255, 255), (25, 25, 150, 150))
				#(for the color, for the size and position)
				second = pygame.draw.rect(win, (255, 255, 255), (200, 25, 150, 150))
				third = pygame.draw.rect(win, (255, 255, 255), (370, 25, 150, 150))

				fourth = pygame.draw.rect(win, (255, 255, 255), (25, 200, 150, 150))
				fifth = pygame.draw.rect(win, (255, 255, 255), (200, 200, 150, 150))
				sixth = pygame.draw.rect(win, (255, 255, 255), (375, 200, 150, 150))

				seventh = pygame.draw.rect(win, (255, 255, 255), (25, 375, 150, 150))
				eighth = pygame.draw.rect(win, (255, 255, 255), (200, 375, 150, 150))
				ninth = pygame.draw.rect(win, (255, 255, 255), (375, 375, 150, 150))


		# whenever the mouse button is up ie after click
		if event.type == pygame.MOUSEBUTTONUP:
			pos = pygame.mouse.get_pos()
			if first.collidepoint(pos) and first_open:
				if draw_object == 'rect':
					pygame.draw.rect(win, (255, 0, 0), (50, 50, 100, 100))
					draw_object = 'circle'
				else:
					pygame.draw.circle(win, (0, 255, 0), (100, 100), 50)
					draw = 'rect'
				first_open = False

			if second.collidepoint(pos) and sec_open:
				if draw_object == 'rect':
					pygame.draw.rect(win, (255, 0, 0), (225, 50, 100, 100))
					draw_object = 'circle'
				else:
					pygame.draw.circle(win, (0, 255, 0), (275, 100), 50)
					draw_object = 'rect'
				sec_open = False

			if third.collidepoint(pos) and third_open:
				if draw_object == 'rect':
					pygame.draw.rect(win, (255, 0, 0), (400, 50, 100, 100))
					draw_object = 'circle'
				else:
					pygame.draw.circle(win, (0, 255, 0), (450, 100), 50)
					draw_object = 'rect'
				third_open = False

			if fourth.collidepoint(pos) and fourth_open:
				if draw_object == 'rect':
					pygame.draw.rect(win, (255, 0, 0), (50, 225, 100, 100))
					draw_object = 'circle'
				else:
					pygame.draw.circle(win, (0, 255, 0), (100, 275), 50)
					draw_object = 'rect'
				fourth_open = False

			if fifth.collidepoint(pos) and fif_open:
				if draw_object == 'rect':
					pygame.draw.rect(win, (255, 0, 0), (225, 225, 100, 100))
					draw_object = 'circle'
				else:
					pygame.draw.circle(win, (0, 255, 0), (275, 275), 50)
					draw_object = 'rect'
				fif_open = False

			if sixth.collidepoint(pos) and six_open:
				if draw_object == 'rect':
					pygame.draw.rect(win, (255, 0, 0), (400, 225, 100, 100))
					draw_object = 'circle'
				else:
					pygame.draw.circle(win, (0, 255, 0), (450, 275), 50)
					draw_object = 'rect'
				six_open = False

			if seventh.collidepoint(pos) and sev_open:
				if draw_object == 'rect':
					pygame.draw.rect(win, (255, 0, 0), (50, 400, 100, 100))
					draw_object = 'circle'
				else:
					pygame.draw.circle(win, (0, 255, 0), (100, 450), 50)
					draw_object = 'rect'
				sev_open = False

			if eighth.collidepoint(pos) and eighth_open:
				if draw_object == 'rect':
					pygame.draw.rect(win, (255, 0, 0), (225, 400, 100, 100))
					draw_object = 'circle'
				else:
					pygame.draw.circle(win, (0, 255, 0), (275, 450), 50)
					draw_object = 'rect'
				eighth_open = False
			if ninth.collidepoint(pos) and nin_open:
				if draw_object == 'rect':
					pygame.draw.rect(win, (255, 0, 0), (400, 400, 100, 100))
					draw_object = 'circle'
				else:
					pygame.draw.circle(win, (0, 255, 0), (450, 450), 50)
					draw_object = 'rect'
				nin_open = False


    #whenever new things happen it update or display in the front of the screen.
	pygame.display.update()
pygame.quit()