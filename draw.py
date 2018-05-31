#!/usr/bin/python3
import json
import os
import random
import requests
from time import sleep
from PIL import Image, ImageDraw


PICS = 'static/pics/'
DMN = 'https://techshirt-sergeysh.c9users.io/pics'

#logos = ["red", "green", "blue", "orange", "pink", "purple", "yellow", "cyan"]
#logos = ["android", "angular", "ansible", "docker", "kubernetes", "python", "react", "vue", "puppet", "grafana", "redis", "linux", "prometheus", "apache", "django"]
techs = os.listdir("logo")
#techs = ["android.png"]
# places = [((270, 255), 200), ((1195, 156), 240),
#             ((200, 153), 100), ((440, 153), 100), ((280, 470), 100), ((380, 470), 100),
#             ((1215, 410), 100), ((1315, 410), 100),
#             ((820, 180), 92),
#             ((1195, 520), 80), ((1275, 520), 80), ((1355, 520), 80),
#             ((256, 580), 80), ((336, 580), 80), ((416, 580), 80)]

# places = [((120, 125), 200),
#             ((50, 23), 100), ((290, 23), 100), ((130, 340), 100), ((230, 340), 100),
#             ((106, 450), 80), ((186, 450), 80), ((266, 450), 80)]

front_places = [((250, 750), 1300),
            ((0, 0), 700), ((1100, 0), 700),
            ((25, 2200), 400), ((450, 2200), 400), ((875, 2200), 400), ((1300, 2200), 400)]

back_places = [((0, 0), 1800),
            ((25, 1900), 400), ((450, 1900), 400), ((875, 1900), 400), ((1300, 1900), 400),
            ((25, 2350), 400), ((450, 2350), 400), ((875, 2350), 400), ((1300, 2350), 400)]

left_places = [((50, 50), 700)]

right_places = [((50, 50), 700)]


# generated_urls = {"default" : "https://image.ibb.co/d01nFy/front.png",
#         "back" : "https://image.ibb.co/eTxr8J/back.png",
#         "sleeve_left" : "https://image.ibb.co/mMM18J/left.png",
#         "sleeve_right" : "https://image.ibb.co/hYeooJ/right.png"}

generated_urls = {"default" : DMN + "front.png",
        "back" : DMN + "back.png",
        "sleeve_left" : DMN + "left.png",
        "sleeve_right" : DMN + "right.png"}

def send_shirt(urls):
    with open('tshirt.json') as data_file:
        data = json.loads(data_file.read())
    for fileim in data["files"]:
        fileim["image_url"] = urls[fileim["placement"]]

    r = requests.get('https://api.printful.com/mockup-generator/create-task/257',
        headers={'authorization': 'Basic dzd0YTd0M24tbXpyeC02YTg0OnFtbWctbjR6MXJzdWR4Ym9y'},
        json=data)

    task_key = r.json()["result"]["task_key"]
    print(task_key)
    return task_key


def wait_shirt(task_id):
    status = "no"
    while "completed" not in status:
        sleep(0.5)
        r = requests.get('https://api.printful.com/mockup-generator/task?task_key='+task_id,
            headers={'authorization': 'Basic dzd0YTd0M24tbXpyeC02YTg0OnFtbWctbjR6MXJzdWR4Ym9y'})
        status = r.json()["result"]["status"]
        print(status)

    result = r.json()["result"]["mockups"][0]
    shirt_mockups = []
    shirt_mockups.append(result["mockup_url"])
    for extra in result["extra"]:
        shirt_mockups.append(extra["url"])
    return shirt_mockups


def draw_logo(input_path, logo_files, places, output_path):
    image = Image.open(input_path).convert('RGBA')
    for place, size in places:
        if (len(logo_files) < 1):
            break
        #index = random.randint(0, len(logo_files) - 1)
        logo_file = logo_files.pop().resize((size, size), Image.BICUBIC)
        image.paste(logo_file, place, logo_file)
    image.save(output_path, "PNG")


def shirt(techs):
    logo_files = list(map(lambda logo: Image.open("logo/"+logo + ".png").convert('RGBA'), techs))
    draw_logo("empty_frontback.png", logo_files, front_places, PICS + "front.png")
    draw_logo("empty_frontback.png", logo_files, back_places, PICS + "back.png")
    draw_logo("empty_side.png", logo_files, left_places, PICS + "left.png")
    draw_logo("empty_side.png", logo_files, right_places, PICS + "right.png")

def run(t):
    shirt(t)
    wait_shirt(send_shirt(generated_urls))

if __name__ == "__main__":
    shirt(techs)
    wait_shirt(send_shirt(generated_urls))
