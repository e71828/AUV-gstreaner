#!/usr/bin/env python
from datetime import datetime

import gi
import cv2

from receive_and_disp import Video

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf, GLib
from PIL import Image


def update_frame():
    if video.frame_available():
        # Only retrieve and display a frame if it's new
        frame = video.frame()

        # 将OpenCV图像转换为PIL图像
        pil_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

        # 将PIL图像转换为GdkPixbuf图像
        pixbuf = GdkPixbuf.Pixbuf.new_from_data(
            pil_image.tobytes(),
            GdkPixbuf.Colorspace.RGB,
            False,
            8,
            pil_image.width,
            pil_image.height,
            pil_image.width * 3
        )

        # 在图像控件中显示图像
        image1.set_from_pixbuf(pixbuf)
        image2.set_from_pixbuf(pixbuf)

    # 更新画面
    return True


# 创建GTK+窗口，指定默认的窗口大小 1920x1080
window = Gtk.Window(title="EIMO GUI")
window.set_default_size(2560, 1440)

# 使用格子，2x2
grid = Gtk.Grid()
window.add(grid)
# 设置网格布局的属性，使得格子可以自适应放大
grid.set_row_homogeneous(True)
grid.set_column_homogeneous(True)
# 创建四个标签并将它们添加到格子中
label1 = Gtk.Label(label="Label 1")
label2 = Gtk.Label(label="Label 2")
label3 = Gtk.Label(label="Label 3")
label4 = Gtk.Label(label="Label 4")

# 创建图像小部件
image1 = Gtk.Image()
image2 = Gtk.Image()

# 将图像小部件添加到网格的适当位置
grid.attach(image1, 0, 0, 1, 1)
grid.attach(image2, 0, 1, 1, 1)
grid.attach(label3, 1, 0, 1, 1)
grid.attach(label4, 1, 1, 1, 1)

def key_event(widget, event):
    #  when 's' is pressed
    if event.keyval == 115:
        # save pictures
        cv2.imwrite("Frame_" + datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpg", video.latest_frame)
    if event.keyval == 113:
        # quit
        Gtk.main_quit()

window.connect("destroy", Gtk.main_quit)
window.show_all()
video = Video()
GLib.timeout_add(1000 / 15, update_frame)
Gtk.main()
