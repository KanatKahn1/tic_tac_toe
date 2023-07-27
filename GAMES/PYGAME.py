import pygame, sys, random
from pygame import math

cell_size = 20
cell_number = 20

FPS = 30

clock = pygame.time.Clock()
screen = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number))
pygame.display.set_caption('Prehistoric Snake')


class Main:
    def __init__(self):
        self.fruit = Fruit()
        self.snake = Snake()

    def update(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.check_collisions()
        self.check_fail()
        self.check_edges()


    def check_collisions(self):
        if self.snake.body[0] == self.fruit.pos:
            self.fruit.randomize()
            self.snake.grow()
        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()

    def check_fail(self):
        for block in self.snake.body[1:]:

            if block == self.snake.body[0]:
                self.reset()
    def reset(self):
        self.snake.body = [math.Vector2(5,10), math.Vector2(4.10), math.Vector2(3,10)]
        # self.snake.direction = math.Vector2(0,0)

    def check_edges(self):
        body_len = len(self.snake.body)
        body_copy = self.snake.body
        c_r_d = 0
        c_l_u = cell_number

        if self.snake.body[-1].x >= cell_number:
            for i in range(body_len):
                self.snake.body[i] = math.Vector2(c_r_d, body_copy[0].y)
                c_r_d -= 1
        if self.snake.body[-1].x <= 0:

            for i in range(body_len):
                self.snake.body[i] = math.Vector2(c, body_copy[0].y)
                c += 1
        # if self.snake.body[-1].y <= cell_number:
        #     c = cell_number
        #     for i in range(body_len):
        #         self.snake.body[i] = math.Vector2(body_copy[0]. x, c)
        #         c += 1
        # if self.snake.body[-1].x >= cell_number:
        #     c = 0
        #     for i in range(body_len):
        #         self.snake.body[i] = math.Vector2(body_copy[0].x, c)
        #         c -= 1
class Snake:
    def __init__(self):
        self.body = [math.Vector2(5, 10), math.Vector2(4, 10), math.Vector2(3, 10)]
        self.direction = math.Vector2(1, 0)
        self.new_block = False

        head_right = pygame.image.load('assets/Head.png')
        self.head_right = pygame.transform.scale(head_right, (cell_size, cell_size))
        self.head_down = pygame.transform.rotate(self.head_right, 90)
        self.head_left = pygame.transform.rotate(self.head_down, 90)
        self.head_up = pygame.transform.rotate(self.head_left, 90)

        body_horizontal = pygame.image.load('assets/Body.png')
        self.body_horizontal = pygame.transform.scale(body_horizontal, (cell_size, cell_size))
        self.body_vertical = pygame.transform.rotate(self.body_horizontal, 90)

        tail_r = pygame.image.load('assets/tail.png')
        self.tail_r = pygame.transform.scale(tail_r, (cell_size, cell_size))
        self.tail_d = pygame.transform.rotate(self.tail_r, 90)
        self.tail_l = pygame.transform.rotate(self.tail_d, 90)
        self.tail_u = pygame.transform.rotate(self.tail_l, 90)

        up_right_turn = pygame.image.load('assets/Turned_body.png')
        self.up_right_turned = pygame.transform.scale(up_right_turn, (cell_size, cell_size))
        self.up_left_turned = pygame.transform.rotate(self.up_right_turned, 90)
        self.down_left_turned = pygame.transform.rotate(self.up_left_turned, 90)
        self.down_right_turned = pygame.transform.rotate(self.down_left_turned, 90)

    def draw_snake(self):
        self.update_head()
        self.updater_tail()
        for index, block in enumerate(self.body):
            rect = pygame.Rect(block.x * cell_number, block.y * cell_number, cell_size, cell_size)
            if index == 0:
                screen.blit(self.head, rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail, rect)
            else:
                prev_block = self.body[index+1]-block
                next_block = self.body[index -1]-block
                if prev_block.x == next_block.x:
                    screen.blit(self.body_vertical, rect)
                elif prev_block.y == next_block.y:
                    screen.blit(self.body_horizontal,rect)
                else:
                    if prev_block.x == -1 and next_block.y == -1 or prev_block.y == -1 and next_block.x ==-1:
                        screen.blit(self.up_right_turned,rect)
                    elif prev_block.x == -1 and next_block.y == 1 or prev_block.y == 1 and next_block.x ==-1:
                        screen.blit(self.down_right_turned,rect)
                    elif prev_block.x == 1 and next_block.y == -1 or prev_block.y == -1 and next_block.x == 1:
                        screen.blit(self.up_left_turned, rect)
                    elif prev_block.x == 1 and next_block.y == 1 or prev_block.y == 1 and next_block.x == 1:
                        screen.blit(self.down_left_turned, rect)


    def update_head(self):
        head_dir = self.body[1] - self.body[0]
        if head_dir.x == 1:
            self.head = self.head_left
        elif head_dir.x == -1:
            self.head = self.head_right
        elif head_dir.y == 1:
            self.head = self.head_down
        elif head_dir.y == -1:
            self.head = self.head_up

    def updater_tail(self):
        tail_dir = self.body[-2] - self.body[-1]
        if tail_dir == math.Vector2(1, 0):
            self.tail = self.tail_r
        elif tail_dir == math.Vector2(-1, 0):
            self.tail = self.tail_l
        elif tail_dir == math.Vector2(0, 1):
            self.tail = self.tail_u
        elif tail_dir == math.Vector2(0, -1):
            self.tail = self.tail_d

    def move(self):


        copy_body = self.body
        if self.new_block == True:
            copy_body = self.body[:]
            copy_body.insert(0, copy_body[0] + self.direction)
            self.body = copy_body
            self.new_block = False
        else:
            copy_body = self.body[:-1]
            copy_body.insert(0, copy_body[0] + self.direction)
            self.body = copy_body

    def grow(self):
        self.new_block = True


class Fruit:
    def __init__(self):
        self.randomize()

        Apple = pygame.image.load('assets/Apple.png')
        self.apple = pygame.transform.scale(Apple,(cell_size,cell_size))

    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.x * cell_number, self.y * cell_number, cell_size, cell_size)
        screen.blit(self.apple, fruit_rect)

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = math.Vector2(self.x, self.y)
        return self.pos


SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 100)

main = Main()
running = True
while running:
    for event in pygame.event.get():
        clock.tick(FPS)
        if event.type == pygame.QUIT:
            running = False
            sys.exit()

        if event.type == SCREEN_UPDATE:
            main.snake.move()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main.snake.direction.y != 1:
                    main.snake.direction = math.Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                if main.snake.direction.y != -1:
                    main.snake.direction = math.Vector2(0, 1)
            if event.key == pygame.K_RIGHT:
                if main.snake.direction.x != -1:
                    main.snake.direction = math.Vector2(1, 0)
            if event.key == pygame.K_LEFT:
                if main.snake.direction.x != 1:
                    main.snake.direction = math.Vector2(-1, 0)

    screen.fill((100, 200, 122))
    main.update()

    # screen.update()

    pygame.display.flip()

pygame.quit()
