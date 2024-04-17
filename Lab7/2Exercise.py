import pygame

pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("Naruto Shippuden Openings player")

font = pygame.font.Font("Nexus_Font.TTF" , 24)

Black = (0 , 0 , 0)
screen.fill((255,255,255))

pygame.mixer.init()

playlist = ["C:\\Users\\user\\Desktop\\PP2Labs\\naruto-2-sezon-1-openning.mp3" , "C:\\Users\\user\\Desktop\\PP2Labs\\naruto-shipuden--2-sezon-2-opening.mp3" , "C:\\Users\\user\\Desktop\\PP2Labs\\Наруто-2сезон3опенинг(весь)_(muzmo.su).mp3" , "C:\\Users\\user\\Desktop\\PP2Labs\\naruto-2-sezon-opening-4.mp3" , "C:\\Users\\user\\Desktop\\PP2Labs\\(Наруто-2сезон5опенинг)-HotarunoHikari-Sha-lala_(muzmo.su).mp3"]
current_track = 0
playing = False

def draw_text(text , font , surface , x ,y , color):
    text_obj = font.render(text , True , color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x,y)
    surface.blit(text_obj , text_rect)
    
def play_music(track):
    pygame.mixer.music.load(track)
    pygame.mixer.music.play()
    
def stop_music():
    pygame.mixer.music.stop()
    
def next_track():
    global current_track
    current_track = (current_track + 1) % len(playlist)
    play_music(playlist[current_track])
    
def previous_track():
    global current_track
    current_track = (current_track - 1) % len(playlist)
    play_music(playlist[current_track])
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if playing:
                    stop_music()
                    playing = False
                else:
                    play_music(playlist[current_track])
                    playing = True
            elif event.key == pygame.K_n:
                next_track()
                playing = True
            elif event.key == pygame.K_p:
                previous_track()
                playing = True
    screen.fill((255 , 255 , 255))          
    status_text = "Playing" if playing else "Paused"

    draw_text(status_text,font,screen,10,10,Black)
    draw_text("Press SPACE to play/pause" , font , screen , 10 , 40 , Black)
    draw_text("Press N for next track" , font , screen , 10 , 70 , Black)
    draw_text("Press P for previous track" , font , screen , 10 , 100 , Black)
    
    pygame.display.update()
     