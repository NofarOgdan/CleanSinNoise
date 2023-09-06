import os
import random
import shutil

# Specify the source directory containing your photos
source_directory = 'noisy_images/'

# Specify the destination directories for the training and testing sets
train_directory = 'train/'
test_directory = 'test/'

# Create the train and test directories if they don't exist
if not os.path.exists(train_directory):
    os.makedirs(train_directory)
if not os.path.exists(test_directory):
    os.makedirs(test_directory)

# Define the ratio of photos to be included in the test set (e.g., 20%)
test_ratio = 0.2

# List all files in the source directory (assuming all are photos)
photo_files = os.listdir(source_directory)

# Calculate the number of files to move to the test set
num_test_files = int(len(photo_files) * test_ratio)

# Randomly select files for the test set
test_files = random.sample(photo_files, num_test_files)

# Move the selected test files to the test directory
for file_name in test_files:
    source_path = os.path.join(source_directory, file_name)
    test_path = os.path.join(test_directory, file_name)
    shutil.move(source_path, test_path)

# Move the remaining files (training set) to the train directory
for file_name in os.listdir(source_directory):
    source_path = os.path.join(source_directory, file_name)
    train_path = os.path.join(train_directory, file_name)
    shutil.move(source_path, train_path)

# Optionally, print information about the split
print(f"Total photos: {len(photo_files)}")
print(f"Training set size: {len(photo_files) - num_test_files}")
print(f"Testing set size: {num_test_files}")
