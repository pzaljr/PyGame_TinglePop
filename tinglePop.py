""" tinglePop.py
    Pete Zalabowski
    12/15/09
    Creates an image that when collieded with makes a sound
    in this case we pop that annoying-as-hell elf dude from zelda
    for chapter 6,
    modified spriteGroup.py """
    
import pygame, collisionObjects2
pygame.init()

def main():
    screen = pygame.display.set_mode((628, 446))
    pygame.display.set_caption("Pop Tingle out of the Sky!")
    
    background = pygame.Surface(screen.get_size())
    background.fill((255, 255, 255))
    background = pygame.image.load('img/kvillage.gif')
    screen.blit(background, (0, 0))
    
    circle = collisionObjects2.Circle()
    squeakerGroup = pygame.sprite.Group()
    for i in range(10):
        squeaker = collisionObjects2.Squeaker(screen, "img/tingle.gif")
        squeakerGroup.add(squeaker)
        
    basicSprites = pygame.sprite.Group(circle)

    #create sound
    gameSqueak = pygame.mixer.Sound("sound/pop.wav")
    
    keepGoing = True
    clock = pygame.time.Clock()
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            #gameSqueak.play()
        spriteCrash =  pygame.sprite.spritecollide(circle, squeakerGroup, True)
        for squeaker in spriteCrash:
            squeaker.squeakerMusic()
            
            
        squeakerGroup.clear(screen, background)
        basicSprites.clear(screen, background)
        
        squeakerGroup.update()
        basicSprites.update()
        
        squeakerGroup.draw(screen)
        basicSprites.draw(screen)
    
        pygame.display.flip()
        
if __name__ == "__main__":
    main()

