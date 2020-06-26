from kivymd.app import MDApp
from calculator import calculate_dps
from kivy.core.window import Window

size = 35
Window.size = (size*9, size*16)


class DPSCalculatorApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = 'Dark'

    def action(self):
        dps = calculate_dps(
            damage=self.root.ids.tf_damage.text,
            damage_bonus=self.root.ids.tf_damage_bonus.text,
            f_rate=self.root.ids.tf_f_rate.text,
            f_rate_bonus=self.root.ids.tf_f_rate_bonus.text,
            reload_t=self.root.ids.tf_reload_t.text,
            reload_t_bonus=self.root.ids.tf_reload_t_bonus.text,
            mag_size=self.root.ids.tf_mag_size.text,
            ammo_per_shot=self.root.ids.tf_ammo_per_shot.text
        )
        self.root.ids.b_bar.title = f'{str(round(dps, 2))} DPS'

    def navigation(self):
        print('menu was pressed')

    def no_action(self):
        pass


if __name__ == "__main__":
    DPSCalculatorApp().run()
