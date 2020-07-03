import webbrowser
from kivymd.app import MDApp
from calculator import calculate_dps
from kivy.lang import Builder


class DPSCalculatorApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = 'Dark'
        return Builder.load_file('DPSCalculator.kv')

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

    def github(self):
        webbrowser.open('https://github.com/SpacewaIker/bl3-dps-calculator',
                        new=2)

    def no_action(self):
        pass


if __name__ == "__main__":
    DPSCalculatorApp().run()
