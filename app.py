import sys
import warnings
import pkgutil
import face_recognition
import locale
import cv2 
import face_recognition_models
import os
import numpy
import numpy as np
import tkinter as tk
from tkinter import simpledialog, messagebox, scrolledtext
from PIL import Image, ImageTk
import time
import serial
import serial.tools.list_ports
import json
from datetime import datetime
from PIL import Image
warnings.filterwarnings("ignore", message="pkg_resources is deprecated")



print(cv2.__version__)
print(os.path.dirname(face_recognition_models.__file__))

image = face_recognition.load_image_file("blue.jpg")
encodings = face_recognition.face_encodings(image)

print(f"Найдено {len(encodings)} лиц(о/а/лиц) с эмбеддингами.")


