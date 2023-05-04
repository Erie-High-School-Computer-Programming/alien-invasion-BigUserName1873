

class Settings:
    def __init__(self):
        self.screen_width = 1600
        self.screen_height = 1000
        self.bg_color = (0, 211, 0)
        

        self.ship_limit = 3


        self.bullet_width = 500
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        self.fleet_drop_speed = 10

        self.speedup_scale = 1.1

        self.score_scale = 1.5

        self.buffed_alien_scale = 1.75

        self.initialize_dynamic_settings()



    def increase_speed(self):
            self.ship_speed *= self.speedup_scale
            self.bullet_speed *= self.speedup_scale
            self.alien_speed *= self.speedup_scale
            self.alien_points = int(self.alien_points*self.score_scale)



    def initialize_dynamic_settings(self):
            self.ship_speed = 0.5
            self.bullet_speed = 1.5
            self.alien_speed = 0.5
            self.fleet_direction = 1
            self.alien_points = 50