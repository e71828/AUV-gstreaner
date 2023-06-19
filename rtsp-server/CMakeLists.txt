cmake_minimum_required(VERSION 3.5)

project(basic LANGUAGES C)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)


## GStreamer 1.0 package required
# check and search moudles
find_package(PkgConfig REQUIRED)
pkg_search_module(GST REQUIRED gstreamer-1.0)
pkg_search_module(GST_VIDEO REQUIRED gstreamer-video-1.0)
pkg_search_module(GST_RTSP REQUIRED gstreamer-rtsp-server-1.0)
pkg_search_module(GST_APP REQUIRED gstreamer-app-1.0)

include_directories(
    ${GST_INCLUDE_DIRS} ${GST_VIDEO_INCLUDE_DIRS} ${GST_APP_INCLUDE_DIRS} ${GTK_INCLUDE_DIRS} ${GST_RTSP_INCLUDE_DIRS}
    )

link_libraries(
    ${GST_LDFLAGS} ${GST_VIDEO_LDFLAGS} ${GST_APP_LDFLAGS} ${GTK_LDFLAGS} ${GST_RTSP_LDFLAGS}
    )


add_executable(test test-video.c)
