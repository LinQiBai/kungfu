import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


POSE_MODEL_COMPLEXITY = 1
POSE_MIN_DETECTION_CONFIDENCE = 0.5
POSE_MIN_TRACKING_CONFIDENCE = 0.5


RECOGNITION_THRESHOLD = 0.55
SCORE_WEIGHTS = {
    "angles": 0.7,
    "symmetry": 0.15,
    "stability": 0.15,
}


HOST = "0.0.0.0"
PORT = 5000
DEBUG = True
MAX_CONTENT_LENGTH = 32 * 1024 * 1024
