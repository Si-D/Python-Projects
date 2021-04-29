import pygame
import tkinter as tk
from tkinter.filedialog import askdirectory
import os


mp3_player = tk.Tk()
mp3_player.title("Music - The Antidote")
mp3_player.geometry("500x400")


dir = askdirectory()
dir = os.path.abspath(dir)
#os.chdir(dir)
#dirpath = os.path.basename(os.getcwd())
song_list = os.listdir()

playlist = tk.Listbox(mp3_player, font="Helvetica 15 bold", bg="green", selectmode=tk.SINGLE)

for i in song_list:
    pos = 0
    playlist.insert(pos, i)
    pos += 1

pygame.init()
pygame.mixer.init()

#Music player functions

def play():
    pygame.mixer.music.load(playlist.get(tk.ACTIVE))
    var.set(playlist.get(tk.ACTIVE))
    pygame.mixer.music.play()

def stop():
    pygame.mixer.music.stop()

def pause():
    pygame.mixer.music.pause()

def resume():
    pygame.mixer.music.unpause()

Button1 = tk.Button(music_player, width=5, height=3, font='Helvetica 15 bold', text='PLAY', command=play, bg='blue', fg='white')
Button2 = tk.Button(music_player, width=5, height=3, font='Helvetica 15 bold', text='STOP', command=stop, bg='red', fg='white')
Button3 = tk.Button(music_player, width=5, height=3, font='Helvetica 15 bold', text='PAUSE', command=pause, bg='purple', fg='white')
Button4 = tk.Button(music_player, width=5, height=3, font='Helvetica 15 bold', text='RESUME', command=unpause, bg='orange', fg='white')   

var = tk.StringVar()
song_title = tk.Label(mp3_player, font="Helvetica 15 bold", textVariable=var)

song_title.pack()
Button1.pack(fill='x')
Button2.pack(fill='x')
Button3.pack(fill='x')
Button4.pack(fill='x')
playlist.pack(fill='both', expand='yes')
mp3_player.mainloop()