import pygame

# 초기화(반드시 필요)
pygame.init()

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Game 1") # 게임 이름

# 이벤트 루프(프로그램이 바로 종료되는 걸 막기 위해)
running = True
while running:
    for event in pygame.event.get(): # 이벤트가 발생하는 동안 실행
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가
            running = False # 게임이 진행중이 아니다
# pygmae 종료
pygame.quit