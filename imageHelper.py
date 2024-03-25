import os
from PIL import Image
import numpy as np

def find_images(folder_path):
    image_extensions = ['.jpg', '.png', '.jpeg', '.bmp', '.gif']  # Update or change this list based on the image files you are looking for
    image_paths = []

    for root, dirs, files in os.walk(folder_path):

        for file in files:

            if any(file.endswith(extension) for extension in image_extensions):
                image_paths.append(os.path.join(root, file))

    return image_paths
    
def binary_to_numpy(binary_image):
    numpy_array = np.array(binary_image)

    numpy_float_array = numpy_array.astype(np.int32)
    return numpy_float_array
    
def image_to_binaryNumpy(input_image_path, threshold=128, size=(16,16)):
    original_image = Image.open(input_image_path).convert('L')  # Convert image to grayscale
    resized_image = original_image.resize(size)  # Resize the image

    binary_image = resized_image.point(lambda p: p > threshold and 255)  # Apply threshold
    binary_image = binary_image.convert('1')  # Convert the image to binary format

    return binary_to_numpy(binary_image)
    
def invertBinaryArray(binary):
    return binary_to_numpy(np.logical_not(binary).astype(np.int32))
    
def getRawImageData(imagePath):
    img = Image.open(imagePath)
    arr = np.array(img)
    return arr.flatten()
    