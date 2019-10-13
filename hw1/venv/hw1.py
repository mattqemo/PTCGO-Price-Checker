import numpy as np
from hw1_starter import generate_gif

def rotY(theta):
    dimen = (3, 3)
    r = np.zeros(dimen)
    r[0, 0] = np.cos(theta)
    r[2, 0] = np.sin(theta)
    r[0, 2] = -np.sin(theta)
    r[2, 2] = np.cos(theta)
    r[1, 1] = 1;
    return r

def rotX(theta):
    dimen = (3, 3)
    r = np.zeros(dimen)
    r[0, 0] = 1;
    r[1, 1] = np.cos(theta)
    r[2, 1] = np.sin(theta)
    r[1, 2] = -np.sin(theta)
    r[2, 2] = np.cos(theta)
    return r

generate_gif()

