class ImagePreprocessor():

    def __init__(self, image_width, image_height, 
        image_channels, rescale=None, bgr=False):

        self.image_width = image_width
        self.image_height = image_height
        self.image_channels = image_channels

        self.rescale = rescale
        self.bgr = bgr

    def process(self, image):

        image = imresize(image, (self.image_width, 
            self.image_height, self.image_channels))

        if self.rescale is not None:
            image = np.true_divide(image, 255.)

        if self.bgr:
            image = image[...,::-1]

        return image

def deprocess_image(image):
    """ 
        # Source
            https://github.com/keras-team/keras/blob/master/examples/conv_filter_visualization.py
    """
    if np.ndim(image) > 3:
        image = np.squeeze(image)
        
    image -= image.mean()
    image /= (image.std() + 1e-5)
    image *= 0.1

    image += 0.5
    image = np.clip(image, 0, 1)

    image *= 255
    
    image = np.clip(image, 0, 255).astype('uint8')
    return image

def deprocess_saliency(saliency, grayscale=False):
    if np.ndim(saliency) > 3:
        saliency = np.squeeze(saliency)

    saliency *= 255
    saliency = np.clip(saliency, 0, 255)
    
    if grayscale:
        saliency = cv2.cvtColor(saliency, cv2.COLOR_BGR2GRAY)

    return saliency

def deprocess_gradcam(image, gradcam, greyscale=False):
    if np.ndim(image) > 3:
        image = np.squeeze(image)

    image -= np.min(image)     
    image  = np.minimum(image, 255)

    gradcam = cv2.applyColorMap(np.uint8(255 * gradcam), cv2.COLORMAP_JET)
    gradcam = np.float32(gradcam) + np.float32(image)
    gradcam = 255 * gradcam / np.max(gradcam)

    if greyscale:
        gradcam = cv2.cvtColor(gradcam, cv2.COLOR_BGR2GRAY)

    return gradcam