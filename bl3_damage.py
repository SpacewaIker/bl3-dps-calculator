import re


def dps():
    damage = input('Damage:                    ')
    add_damage = input('Additional damage (%):     ')
    rate = float(input('Fire rate:                 '))
    add_rate = input('Additional fire rate (%):  ')
    reload_ = float(input('Reload time:               '))
    add_reload = input('Improved reload time (%):  ')
    mag_size = float(input('Magazine size:             '))
    ammo_shot = input('Ammo per shot:             ')

    try:
        damage = float(damage)
    except ValueError:
        pattern = re.compile(r'x')
        damage_num = re.split(pattern, damage)
        damage = float(damage_num[0]) * float(damage_num[1])
    try:
        add_damage = float(add_damage)
    except ValueError:
        add_damage = 0
    try:
        add_rate = float(add_rate)
    except ValueError:
        add_rate = 0
    try:
        add_reload = float(add_reload)
    except ValueError:
        add_reload = 0
    try:
        ammo_shot = float(ammo_shot)
    except ValueError:
        ammo_shot = 1

    damage_total = damage + (damage * add_damage / 100)
    rate_total = rate + (rate * add_rate / 100)
    reload_total = reload_ - (reload_ * add_reload / 100)
    magazine = mag_size / ammo_shot  # if 3 ammo per shot, like 1 mag size

    time_until_reload = magazine / rate_total

    damage_no_reload = damage_total * rate_total * time_until_reload
    dps = damage_no_reload / (time_until_reload + reload_total)

    print(f'\nWeapon damage: {dps:,} DPS')
