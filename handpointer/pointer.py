# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""handpointer"""

import cv2
import numpy as np
from collections import namedtuple

from . import draw

Pointer = namedtuple("Pointer", ["x", "y", "z", "active"])


class pointer():
  """handpointer pointer
    Handpointer processes a videostream and gives back a 3d position.
  """

  def __init__(self,
               show_video=True,
               webcam_video=True,
               draw_info=True,
               draw_cursor=True,
               draw_landmarks=True,
               follow_rate=0.1,
               process_mode='mp_hands'
               ):
    """Initializes a handpointer object.
    Args:
      show_video: Enable to show webcam stream in a window.
      webcam_video:
      draw_info:
      draw_cursor:
      draw_landmarks:
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

  def process_image(self, image: np.ndarray) -> namedtuple:
    """
    Processes an RGB image and returns the pointer location and the state of the pointer.
    Args:
      image: An optional RGB image represented as a numpy ndarray.
    Raises:
    Returns:
      A namedtuple  with four fields: Coordinates x, y, z ranging from 0.0 to 1.0
        and the current state of the pointer click.
    """
    return
