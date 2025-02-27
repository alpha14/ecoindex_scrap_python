from os import chown, unlink

from PIL import Image

from ecoindex_scraper.models import ScreenShot


def convert_screenshot_to_webp(screenshot: ScreenShot) -> None:
    image = Image.open(rf"{screenshot.get_png()}")
    width, height = image.size
    ratio = 800 / height if width > height else 600 / width

    image.convert("RGB").resize(size=(int(width * ratio), int(height * ratio))).save(
        rf"{screenshot.get_webp()}",
        format="webp",
    )
    unlink(screenshot.get_png())


def set_screenshot_rights(
    screenshot: ScreenShot, uid: int | None = None, gid: int | None = None
) -> None:
    if uid and gid:
        chown(path=screenshot.get_webp(), uid=uid, gid=gid)
