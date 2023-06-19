
# rtspserver

## server
`v4l2rtspserver -H 720 -W 1280 -F 25 -P 8555 /dev/video0`
 
## client
```
gst-launch-1.0 rtspsrc location=rtsp://192.168.31.249:8555/unicast ! rtph264depay ! h264parse ! avdec_h264 ! videoconvert ! autovideosink
gst-launch-1.0 rtspsrc location=rtsp://192.168.31.249:8555/unicast ! rtpjpegdepay ! jpegdec ! autovideosink fps-update-interval=1000 sync=false
gst-launch-1.0 rtspsrc location=rtsp://192.168.31.249:8555/unicast ! rtpjpegdepay ! jpegdec ! x264enc pass=quant ! matroskamux ! filesink location=video.mkv
```

##  port already in use
`sudo fuser -k 8000/tcp` [ref](https://stackoverflow.com/questions/20239232/django-server-error-port-is-already-in-use)

## Other Method
use `gstreamer-rtsp-server-1.0`, as the CMakeLists.txt in this project.
