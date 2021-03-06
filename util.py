import cfg
import re


def get_ep(raider_name):
    return cfg.raider_dict[raider_name].ep


def get_gp(raider_name):
    return cfg.raider_dict[raider_name].gp


def set_ep(raider_name, ep):
    cfg.raider_dict[raider_name].ep = ep


def set_gp(raider_name, gp):
    cfg.raider_dict[raider_name].gp = gp


def calculate_pr(raider_name):
    return round(get_ep(raider_name) / get_gp(raider_name), 3)


def find_raider_name(user_id):
    for raider in cfg.raider_dict.values():
        if (user_id in raider.user_id):
            return raider.name

    return None


def is_match(reg, content):
    return re.fullmatch(reg, content, re.IGNORECASE)
