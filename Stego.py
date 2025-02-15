import cv2
import os
import numpy as np

# Use raw string or double backslashes for paths
img_path =(r"C:/Users/binoc/Desktop/Stego/R.jpeg")
output_path = (r"C:/Users/binoc/Desktop/Stego/New folder/stego.bmp")

img = cv2.imread(img_path)  # Read the image

if img is None:
    print("Error: Image not found!")
    exit()

msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

# Convert message to byte values (UTF-8 encoding)
msg_bytes = msg.encode("utf-8")
msg_length = len(msg_bytes)

# Ensure image can hold the message
height, width, _ = img.shape
max_bytes = height * width * 3  # Total bytes available in RGB channels

if msg_length > max_bytes:
    print("Error: Message is too long for this image!")
    exit()

# Embed message in image
idx = 0
for row in range(height):
    for col in range(width):
        for channel in range(3):  # Iterate over RGB channels
            if idx < msg_length:
                img[row, col, channel] = msg_bytes[idx]
                idx += 1
            else:
                break

cv2.imwrite(output_path, img)
os.system(f'start "" "{output_path}"')  # Open image on Windows

# **Decryption**
message = []
idx = 0

pas = input("Enter passcode for Decryption: ")
if password == pas:
    for row in range(height):
        for col in range(width):
            for channel in range(3):
                if idx < msg_length:
                    message.append(img[row, col, channel])
                    idx += 1
                else:
                    break
    decrypted_msg = bytes(message).decode("utf-8")
    print("Decryption message:", decrypted_msg)
else:
    print("YOU ARE NOT authorized")
