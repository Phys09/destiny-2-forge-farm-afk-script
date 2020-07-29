import pyautogui as pg
import time

pg.FAILSAFE = True
width, height = pg.size()


def forge_farm():
    """
    Precondition: Player is in orbit and director button is visible

    Perform the operations to launch the forge from orbit
    """
    time.sleep(3)
    pg.moveTo(width/2, (4/5)*height)  # director button
    pg.click()  # click on the director
    time.sleep(3)
    pg.moveTo(width/2, height/2)  # move cursor to earth
    pg.click()
    time.sleep(3)
    pg.moveTo(150, height-100)  # forge icon
    pg.click()
    time.sleep(1)

    # start forge button
    pg.moveTo((3/4)*width, (5/6)*height)
    time.sleep(1)
    pg.click()
    time.sleep(40)  # give time to find match


def return_to_orbit():
    """
    Return the player to orbit from any menu
    Press escape multiple times then click on dismiss on exit menu
    """
    for i in range(3):
        pg.press('esc')
        time.sleep(1)
    pg.moveTo(1680, 760)
    pg.click()


# start script
while True:
    time.sleep(3)
    return_to_orbit()
    forge_farm()
