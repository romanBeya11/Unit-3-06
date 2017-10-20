import ui
import time

@ui.in_background

def animate():
	counter = 1
	while(counter <= 50):
		if counter == 1:
			view['imageview1'].image = ui.Image.named("./assets/sprites/walking_man_1.bmp")
		elif counter == 2:
			view['imageview1'].image = ui.Image.named("./assets/sprites/walking_man_2.bmp")
		elif counter == 3:
			view['imageview1'].image = ui.Image.named("./assets/sprites/walking_man_3.bmp")
		elif counter == 4:
			view['imageview1'].image = ui.Image.named("./assets/sprites/walking_man_4.bmp")
		elif counter == 5:
			view['imageview1'].image = ui.Image.named("./assets/sprites/walking_man_5.bmp")
		elif counter == 6:
			view['imageview1'].image = ui.Image.named("./assets/sprites/walking_man_6.bmp")
		elif counter == 7:
			view['imageview1'].image = ui.Image.named("./assets/sprites/walking_man_7.bmp")
		elif counter == 8:
			view['imageview1'].image = ui.Image.named("./assets/sprites/walking_man_8.bmp")
		elif counter == 9:
			view['imageview1'].image = ui.Image.named("./assets/sprites/walking_man_9.bmp")
		elif counter == 10:
			view['imageview1'].image = ui.Image.named("./assets/sprites/walking_man_10.bmp")
		counter = counter + 1
		time.sleep(0.15)
		view['imageview1'].x = view['imageview1'].x - 10
		if view['imageview1'].x <= -250:
			view['imageview1'].x = 225
		if counter >= 10:
			counter = 1
		
animate()
view = ui.load_view()
view.present('sheet')
