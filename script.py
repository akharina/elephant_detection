import pandas as pd
import numpy as np
import os
from PIL import Image


def check_duplicates(df1):
    if df1.duplicated().sum():
        print("There were {} duplicates and they have been removed".format(
            df1.duplicated().sum()))
        df1.drop_duplicates(inplace=True)
    else:
        print("You are all clear of duplicates")

    return None


def show_image(list_img_name):
    for image in list_img_name:
        img = Image.open(f'../data/test_images/{image}.jpg')
        img.show()