import pygame
import random

from pygame.examples.aliens import load_sound


class Player (pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load('../images/player.png').convert_alpha()
        self.rect = self.image.get_frect(center= (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
        self.direction = pygame.math.Vector2()
        self.speed = 500
        #cooldown section
        self.can_shoot = True
        self.laser_shoot_time = 0
        self.cooldown_duration = 400

    def laser_timer(self):
        #this function gets switches the shoot abb after cooldown
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_shoot_time >= self.cooldown_duration:
                self.can_shoot = True

    def update(self, dt):
        #player movement properties + key mapping
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        # this method unifies speed of movement (2axis > 1axis)
        self.direction = self.direction.normalize() if self.direction else self.direction
        self.rect.center += self.direction * self.speed * dt

        #shooting key mapping + can_shoot switch + cooldown func
        recent_keys = pygame.key.get_just_pressed()
        if recent_keys[pygame.K_SPACE] and self.can_shoot:
            Laser(laser_surf, self.rect.midtop, (all_sprites, laser_sprites))
            self.can_shoot = False
            self.laser_shoot_time = pygame.time.get_ticks()
            laser_sound.play()

        self.laser_timer()

class Stars(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load('../images/star.png').convert_alpha()
        self.rect = self.image.get_frect(center= (random.randint(30, 1200), random.randint(30, 680)))

class Laser(pygame.sprite.Sprite):
    def __init__(self, surf, position, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(midbottom = position)

    def update(self, dt):
        #function to move laser sprite
        self.rect.centery -= 400 * dt
        #deletion of invisible lasers
        if self.rect.bottom < 0:
            self.kill()


class Meteor(pygame.sprite.Sprite):
    def __init__(self, surf, position, groups):
        super().__init__(groups)
        self.original_surf = surf
        self.image = surf
        self.rect = self.image.get_frect(center= position)
        self.start_time = pygame.time.get_ticks()
        self.life_time = 3000
        self.speed = random.randint(400, 500)
        self.direction = pygame.Vector2(random.uniform(-0.5, 0.5), 1)
        self.rotation_speed = random.randint(40, 80)
        self.rotation = 0

    def update(self, dt):
        self.rect.center += self.direction * self.speed * dt
        if pygame.time.get_ticks() - self.start_time >= self.life_time:
            self.kill()
        self.rotation += self.rotation_speed * dt
        self.image = pygame.transform.rotozoom(self.original_surf, self.rotation, 1)
        #stabilization of meteors (weird trajectory occured)
        self.rect = self.image.get_frect(center = self.rect.center)

class AnimatedExplosions(pygame.sprite.Sprite):
    def __init__(self, frames, position, groups):
        super().__init__(groups)
        self.frames = frames
        self.frames_index = 0
        self.image = self.frames[self.frames_index]
        self.rect = self.image.get_frect(center= position)

    def update(self, dt):
        self.frames_index += 20 * dt
        if self.frames_index < len(self.frames):
            self.image = self.frames[int(self.frames_index) % len(self.frames)]
        else:
            self.kill()

def collisions():
    global running
    # removal of collided meteors + collided lasers removal
    collision_sprites = pygame.sprite.spritecollide(player, meteor_sprites, True, pygame.sprite.collide_mask)
    if collision_sprites:
        running = False
    for laser in laser_sprites:
        collided_sprites = pygame.sprite.spritecollide(laser, meteor_sprites, True)
        if collided_sprites:
            laser.kill()
            AnimatedExplosions(explosion_frames, laser.rect.center, all_sprites)
            explosion_sound.play()

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000)
    text_surf = font.render(str(current_time), True, 'white')
    text_rec = text_surf.get_frect(midbottom= (WINDOW_WIDTH / 2, WINDOW_HEIGHT - 50))
    display_surface.blit(text_surf, text_rec)
    pygame.draw.rect(display_surface, 'white', text_rec.inflate(20, 20).move(0, -3), 5, 10)

#general setup
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
running = True
clock = pygame.time.Clock()

#creating a display surface
pygame.init()
pygame.mixer.init()
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Space Shooter')

#import
meteor_surf = pygame.image.load('../images/meteor.png').convert_alpha()
laser_surf = pygame.image.load('../images/laser.png').convert_alpha()
font = pygame.font.Font(None, 40)
explosion_frames = [pygame.image.load(f'../images/explosion/{i}.png').convert_alpha() for i in range (21)]
laser_sound = pygame.mixer.Sound(file='../audio/laser.wav')
laser_sound.set_volume(0.5)
explosion_sound = pygame.mixer.Sound(file='../audio/explosion.wav')
damage_sound = pygame.mixer.Sound(file='../audio/damage.ogg')
game_music = pygame.mixer.Sound(file='../audio/game_music.wav')
game_music.set_volume(0.4)
game_music.play(loops= -1)

#sprites
all_sprites = pygame.sprite.Group()
meteor_sprites = pygame.sprite.Group()
laser_sprites = pygame.sprite.Group()

#setting up stars + player obj
for i in range (20):
    Stars(all_sprites)
player = Player(all_sprites)

#custom events --> meteor event
meteor_event = pygame.event.custom_type()
pygame.time.set_timer(meteor_event, 500)

#by while loop we're creating frames
while running:
    #creating delta time + converting it from ms to s
    dt = clock.tick() / 1000
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == meteor_event:
            x = random.randint(0, WINDOW_WIDTH)
            y = random.randint(-200, -100)
            Meteor(meteor_surf, (x, y), (all_sprites, meteor_sprites))

    #draw the game
    all_sprites.update(dt)
    collisions()
    display_surface.fill('darkgray')
    all_sprites.draw(display_surface)
    display_score()



    pygame.display.update()

pygame.quit()