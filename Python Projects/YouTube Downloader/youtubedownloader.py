from tkinter import * #import everything
from tkinter import filedialog
import tkinter.messagebox
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube
import shutil #a built-in library to move the file to the selected directory


#Functions
def select_path():
    #lets user select a directory
    path = filedialog.askdirectory()
    path_label.config(text=path)

def download_file():
    #get user's link
    get_link = link_field.get()
    #get selected path
    user_path = path_label.cget('text')
    screen.title("Downloading...!")
    #download the video
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()
    #move file to selected directory
    try:
        shutil.move(mp4_video, user_path)
        tkinter.messagebox.showinfo(" ", "Download Complete!")
    except: 
        tkinter.messagebox.showinfo("Download Complete", "The File was saved on your Desktop!")
    
    screen.title('YouTube Downloader')

#Set up the Screen
screen = Tk()
title = screen.title('YouTube Downloader')
canvas  = Canvas(screen, width=500, height=500)
canvas.pack()

#YouTube Logo
logo_img = PhotoImage(file='E:/yt.png')
#resize the image
logo_img = logo_img.subsample(2,2)
canvas.create_image(250, 80, image =logo_img) #x and y position on the screen

#Link Field
link_field = Entry(screen,width=50)
link_label=Label(screen, text="Enter the link here:", font=('Arial', 10))

#Select Path for saving the file
path_label = Label(screen, text="Select Path:", font=('Arial', 10))
select_btn = Button(screen, text="Select", command= select_path)

#Download Button
download_btn = Button(screen, text="Download", command= download_file)

#Add Widgets to window 
canvas.create_window(250, 170, window=link_label)
canvas.create_window(250, 190, window=link_field)
canvas.create_window(250, 250, window=path_label)
canvas.create_window(250, 280, window=select_btn)
canvas.create_window(250, 390, window=download_btn)

screen.mainloop()
