class Tv:
    def __init__(self):
        self.is_On: bool = False
        self.chanel = 0
        self.volume = 0
        self.is_muted = False
        self.previous_volume = 0

    def turn_on(self):
            self.is_On = True

    def turn_off(self):
            self.is_On = False

    def get_chanel(self):
        return self.chanel

    def set_chanel(self, chanel):
        self.chanel = chanel

    def get_volume(self):
        return self.volume

    def set_volume(self, volume):
        self.volume = volume

    def increase_volume(self):
        self.volume += 1

    def decrease_volume(self):
        self.volume -= 1

    def get_mute(self):
        if not self.is_muted:
            self.is_muted = True
            self.previous_volume = self.volume
            self.volume = 0

        else:
            self.is_muted = False
            self.volume = self.previous_volume

    def chanel_up(self):
        self.chanel += 1

    def chanel_down(self):
        self.chanel -= 1






