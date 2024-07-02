#!/usr/bin/env python
# coding: utf-8

# In[13]:


import cv2
import matplotlib.pyplot as plt

# loading file path
image_path = r'C:\Users\SANSHIYA\Downloads\archive (13)\input_image.png'

# Step 1: Read the image in RGB format
image = cv2.imread(image_path)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Display the original image
plt.imshow(image_rgb)
plt.title('Original Image')
plt.axis('off')
plt.show()


# In[14]:


import cv2
import matplotlib.pyplot as plt

# Corrected file path
image_path = r'C:\Users\SANSHIYA\Downloads\archive (13)\input_image.png'

# Step 1: Read the image in RGB format
image = cv2.imread(image_path)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Step 2: Convert to grayscale
gray_image = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2GRAY)

# Display the grayscale image
plt.imshow(gray_image, cmap='gray')
plt.title('Grayscale Image')
plt.axis('off')
plt.show()


# In[15]:


import cv2
import matplotlib.pyplot as plt

# Corrected file path
image_path = r'C:\Users\SANSHIYA\Downloads\archive (13)\input_image.png'

# Step 1: Read the image in RGB format
image = cv2.imread(image_path)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Step 2: Convert to grayscale
gray_image = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2GRAY)

# Step 3: Invert the grayscale image
inverted_gray_image = cv2.bitwise_not(gray_image)

# Display the inverted grayscale image
plt.imshow(inverted_gray_image, cmap='gray')
plt.title('Inverted Grayscale Image')
plt.axis('off')
plt.show()


# In[17]:


import cv2
import matplotlib.pyplot as plt

# Corrected file path
image_path = r'C:\Users\SANSHIYA\Downloads\archive (13)\input_image.png'

# Step 1: Read the image in RGB format
image = cv2.imread(image_path)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Step 2: Convert to grayscale
gray_image = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2GRAY)

# Step 3: Invert the grayscale image
inverted_gray_image = cv2.bitwise_not(gray_image)

# Step 4: Apply Gaussian blur to the inverted image
blurred_image = cv2.GaussianBlur(inverted_gray_image, (21, 21), 0)

# Display the blurred image
plt.imshow(blurred_image, cmap='gray')
plt.title('Blurred Image')
plt.axis('off')
plt.show()


# In[18]:


import cv2
import matplotlib.pyplot as plt

# Corrected file path
image_path = r'C:\Users\SANSHIYA\Downloads\archive (13)\input_image.png'

# Step 1: Read the image in RGB format
image = cv2.imread(image_path)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Step 2: Convert to grayscale
gray_image = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2GRAY)

# Step 3: Invert the grayscale image
inverted_gray_image = cv2.bitwise_not(gray_image)

# Step 4: Apply Gaussian blur to the inverted image
blurred_image = cv2.GaussianBlur(inverted_gray_image, (21, 21), 0)

# Step 5: Invert the blurred image
inverted_blurred_image = cv2.bitwise_not(blurred_image)

# Display the inverted blurred image
plt.imshow(inverted_blurred_image, cmap='gray')
plt.title('Inverted Blurred Image')
plt.axis('off')
plt.show()


# In[19]:


import cv2
import matplotlib.pyplot as plt

# Corrected file path
image_path = r'C:\Users\SANSHIYA\Downloads\archive (13)\input_image.png'

# Step 1: Read the image in RGB format
image = cv2.imread(image_path)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Step 2: Convert to grayscale
gray_image = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2GRAY)

# Step 3: Invert the grayscale image
inverted_gray_image = cv2.bitwise_not(gray_image)

# Step 4: Apply Gaussian blur to the inverted image
blurred_image = cv2.GaussianBlur(inverted_gray_image, (21, 21), 0)

# Step 5: Invert the blurred image
inverted_blurred_image = cv2.bitwise_not(blurred_image)

# Step 6: Create the pencil sketch by dividing the grayscale image by the inverted blurry image
pencil_sketch = cv2.divide(gray_image, inverted_blurred_image, scale=256.0)

# Display the pencil sketch
plt.imshow(pencil_sketch, cmap='gray')
plt.title('Pencil Sketch')
plt.axis('off')
plt.show()


# In[ ]:




