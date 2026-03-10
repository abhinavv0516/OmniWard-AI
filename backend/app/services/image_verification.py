import cv2
import numpy as np

def verify_change(before_path, after_path):

    before = cv2.imread(before_path)
    after = cv2.imread(after_path)

    # resize after image to match before image
    after = cv2.resize(after, (before.shape[1], before.shape[0]))

    before_gray = cv2.cvtColor(before, cv2.COLOR_BGR2GRAY)
    after_gray = cv2.cvtColor(after, cv2.COLOR_BGR2GRAY)

    diff = cv2.absdiff(before_gray, after_gray)

    score = np.sum(diff)

    print("Difference Score:", score)

    if score > 500000:
        return True

    return False