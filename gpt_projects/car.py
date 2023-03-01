import pygame

# initialize pygame
pygame.init()

# set up the window
screen_width, screen_height = 640, 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Car Simulation")

# load the car image
car_image = pygame.image.load("car.png").convert_alpha()

# set the initial position and velocity of the car
car_x, car_y = screen_width // 2, screen_height // 2
car_vx, car_vy = 0, 0
car_speed = 5

# main game loop
running = True
while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                car_vy = -car_speed
            elif event.key == pygame.K_DOWN:
                car_vy = car_speed
            elif event.key == pygame.K_LEFT:
                car_vx = -car_speed
            elif event.key == pygame.K_RIGHT:
                car_vx = car_speed
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                car_vy = 0
            elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                car_vx = 0

    # update the car's position based on velocity
    car_x += car_vx
    car_y += car_vy

    # draw the car onto the screen
    screen.blit(car_image, (car_x, car_y))

    # update the screen
    pygame.display.flip()

    # wait for a short time to control the frame rate
    pygame.time.wait(10)

# clean up resources
pygame.quit()
