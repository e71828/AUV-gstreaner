#!/usr/bin/env python

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# 创建GTK+窗口
window = Gtk.Window(title="Video Player")
window.set_default_size(1200, 800)

# 创建主要布局容器，使用Gtk.Grid
grid = Gtk.Grid()
window.add(grid)

# 创建视频显示区域，使用Gtk.DrawingArea
video_area = Gtk.DrawingArea()
video_area.set_size_request(800, 600)
grid.attach(video_area, 0, 0, 1, 2)

# 创建运动控制标签
controls_label1 = Gtk.Label(label="上")
controls_label2 = Gtk.Label(label="下")
controls_label3 = Gtk.Label(label="左")
controls_label4 = Gtk.Label(label="右")

# 创建旋转姿态标签
attitude_label1 = Gtk.Label(label="旋转姿态1")
attitude_label2 = Gtk.Label(label="旋转姿态2")
attitude_label3 = Gtk.Label(label="旋转姿态3")

# 创建高度标签
height_label = Gtk.Label(label="高度")

# 设置标签样式
label_style = "font-size: 14pt; padding: 10px"
controls_label1.set_name("controls-label")
controls_label2.set_name("controls-label")
controls_label3.set_name("controls-label")
controls_label4.set_name("controls-label")
attitude_label1.set_name("attitude-label")
attitude_label2.set_name("attitude-label")
attitude_label3.set_name("attitude-label")
height_label.set_name("height-label")

# 将标签添加到布局容器中
grid.attach(controls_label1, 1, 0, 1, 1)
grid.attach(controls_label2, 1, 1, 1, 1)
grid.attach(controls_label3, 2, 0, 1, 1)
grid.attach(controls_label4, 2, 1, 1, 1)
grid.attach(attitude_label1, 3, 0, 1, 1)
grid.attach(attitude_label2, 3, 1, 1, 1)
grid.attach(attitude_label3, 3, 2, 1, 1)
grid.attach(height_label, 0, 2, 1, 1)

# 设置布局容器的行列属性
grid.set_column_homogeneous(True)
grid.set_row_homogeneous(True)

# 设置布局容器的间距
grid.set_column_spacing(10)
grid.set_row_spacing(10)

# 设置标签的样式
style_provider = Gtk.CssProvider()
style_provider.load_from_data("""
    #controls-label, #attitude-label, #height-label {
        %s
    }
""" % label_style)
Gtk.StyleContext.add_provider_for_screen(
    Gdk.Screen.get_default(),
    style_provider,
    Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
)

window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()
