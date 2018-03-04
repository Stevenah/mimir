import cv2

from utils.image import process_image

def process_base64_video(video):
    video = decode_base64(video)
    video = prepare_video(video)
    return process_video(video)

def prepare_video(video):
    with open('file.mp4', 'wb') as f_vid:
        f_vid.write(video)

    return cv2.VideoCapture('file.mp4')

def process_video(video):
    frames = []
    while True:
        ret, frame = video.read()

        if not ret:
            break

        frame = process_image(frame, IMAGE_WIDTH, IMAGE_HEIGHT, 3)
        frames.append(frame)
        
    return frames