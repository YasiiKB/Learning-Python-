'''
First, you'll need to: 
pip install tk
pip install Pillow 
'''
import tkinter
from PIL import Image, ImageTk
import random 
from pygame import mixer

# location of the files - the directory in which these files are
location = ' '.replace('\\','/')

# Window
background_color = '#C793C3' # won't work with RGB
root = tkinter.Tk()
root.geometry('400x500')
root.title('Roll the Dice!')
root.configure(bg = background_color)

# Label
text_on_top = tkinter.Label(root, text='Roll the Dice!', fg= 'purple', bg = background_color, font = 'Helvetica 16 bold')
text_on_top.pack()

# Image
dice_img = Image.open(location +'dice.png')
win_image = ImageTk.PhotoImage(dice_img)
win_pic = tkinter.Label(root, image=win_image)
win_pic.image = win_image
win_pic.pack(expand= True)  # Pack a widget in the parent widget

# Dice faces
dice = [location +'dice_1.png',location +'dice_2.png',location +'dice_3.png', location +'dice_4.png', location +'dice_5.png', location +'dice_6.png',]

# Roll Function
def roll(event=None):  # event=None is necessary for the root.bind
    win_dice = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    # update the image
    win_pic.configure(image = win_dice, bg = background_color)
   # keep a refrence
    win_pic.image = win_dice

    # sound
    mixer.init()
    diceroll= mixer.Sound(location +'roll.wav')
    diceroll.play()

# Create a Button
btn = tkinter.Button(root, text = 'Click or Hit Space!', font=('Arial,10,bold') ,width = 20, height =2, bg='purple', fg='white', command = roll)
btn.pack(expand= True)

# Binding space to the roll function
root.bind("<space>", roll)

root.mainloop()
