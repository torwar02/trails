import numpy as np
from PIL import Image

def combined_display(image, matte):
    """
    Combine an input image with its corresponding matte (alpha channel) for display.

    Parameters:
    - image: PIL.Image or ndarray
        Input image to be combined.
    - matte: PIL.Image or ndarray
        Corresponding matte (alpha channel) for the input image.

    Returns:
    - combined: PIL.Image
        Combined image displaying the original image, predicted foreground, and matte.
    - middle_image: PIL.Image
        Image representing the predicted foreground extracted from the combined image.
    """
    # calculate display resolution
    w, h = image.width, image.height
    rw, rh = 800, int(h * 800 / (3 * w))

    # obtain predicted foreground
    image = np.asarray(image)
    if len(image.shape) == 2:
        image = image[:, :, None]
    if image.shape[2] == 1:
        image = np.repeat(image, 3, axis=2)
    elif image.shape[2] == 4:
        image = image[:, :, 0:3]
    matte = np.repeat(np.asarray(matte)[:, :, None], 3, axis=2) / 255
    foreground = image * matte + np.full(image.shape, 255) * (1 - matte)

    # combine image, foreground, and alpha into one line
    combined = np.concatenate((image, foreground, matte * 255), axis=1)
    combined = Image.fromarray(np.uint8(combined)).resize((rw, rh))

    # extract the middle image
    middle_image = Image.fromarray(np.uint8(foreground))

    return combined, middle_image
