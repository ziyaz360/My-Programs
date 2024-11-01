import os
import matplotlib.pyplot as plt

# Set the dimensions for a 16:9 ratio image
width = 16
height = 9

# Define the directory and file path
directory = 'C:/Users/z9834/Documents/Python code'
image_path = os.path.join(directory, 'earn_wallpaper.png')

# Ensure the directory exists
os.makedirs(directory, exist_ok=True)

# Create the figure and axis
fig, ax = plt.subplots(figsize=(width, height))

# Set the background color
fig.patch.set_facecolor('grey')

# Hide the axes
ax.axis('off')

# Add the text
ax.text(0.5, 0.5, 'Learn', color='black', fontsize=100, ha='center', va='center', fontweight='bold')

# Save the image
plt.savefig(image_path, bbox_inches='tight', pad_inches=0, facecolor='grey')
plt.close(fig)

print(f"Image saved at {image_path}")

