import pygame.font


class FpsCount:
    """Init fps count"""
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings

        # Font settings
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 35)

        # Prepare source image
        self.prep_count(0)

    def prep_count(self, fps):
        """Transform fps number to a graphic image"""
        fps_count = "fps: {}".format(fps)

        self.fps_count_image = self.font.render(fps_count, True, self.text_color, self.ai_settings.bg_color)

        # Align fps to center top
        self.fps_count_rect = self.fps_count_image.get_rect()
        self.fps_count_rect.centerx = self.screen_rect.centerx
        self.fps_count_rect.left = 10
        self.fps_count_rect.bottom = self.screen_rect.bottom - 30

    def show_fps(self):
        """Show fps count"""
        self.screen.blit(self.fps_count_image, self.fps_count_rect)