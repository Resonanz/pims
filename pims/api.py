import warnings

from pims.image_sequence import ImageSequence


def require_cv2_Video(*args, **kwargs):
    raise ImportError("""To import frames from video files, you must install
OpenCV and the Python module cv2.""")


def require_cv2_tools(*args, **kwargs):
    raise ImportError("""To use video tools, you must install
OpenCV and the Python module cv2.""")


def require_libtiff(*args, **kwargs):
    raise ImportError("""To import tiff stacks, you must install libtiff.""")


try:
    import cv2
except ImportError:
    Video = require_cv2_Video
    play = require_cv2_tools
else:
    from pims.video import Video
    from pims.annotate import circle
    from pims.playback import play

try:
    import libtiff
except ImportError:
    TiffStack = require_libtiff
else:
    from pims.tiff_stack import TiffStack
