""" Doing the tests with your naked eyes """
import pathlib

import PIL.Image
import PIL.ImageFont
from util import *

from pylf import *


def test_handwrite():
    template = dict(
        background=PIL.Image.open(get_path("data/backgrounds/letter.png")),
        box=(68, 130, 655, 925),
        font=get_default_font(),
        font_size=27,
        line_spacing=6
    )
    for file in pathlib.Path(get_path("data/texts")).iterdir():
        print(file)
        with file.open() as f:
            text = f.read()
        images = handwrite(text, template)
        for im in images:
            im.show()
        assert input("Like it? [Y/N] ").upper() == 'Y'


def test_handwrite2():
    template2 = dict(
        page_settings=[
            dict(
                background=PIL.Image.open(get_path("data/backgrounds/even-odd-letter/村庄信笺纸.jpg")),
                box=(20, 107, 1285, 1110),
                font_size=37,
            ),
            dict(
                background=PIL.Image.open(get_path("data/backgrounds/even-odd-letter/树信笺纸.jpg")),
                box=(20, 107, 1285, 900),
                font_size=37,
            ),
        ],
        font=get_default_font(),
    )
    for file in pathlib.Path(get_path("data/texts")).iterdir():
        print(file)
        with file.open() as f:
            text = f.read()
        images = handwrite2(text, template2)
        for im in images:
            im.show()
        assert input("Like it? [Y/N] ").upper() == 'Y'



if __name__ == '__main__':
    print("""Test by naked eyes:""")
    # Testing handwrite2 is enough.
    # print("""======================================
    # Test: pylf.handwrite""")
    # test_handwrite()
    print("""======================================
    Test: pylf.handwrite2""")
    test_handwrite2()