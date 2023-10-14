import pygame

class Button():

    def __init__(self, x, y, w, h, color, highlight_color, font, buttonMsg):
        self.color = color
        self.highlight_color = highlight_color
        self.rect = pygame.Rect(x, y, w, h)
        self.font = font
        self.buttonMsg = buttonMsg
        self.button_active = False

    def draw(self, surf):
        pygame.draw.rect(surf, self.highlight_color if self.button_active else self.color, self.rect) # Button Background
        pygame.draw.rect(surf, (0, 0, 0), self.rect, 2) #Button Border
        msg = self.font.render(self.buttonMsg, 1, (0, 0, 0))
        surf.blit(msg, msg.get_rect(center = self.rect.center))

    def update(self, event_list):
        mpos = pygame.mouse.get_pos()
        self.button_active = self.rect.collidepoint(mpos)

        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and self.button_active:
                    return True
                
        return False
