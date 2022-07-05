from image import Image
import numpy as np

def brighten(image, factor):
    # when we brighten, we just want to make each channel higher by some amount 
    # factor is a value > 0, how much you want to brighten the image by (< 1 = darken, > 1 = brighten)
    x_pixels, y_pixels, num_channels = image.array.shape # get the size and channel from the image.py module into an array
    # making a copy of the original image so we won't change the original one.
    new_im = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)  

    new_im.array = image.array * factor
    
    return new_im

def adjust_contrast(image, factor, mid=0.5):
    # adjust the contrast by increasing the difference from the user-defined midpoint (0.5) by factor amount
    x_pixels, y_pixels, num_channels = image.array.shape # get the size and channel from the image.py module
    # making a copy of the original image so we won't change the original one.
    new_im = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)  

    #non-verctorized
    for x in range (x_pixels):
        for y in range (y_pixels):
            for c in range(num_channels):
                new_im.array[x, y, c] = (image.array[x, y, c] - mid) * factor + mid 
    # vectorized
    # new_im = (image.array - mid) * factor + mid

    return new_im


def blur(image, kernel_size):
    # kernel size is the number of pixels to take into account when applying the blur
    # (ie kernel_size = 3 would be neighbors to 3 pixels to left, 3 to right, top/bottom, and diagonals)
    # kernel size should always be an *odd* number
    x_pixels, y_pixels, num_channels = image.array.shape # channels (R, G, B)
    new_im = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels) # making a copy
    neighbor_range = kernel_size // 2 # how many neighbor pixels do we need to look at (ie for a 3x3 kernel, this value should be 1)

    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):
                # iterate thourgh each neighbor
                total = 0
                # uning min & max to check the balance, not to go beyond the picture.
                # max(0,x-neighbor_range) will ensure we won't run into negative numbers 
                # min(x_pixels-1, x+neighbor_range) will ensure we won't go bigger than the picture size 
                # x_pixels-1 (-1 because the pic size starts from 0:  [0 - x_pixels-1])
                for x_i in range(max(0,x-neighbor_range), min(new_im.x_pixels-1, x+neighbor_range)+1): 
                    for y_i in range(max(0,y-neighbor_range), min(new_im.y_pixels-1, y+neighbor_range)+1):
                        total += image.array[x_i, y_i, c]
                new_im.array[x, y, c] = total / (kernel_size ** 2)  # average
    return new_im

# To detect edges (Sobel Operator):
def apply_kernel(image, kernel):
    # the kernel should be a 2D array that represents the kernel we'll use!
    # for the sake of simiplicity of this implementation, let's assume that the kernel is SQUARE
    # for example the sobel x kernel (detecting horizontal edges) is as follows:
    # [1 0 -1]
    # [2 0 -2]
    # [1 0 -1]
    x_pixels, y_pixels, num_channels = image.array.shape  # represents x, y pixels of image, # channels (R, G, B)
    new_im = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)  # making a new array to copy values to!
    neighbor_range = kernel.shape[0] // 2  # this is a variable that tells us how many neighbors we actually look at 
    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):
                total = 0
                for x_i in range(max(0,x-neighbor_range), min(new_im.x_pixels-1, x+neighbor_range)+1):
                    for y_i in range(max(0,y-neighbor_range), min(new_im.y_pixels-1, y+neighbor_range)+1):
                        x_k = x_i + neighbor_range - x
                        y_k = y_i + neighbor_range - y
                        kernel_val = kernel[x_k, y_k]
                        total += image.array[x_i, y_i, c] * kernel_val
                new_im.array[x, y, c] = total
    return new_im

def combine_images(image1, image2):
    # let's combine two images using the Pythagorean theorem to use it in an edge decetor later
    # size of image1 and image2 MUST be the same
    x_pixels, y_pixels, num_channels = image1.array.shape  # represents x, y pixels of image, # channels (R, G, B)
    new_im = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)  # making a new array to copy values to!
    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):
                new_im.array[x, y, c] = (image1.array[x, y, c]**2 + image2.array[x, y, c]**2)**0.5
    return new_im


def choose_pic ():
    while True: 
        pic = input('Which picture do you want, City or Lake?\n').lower()
        if pic == 'lake':
            pic = Image(filename='lake.png')
        elif pic == 'city':
            pic = Image(filename='city.png')
        else:
            print("Only Two Choises, City or Lake!")
            continue

        return pic


def choose_op ():
    op = input('What do you want to do with the photo? Choose: \n(B) for adjusting the Brightness,\n\
(C) for adjusting the Contrast,\n(Bl) for bluring the photo,\n(E) for deceting the edges:\n'). lower()

    return op

if __name__ == '__main__':
        # get the user's choice
        pic = choose_pic()
        # what do they want to do
        op = choose_op() 
        
        if op == 'b':
            while True:
                # getting user's input
                fac = input('To brighten the photo, put in a number bigger than 1. To darken it, put in a number between 0 to 1:')
                # check the input
                try:
                    fac = float(fac)
                except:
                    print('Invalid Input. Put in a number, please!')
                    continue  
                # brightening/darkening the photo using def brighten(image, factor)
                brightened_im = brighten(pic, fac)
                if fac > 1:
                    brightened_im.write_image('brightened.png')
                elif fac < 1:
                    brightened_im.write_image('darkened.png')
                if fac == 1:
                    print ('No Changes!')

                print ('Done!')
                break
        
        elif op == 'c': 
            while True:
                fac = input('To increase the contrast, put in a number bigger than 1. To decrease it, put in a number between 0 to 1:')
                # check the input
                try:
                    fac = float(fac)
                except:
                    print('Invalid Input. Put in a number, please!')
                    continue 

                # increasing/ decreasing the contrast using def adjust_contrast(image, factor, mid)
                if fac > 1:
                # increase contrast:
                    incr_contrast = adjust_contrast(pic, fac, 0.5)
                    incr_contrast.write_image('increased_contrast.png')

                elif fac < 1:
                # decrease contrast:
                    decr_contrast = adjust_contrast(pic, fac, 0.5)
                    decr_contrast.write_image('decreased_contrast.png')

                if fac == 1:
                    print ('No Changes!')
                
                print ('Done!')
                break

        elif op == 'bl':
            while True:
                ker = input('How Blury?')
                # check the input
                try:
                    ker = int(ker)
                except:
                    print('Invalid Input. Put in a number, please!')
                    continue 

                # blur with kernel using def blur(image, kernel_size)
                blur = blur(pic, ker)
                blur.write_image('blur.png')

                print ('Done!')
                break
        
        elif op == 'e':
            while True: 
                # applying a sobel edge detection kernel on the x and y axis
                sobel_x = apply_kernel(pic, np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]]))
                sobel_x.write_image('edge_x.png')
                sobel_y = apply_kernel(pic, np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]]))
                sobel_y.write_image('edge_y.png')

                # making an edge detector!
                sobel_xy = combine_images(sobel_x, sobel_y)
                sobel_xy.write_image('edge_xy.png')

                print ('Done!')
                break
        
        else: 
            print('Invalid Operation!')