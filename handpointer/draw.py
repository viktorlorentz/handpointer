import cv2
import numpy as np
import sys

window_name = 'handpointer'

def _init_window():
    global window_name
    window_name = 'handpointer'
    cv2.namedWindow(window_name,cv2.WINDOW_NORMAL)
    cv2.setWindowProperty(window_name,cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN) # this brings window to foreground
    cv2.setWindowProperty(window_name,cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_NORMAL)



def draw_image(image: np.ndarray):
    """
    Draws the results into a OpenCV window.
    Args:
      image: An RGB image represented as a numpy ndarray.
    """
    global window_name

    cv2.imshow(window_name, image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        sys.exit()