#!/usr/bin/env python

import gi

from receive_and_disp import Video

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf, GLib
import cv2
from PIL import Image
from datetime import datetime

# 创建GTK+窗口
window = Gtk.Window(title="Video Player")

# 创建左侧用于显示视频的框
video_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=20)
video_box.set_size_request(1920, 1080)  # 设置框的大小


# 创建用于显示视频的图像控件
image = Gtk.Image()
video_box.pack_start(image, False, False, 0)

# 创建右侧的框
label_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)
label_box.set_size_request(150, -1)  # 设置宽度为 150 像素

grid = Gtk.Grid()
grid.set_row_spacing(100)  # 设置行间距为 100 像素
grid.set_column_spacing(20)  # 设置列间距为 20 像素

# 创建用于显示值的Label控件列表
value_labels = []

# 创建并添加四个值的Label控件到列表中
for i in range(4):
    value_label = Gtk.Label(label="Value")
    grid.attach(value_label, 1, i, 1, 1)
    value_labels.append(value_label)

grid.attach(Gtk.Label(label="高度"), 0, 0, 1, 1)
grid.attach(Gtk.Label(label="方向"), 0, 1, 1, 1)
grid.attach(Gtk.Label(label="横滚"), 0, 2, 1, 1)
grid.attach(Gtk.Label(label="横滚"), 0, 3, 1, 1)

# 将 grid 添加到垂直居中的容器中
label_box.pack_start(grid, True, False, 0)
# 添加垂直居中容器到左侧框中
video_box.pack_start(label_box, False, False, 0)

# 添加左侧框到窗口中
window.add(video_box)

# 创建视频对象
video = Video()

# 更新值的计数器
value_counter = 100

def update_values():
    global value_counter

    # 循环更新四个值的Label控件的文本内容
    for value_label in value_labels:
        value_label.set_text(str(value_counter))

    # 增加计数器的值
    value_counter += 1

    # 返回True以继续更新
    return True


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
        image.set_from_pixbuf(pixbuf)

    # 更新画面
    return True


# 开始视频播放
print('Starting streaming - press "q" to quit.')


def key_event(widget, event):
    #  when 's' is pressed
    if event.keyval == 115:
        # save pictures
        cv2.imwrite("Frame_" + datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpg", video.latest_frame)
    if event.keyval == 113:
        # quit
        Gtk.main_quit()


window.connect("destroy", Gtk.main_quit)
window.connect("key-press-event", key_event)
window.show_all()

# 更新值
GLib.timeout_add(1000, update_values)
# 更新视频画面
GLib.timeout_add(50, update_frame)

Gtk.main()
