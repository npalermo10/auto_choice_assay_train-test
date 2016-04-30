import max7219.led as led
import numpy as np
from peripheral import Peripheral

#remember that to use max7219 library, SPI needs sudo access. Look at github page for max7219 library for directions on how to do this

class Led_matrix(Peripheral):
    def __init__(self):
        self.led_init = led.matrix(cascaded=1)
        self.mat = []
        if self.device_id = "dummy":
            self.update = dummy_update

    def draw_bars(self, vertical = True):
        if vertical:
            self.mat=np.matrix(
            [
             [1,1,0,0,0,0,1,1],
             [1,1,0,0,0,0,1,1],
             [1,1,0,0,0,0,1,1],
             [1,1,0,0,0,0,1,1],
             [1,1,0,0,0,0,1,1],
             [1,1,0,0,0,0,1,1],
             [1,1,0,0,0,0,1,1],
             [1,1,0,0,0,0,1,1]
            ])
            self.status = "vertical_bars"
        if not vertical:
            self.mat=np.matrix(
            [
            [1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1]
            ])
            self.status = "horizontal_bars"
        height = mat.shape[0]
        width = mat.shape[1]
        for i in range(0, height):
            for k in range(0, width):
            self.device.pixel(k,i, mat[i,k], redraw = False)

    def clear_matrix(self):
        self.mat = np.matrix(
            [
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0]
            ])
        self.status = "off"
        height = mat.shape[0]
        width = mat.shape[1]
        for i in range(0, height):
            for k in range(0, width):
            self.device.pixel(k,i, mat[i,k], redraw = False)
        
    def update(self):
        self.device.flush()
