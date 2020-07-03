import regex


def calculate_dps(damage=0, damage_bonus=0, f_rate=0, f_rate_bonus=0,
                  reload_t=0, reload_t_bonus=0, mag_size=0, ammo_per_shot=1):

    try:
        if damage == '':
            damage = 0
        damage = float(damage)
    except ValueError:
        pattern = regex.compile(r'x')
        damage_num = regex.split(pattern, damage)
        damage = float(damage_num[0]) * float(damage_num[1])
    try:
        damage_bonus = float(damage_bonus)
    except ValueError:
        damage_bonus = 0
    try:
        f_rate_bonus = float(f_rate_bonus)
    except ValueError:
        f_rate_bonus = 0
    try:
        reload_t_bonus = float(reload_t_bonus)
    except ValueError:
        reload_t_bonus = 0
    try:
        ammo_per_shot = float(ammo_per_shot)
    except ValueError:
        ammo_per_shot = 1

    if f_rate == '':
        f_rate = 1
    else:
        f_rate = float(f_rate)
    if reload_t == '':
        reload_t = 1
    else:
        reload_t = float(reload_t)
    if mag_size == '':
        mag_size = 1
    else:
        mag_size = float(mag_size)

    damage_total = damage + (damage * damage_bonus / 100)
    f_rate_total = f_rate + (f_rate * f_rate_bonus / 100)
    reload_t_total = reload_t - (reload_t * reload_t_bonus / 100)
    magazine = mag_size / ammo_per_shot  # if 3 ammo per shot, like 1 mag size

    time_until_reload = magazine / f_rate_total

    damage_no_reload = damage_total * f_rate_total * time_until_reload
    dps = damage_no_reload / (time_until_reload + reload_t_total)

    return dps


if __name__ == "__main__":
    damage = calculate_dps(
        damage=input('Damage:                    '),
        damage_bonus=input('Additional damage (%):     '),
        f_rate=input('Fire rate:                 '),
        f_rate_bonus=input('Additional fire rate (%):  '),
        reload_t=input('Reload time:               '),
        reload_t_bonus=input('Improved reload time (%):  '),
        mag_size=input('Magazine size:             '),
        ammo_per_shot=input('Ammo per shot:             ')
    )

    print(f'Weapon damage: {damage} DPS')
