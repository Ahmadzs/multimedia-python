import pygame
import PIL
import cv2
import moviepy.editor as mp
from pydub import AudioSegment
import tkinter as tk

def check_installation():
    try:
        print("✅ Pygame version:", pygame.version.ver)
    except Exception as e:
        print(f"❌ Terjadi kesalahan saat memeriksa Pygame: {e}")

    try:
        print("✅ Pillow version:", PIL.__version__)
    except Exception as e:
        print(f"❌ Terjadi kesalahan saat memeriksa Pillow: {e}")

    try:
        print("✅ OpenCV version:", cv2.__version__)
    except Exception as e:
        print(f"❌ Terjadi kesalahan saat memeriksa OpenCV: {e}")

    try:
        # Memeriksa versi moviepy
        import moviepy
        print("✅ MoviePy version:", moviepy.__version__)
    except Exception as e:
        print(f"❌ Terjadi kesalahan saat memeriksa MoviePy: {e}")

    try:
        # Memeriksa versi pydub
        print("✅ Pydub version:", AudioSegment.converter)
    except Exception as e:
        print(f"❌ Terjadi kesalahan saat memeriksa Pydub: {e}")

    try:
        # Memeriksa Tkinter
        root = tk.Tk()
        root.title("Tkinter Test")
        root.geometry("200x100")
        label = tk.Label(root, text="Tkinter is working!")
        label.pack()
        root.update_idletasks()
        root.destroy()
        print("✅ Tkinter is installed and working!")
    except Exception as e:
        print(f"❌ Terjadi kesalahan saat memeriksa Tkinter: {e}")

if __name__ == "__main__":
    check_installation()
