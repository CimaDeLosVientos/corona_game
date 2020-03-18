import sys, os
from pygame import image, error, font

# Funtions
# ---------------------------------------------------------------------
def load_image(file_path):
    """
    Loads a image from a path.

    :param      file_path:  The path where is the image
    :type       file_path:  String
    
    :returns:   The image file
    :rtype:     Surface
    """
    try:
        image_file = image.load(resource_path(file_path))
    except error:
        raise ImportError
    return image_file

def draw_text(text, pos_x, pos_y, size = 25, color = (255, 255, 255)):
    """
    
    Formats a text for can show it in the game.
    
    Arguments:
        text {String} -- The text that will be formated
        pos_x {Int} -- coordinate in x axis
        pos_y {Int} -- coordinate in y axis
        
    Keyword Arguments:
        size {Int} -- Size of the text in pp? (default: {25})
        color {tuple} -- Color of the text in RGB (default: {(255, 255, 255)})
        
    Returns:
        Font -- Font object paintable
    """
    typography = font.Font(resource_path("assets/fonts/OpenSans-Regular.ttf"), size)
    text_formated = typography.render(text, 1, color)
    text_formated_rect = text_formated.get_rect()
    text_formated_rect.center_x = pos_x
    text_formated_rect.center_y = pos_y
    
    return text_formated, text_formated_rect

def resource_path(relative):
    """
    If the application is run as a bundle, the pyInstaller bootloader
    extends the sys module by a flag frozen=True and sets the app 
    path into variable _MEIPASS'.
    """
    application_path = os.path.abspath(".")
    if getattr(sys, 'frozen', False):
        application_path = sys._MEIPASS

    return os.path.join(application_path, relative).replace("/", os.sep)