import pygame

class OptionBox():

    def __init__(self, x, y, w, h, color, highlight_color, font, option_list, maxoptions, selected = 0):
        self.color = color
        self.highlight_color = highlight_color
        self.rect = pygame.Rect(x, y, w, h)
        self.font = font
        self.option_list = option_list
        self.selected = selected
        self.draw_menu = False
        self.menu_active = False
        self.active_option = -1
        self.maxoptions = maxoptions
        self.curscroll = 0

    def draw(self, surf):

        if len(self.option_list) <= self.selected:
            self.selected = 0

        pygame.draw.rect(surf, self.highlight_color if self.menu_active else self.color, self.rect) # Button Background
        pygame.draw.rect(surf, (0, 0, 0), self.rect, 2) #Button Border
        msg = self.font.render(self.option_list[self.selected], 1, (0, 0, 0))
        surf.blit(msg, msg.get_rect(center = self.rect.center))

        if self.draw_menu:

            if len(self.option_list) <= self.maxoptions:
                option_list_short = self.option_list
            else:
                option_list_short = self.option_list[self.curscroll:(self.curscroll+self.maxoptions)]
    
            for i, text in enumerate(option_list_short):
                if i != 0:
                    rect = self.rect.copy()
                    rect.y += (i+1) * self.rect.height/2
                    rect.height = self.rect.height/2
                    pygame.draw.rect(surf, self.highlight_color if i == self.active_option else self.color, rect)
                    msg = self.font.render(text, 1, (0, 0, 0))
                    surf.blit(msg, msg.get_rect(center = rect.center))
            # Button Border        
            outer_rect = (self.rect.x, self.rect.y + self.rect.height, self.rect.width, self.rect.height/2 * (len(option_list_short)-1))
            pygame.draw.rect(surf, (0, 0, 0), outer_rect, 2)

    def update(self, event_list):
        mpos = pygame.mouse.get_pos()
        self.menu_active = self.rect.collidepoint(mpos)
        
        self.active_option = -1

        for i in range(len(self.option_list) if len(self.option_list) <= self.maxoptions else self.maxoptions):
            if i != 0:
                rect = self.rect.copy()
                rect.y += (i+1) * self.rect.height/2
                rect.height = self.rect.height/2
                if rect.collidepoint(mpos):
                    self.active_option = i
                    break
        
        if not self.menu_active and self.active_option == -1:
            self.draw_menu = False

        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.menu_active:
                        self.draw_menu = not self.draw_menu
                    elif self.draw_menu and self.active_option >= 0:
                        self.selected = self.active_option + self.curscroll
                        self.draw_menu = False
                        return self.active_option + self.curscroll
                elif event.button == 4:
                    if self.curscroll > 0:
                        self.curscroll = self.curscroll - 1
                elif event.button == 5:
                    if self.curscroll + self.maxoptions < len(self.option_list):
                        self.curscroll = self.curscroll + 1
                
        return -1

    def curSelection(self):
        return self.option_list[self.selected]
