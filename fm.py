import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import os

def bruthForce():
    folder_path = r'D:\Projects\future_matching\New folder'
    img1path = os.path.join(folder_path, 'img1.JPG')
    img2path = os.path.join(folder_path, 'img2.JPG')
    

    if not os.path.exists(img1path):
        print(f"Error: Image not found at {img1path}")
        return
    if not os.path.exists(img2path):
        print(f"Error: Image not found at {img2path}")
        return
        
    img1 = cv.imread(img1path, cv.IMREAD_GRAYSCALE)
    img2 = cv.imread(img2path, cv.IMREAD_GRAYSCALE)

  
    if img1 is None:
        print(f"Error: Could not load image from {img1path}")
        return
    if img2 is None:
        print(f"Error: Could not load image from {img2path}")
        return

    orb = cv.ORB_create()
    keypoints1, descriptors1 = orb.detectAndCompute(img1, None)
    keypoints2, descriptors2 = orb.detectAndCompute(img2, None)

    br = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)
    matches = br.match(descriptors1, descriptors2)

    matches = sorted(matches, key=lambda x: x.distance)

    nMaches = 20
    imgMatch = cv.drawMatches(img1, keypoints1, img2, keypoints2, matches[:nMaches], None, flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    
    plt.figure()
    plt.imshow(imgMatch)
    plt.show() # Add plt.show() to display the plot


bruthForce()