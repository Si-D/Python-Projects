import pygame
import tkinter as tk
from tkinter.filedialog import askdirectory
import os


mp3_player = tk.Tk()
mp3_player.title("Music - The Antidote")
mp3_player.geometry("500x400")

dir = askdirectory()
os.chdir(dir)
song_list = os.listdir()

playlist = tk.Listbox(mp3_player, font="Helvetica 15 bold", bg="green", selectmode=tk.SINGLE)

for i in song_list:
    pos = 0
    playlist.insert(pos, i)
    pos += 1

pygame.init()
pygame.mixer.init()

