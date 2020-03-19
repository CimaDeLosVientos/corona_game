#WIDTH  = 1920
#HEIGHT = 1080
WIDTH  = 1366
HEIGHT = 720
LEVEL_TIME = 120

LEFT_LIMIT = 30
RIGHT_LIMIT = WIDTH - LEFT_LIMIT
GROUND_LEVEL = HEIGHT - 70
BOTTOM_LIMIT = HEIGHT + 100
INITIAL_HEALT = 30
HEALT_BAR_PORTION_SIZE = (int(WIDTH / (2 * INITIAL_HEALT)), 15)

# Locations
TIMER_LOCATION = (int(WIDTH / 2), 30)
OBJECT_1_ICON_LOCATION = (int(WIDTH / 2) - 95, 30)
OBJECT_1_COUNTER_LOCATION = (int(WIDTH / 2) - 70, 30)
OBJECT_2_ICON_LOCATION = (int(WIDTH / 2) + 90, 30)
OBJECT_2_COUNTER_LOCATION = (int(WIDTH / 2) + 70, 30)
HEALT_LOCATION = (int(WIDTH / 2), HEIGHT - 20)
