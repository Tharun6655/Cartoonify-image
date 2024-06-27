import cv2
import sys
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from matplotlib import pyplot as plt

def cartoonify(image_path):
    original_image = cv2.imread(image_path)
    original_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)
    if original_image is None:
        print("Cannot find any image. Choose appropriate file")
        return
    
    resized1 = cv2.resize(original_image, (960, 540))
    gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    resized2 = cv2.resize(gray_image, (960, 540))
    smooth_gray = cv2.medianBlur(gray_image, 5)
    resized3 = cv2.resize(smooth_gray, (960, 540))
    edges = cv2.adaptiveThreshold(smooth_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    resized4 = cv2.resize(edges, (960, 540))
    color_image = cv2.bilateralFilter(original_image, 9, 300, 300)
    resized5 = cv2.resize(color_image, (960, 540))
    cartoon_image = cv2.bitwise_and(color_image, color_image, mask=edges)
    resized6 = cv2.resize(cartoon_image, (960, 540))
    
    images = [resized1, resized2, resized3, resized4, resized5, resized6]
    fig, axes = plt.subplots(3, 2, figsize=(8, 8), subplot_kw={'xticks': [], 'yticks': []}, gridspec_kw=dict(hspace=0.1, wspace=0.1))
    for i, ax in enumerate(axes.flat):
        ax.imshow(images[i], cmap='gray')
    plt.show()

def upload():
    image_path = filedialog.askopenfilename()
    cartoonify(image_path)

top = tk.Tk()
top.geometry('500x500')
top.title('Cartoonify Your Image!')
top.configure(background='#eadbc8')

label = Label(top, background='#eadbc8', font=('ariel', 20, 'bold'))
label.pack()

upload_button = Button(top, text="Cartoonify an Image", command=upload, padx=50, pady=10)
upload_button.configure(background='blue', foreground='white', font=('ariel', 10, 'bold'))
upload_button.pack(side=TOP, pady=200)

top.mainloop()
