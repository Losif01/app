import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import torch
import skimage
from skimage.color import rgb2lab, lab2rgb
from skimage.transform import resize
print("working")
print(st.__version__,
plt.__version__,
np.__version__,
torch.__version__,
skimage.__version__)