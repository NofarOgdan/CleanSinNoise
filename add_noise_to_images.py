import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Create a function to apply sinusoidal noise to an RGB image
def apply_sinusoidal_noise(image, frequency=1.0, amplitude=1.0):
    image_shape = image.shape[:2]
    x = np.arange(0, image_shape[0])
    y = np.arange(0, image_shape[1])
    xx, yy = np.meshgrid(x, y)

    # Generate sinusoidal noise for each channel
    noise_r = amplitude * np.sin(2 * np.pi * frequency * xx / image_shape[0])
    noise_g = amplitude * np.sin(2 * np.pi * frequency * xx / image_shape[0])
    noise_b = amplitude * np.sin(2 * np.pi * frequency * xx / image_shape[0])

    # Add the noise to each channel
    noisy_image = np.stack([
        np.clip(image[:, :, 0] + noise_r.T, 0, 255),
        np.clip(image[:, :, 1] + noise_g.T, 0, 255),
        np.clip(image[:, :, 2] + noise_b.T, 0, 255)
    ], axis=-1).astype(np.uint8)

    return noisy_image

# Specify the directory containing your input images and the directory where you want to save the noisy images
input_directory = 'input_images/'
output_directory = 'noisy_images/'

# Create the output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# List all files in the input directory
input_files = os.listdir(input_directory)

# Loop through each image file in the input directory
for input_file in input_files:
    # Read the input image using OpenCV
    if input_file == '.DS_Store':
        continue
    input_image_path = os.path.join(input_directory, input_file)
    image = cv2.imread(input_image_path)
    print(input_file)
    freq = np.abs(np.random.normal(0,100))
    amp = np.random.randint(0,200)
    # Apply sinusoidal noise to the image
    noisy_image = apply_sinusoidal_noise(image, frequency=freq, amplitude=amp)

    # Save the noisy image to the output directory with the same filename
    output_image_path = os.path.join(output_directory, str(freq)+".JPG")
    cv2.imwrite(output_image_path, noisy_image)

    # Optionally, display or further process the noisy image
    #plt.imshow(cv2.cvtColor(noisy_image, cv2.COLOR_BGR2RGB))
    #plt.title('Noisy Image')
    #plt.show()
