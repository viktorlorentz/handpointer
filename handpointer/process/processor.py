class processor():
  """image processor
    Gets current Pointer position from image.
  """

  def __init__(self,
               follow_rate=0.1,
               process_mode='mp_hands'
               ):
    """Initializes a processor object.
    Args:
      follow_rate:
      process_mode: Which handlandmark detector to use. Available modes: "mp_hands","mp_holistic","tf"
    """
    self.show_video = show_video
    if self.show_video:
      draw._init_window()
    if webcam_video:
        self.video_capture = cv2.VideoCapture(0)
    self.pointer_position = np.array([0.5,0.5,0.5], dtype='float64')
    self.hand_position = np.array([0.5,0.5], dtype='float64')


  def get(self, image: np.ndarray= None) -> namedtuple:
    """
    Processes an RGB image and returns the pointer location and the state of the pointer.
    Args:
      image: An optional RGB image represented as a numpy ndarray.
    Raises:
    Returns:
      A namedtuple  with four fields: Coordinates x, y, z ranging from 0.0 to 1.0
        and the current state of the pointer click.
    """
    if not image and self.video_capture:
      image = self.video_capture.read()[1]

    image_height, image_width, _ = image.shape

    pointer = Pointer(x=1, y=2, z=3, active=False)

    if self.show_video:
      draw.draw_image(image)

    return pointer
