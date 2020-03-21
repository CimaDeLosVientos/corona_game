# Display
MASTER_VOLUMEN = 0.1
#WIDTH  = 1920
#HEIGHT = 1080
WIDTH  = 1280
HEIGHT = 720
ASPECT_RELATION_PLAYER = 2.4
ASPECT_RELATION_CHAT = 0.6
WIDTH_PLAYER_SPRITE = 100
HEIGHT_CHAT = 680
WIDTH_OBJECT = 100
WIDTH_OBJECT_ICON = 20

PLAYER_SURFACE = (WIDTH_PLAYER_SPRITE, int(WIDTH_PLAYER_SPRITE * ASPECT_RELATION_PLAYER))
CHAT_SURFACE = (int(HEIGHT_CHAT * ASPECT_RELATION_CHAT), HEIGHT_CHAT)
OBJECT_SURFACE = (WIDTH_OBJECT, WIDTH_OBJECT)
OBJECT_SURFACE_ICON = (WIDTH_OBJECT_ICON, WIDTH_OBJECT_ICON)


# Locations menus
PLAY_BUTTON = (430, 325)
PLAY_STORY_MODE_BUTTON = (800, 310)
PLAY_SURIVAL_MODE_BUTTON = (800, 415)
HOW_TO_PLAY_BUTTON = (430, 550)
CREDITS_BUTTON = (430, 435)
BACK_BUTTON = (800, 530)

NEXT_CHAT_BUTTON = (int(WIDTH * (4 / 5)), int(HEIGHT * (4 / 5)))
START_LEVEL_BUTTON = (int(WIDTH / 2), int(HEIGHT / 2))
NEXT_LEVEL_BUTTON = (int(WIDTH / 2), int(HEIGHT / 2))
EXIT_BUTTON = (int(WIDTH / 2), int(HEIGHT / 2))



# Level config
LEVEL_TIME = 120
FALL_SPEED = 0.5
PLAYER_SPEED = 0.5
LEFT_LIMIT = 30
RIGHT_LIMIT = WIDTH - LEFT_LIMIT
GROUND_LEVEL = HEIGHT - 175
BOTTOM_LIMIT = HEIGHT + 100
INITIAL_HEALTH = 30
FRAME_PER_SPRITE = 5

# Level 1
RATIO_NEW_OBJECT_LEVEL_1 = 0.03
RATIO_OBJECT_1_LEVEL_1 = RATIO_NEW_OBJECT_LEVEL_1 + RATIO_NEW_OBJECT_LEVEL_1 * 0.3
RATIO_OBJECT_2_LEVEL_1 = RATIO_OBJECT_1_LEVEL_1 + RATIO_NEW_OBJECT_LEVEL_1 * 0.3
RATIO_BAD_OBJECT_LEVEL_1 = RATIO_OBJECT_2_LEVEL_1 + RATIO_NEW_OBJECT_LEVEL_1 * 0.4
OBJECT_1_NEEDS_LEVEL_1 = 20
OBJECT_2_NEEDS_LEVEL_1 = 20

# Level 2
RATIO_NEW_OBJECT_LEVEL_2 = 0.03
RATIO_OBJECT_1_LEVEL_2 = RATIO_NEW_OBJECT_LEVEL_2 + RATIO_NEW_OBJECT_LEVEL_2 * 0.3
RATIO_OBJECT_2_LEVEL_2 = RATIO_OBJECT_1_LEVEL_2 + RATIO_NEW_OBJECT_LEVEL_2 * 0.3
RATIO_BAD_OBJECT_LEVEL_2 = RATIO_OBJECT_2_LEVEL_2 + RATIO_NEW_OBJECT_LEVEL_2 * 0.4
OBJECT_1_NEEDS_LEVEL_2 = 20
OBJECT_2_NEEDS_LEVEL_2 = 20

# Level 3
RATIO_NEW_OBJECT_LEVEL_3 = 0.03
RATIO_OBJECT_1_LEVEL_3 = RATIO_NEW_OBJECT_LEVEL_3 + RATIO_NEW_OBJECT_LEVEL_3 * 0.3
RATIO_OBJECT_2_LEVEL_3 = RATIO_OBJECT_1_LEVEL_3 + RATIO_NEW_OBJECT_LEVEL_3 * 0.3
RATIO_BAD_OBJECT_LEVEL_3 = RATIO_OBJECT_2_LEVEL_3 + RATIO_NEW_OBJECT_LEVEL_3 * 0.4
OBJECT_1_NEEDS_LEVEL_3 = 20
OBJECT_2_NEEDS_LEVEL_3 = 20

# Level 4
RATIO_NEW_OBJECT_LEVEL_4 = 0.03
RATIO_OBJECT_1_LEVEL_4 = RATIO_NEW_OBJECT_LEVEL_4 + RATIO_NEW_OBJECT_LEVEL_4 * 0.3
RATIO_OBJECT_2_LEVEL_4 = RATIO_OBJECT_1_LEVEL_4 + RATIO_NEW_OBJECT_LEVEL_4 * 0.3
RATIO_BAD_OBJECT_LEVEL_4 = RATIO_OBJECT_2_LEVEL_4 + RATIO_NEW_OBJECT_LEVEL_4 * 0.4
OBJECT_1_NEEDS_LEVEL_4 = 20
OBJECT_2_NEEDS_LEVEL_4 = 20

# Level 5
RATIO_NEW_OBJECT_LEVEL_5 = 0.03
RATIO_OBJECT_1_LEVEL_5 = RATIO_NEW_OBJECT_LEVEL_5 + RATIO_NEW_OBJECT_LEVEL_5 * 0.3
RATIO_OBJECT_2_LEVEL_5 = RATIO_OBJECT_1_LEVEL_5 + RATIO_NEW_OBJECT_LEVEL_5 * 0.3
RATIO_BAD_OBJECT_LEVEL_5 = RATIO_OBJECT_2_LEVEL_5 + RATIO_NEW_OBJECT_LEVEL_5 * 0.4
OBJECT_1_NEEDS_LEVEL_5 = 20
OBJECT_2_NEEDS_LEVEL_5 = 20


# HUB
TIMER_LOCATION = (int(WIDTH / 2), 30)
OBJECT_1_ICON_LOCATION = (int(WIDTH / 2) - 95, 30)
OBJECT_1_COUNTER_LOCATION = (int(WIDTH / 2) - 70, 30)
OBJECT_2_ICON_LOCATION = (int(WIDTH / 2) + 90, 30)
OBJECT_2_COUNTER_LOCATION = (int(WIDTH / 2) + 70, 30)
HEALTH_BAR_PORTION_SIZE = (int(WIDTH / (2 * INITIAL_HEALTH)), 15)
HEALTH_LOCATION = (int(WIDTH / 2), HEIGHT - 20)