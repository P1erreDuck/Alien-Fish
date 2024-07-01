class Settings():

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (66,170,255)

        self.ship_limit = 2

        self.bullet_width = 8
        self.bullet_height = 15
        self.bullet_color = (255,140,0)
        self.bullets_allowed = 3

        self.fleet_drop_speed = 10

        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        self.ship_speed = 1
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3.0
        self.alien_speed_factor = 0.5
        self.fleet_direction = 1
        self.alien_speed = 1.0
        self.bullet_speed = 2.0
        self.alien_points = 100

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)