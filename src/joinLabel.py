"""
Program that converts source .jpg satellite images to a row of pixel
values while appending a label
"""

import numpy as np
import glob
import csv

# Load RGB values from source image
def imageOpen(inputImage):
    image = plt.imread(inputImage, format='jpeg')[:,:,0:3]
    # Return the pixel average of input image    
    # Drop .jpg and '/'
    return inputImage.split('/')[-1][:-4], image.flatten()

def get_vector(key):
    with open("cleanTrainVector.csv", 'r') as f:
        for line in f.readlines()[0:]:
            s_line = line.strip().split(',')
            i_name, vec = s_line[0], s_line[1:]
            if i_name == key:
                return vec
    raise ValueError("nothing")
def globber():
    with open("cleanLabelImages.csv", 'w') as f:
        csvwriter = csv.writer(f, delimiter=',')
        counter = 0
        for filename in glob.iglob('/gpudata/kaggle/amazon/train-jpg/*.jpg'):
            
            key, image = imageOpen(filename)
            label = get_vector(key)
            label_image = label + list(image)
            csvwriter.writerow(label_image)
            # label = ",".join( [ i for i in get_vector(key) ] 
            # f.write("{},{}\n".format(label, image))


if __name__ == "__main__":
    globber()
