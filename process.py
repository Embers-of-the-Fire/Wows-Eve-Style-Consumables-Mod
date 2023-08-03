import os
from PIL import Image


def get_files(dir_path: str):
    raw = os.path.join(dir_path, "EVE Raw")
    res = os.path.join(dir_path, "EVE Result")
    for file in os.listdir(raw):
        yield os.path.join(raw, file), os.path.join(res, file)


def scale(img_path: str, save_path: str):
    img = Image.open(img_path)
    img_res = img.resize((60, 60))
    img_res.save(save_path)


def process(path: str):
    for raw, res in get_files(path):
        scale(raw, res)


process(r"D:\WowsMods - Dev\EVE - Consumables Icon\Aircraft Consumable")
process(r"D:\WowsMods - Dev\EVE - Consumables Icon\Consumable - Common")
