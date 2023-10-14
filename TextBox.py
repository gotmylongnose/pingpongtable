import pygame

class TextBox():

    def __init__(self, x, y, w, h, bgcolor, textcolor, font, dispText, border = False, bg = False):
        self.bgcolor = bgcolor
        self.textcolor = textcolor
        self.rect = pygame.Rect(x, y, w, h)
        self.font = font
        self.dispText = dispText
        self.border = border
        self.bg = bg

    def draw(self, surf):
        if self.bg:
            pygame.draw.rect(surf, self.bgcolor, self.rect) # Button Background

        if self.border:
            pygame.draw.rect(surf, (0, 0, 0), self.rect, 2) #Button Border

        msg = self.font.render(self.dispText, 1, self.textcolor)
        surf.blit(msg, msg.get_rect(center = self.rect.center))

    def update(self, event_list):
        pass
