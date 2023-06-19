#!/bin/bash

if screen -ls | grep video; then
        screen -X -S video quit
fi

# this is followed up in start_video.sh
cp /home/ubuntu/ROV-gstreamer/video_h264_stream/vidformat.param /home/ubuntu/ROV-gstreamer/video_h264_stream/vidformat.param.bak

if [ "$#" == 4 ]; then
        echo "$1" > /home/ubuntu/vidformat.param
        echo "$2" >> /home/ubuntu/vidformat.param
        echo "$3" >> /home/ubuntu/vidformat.param
        echo $4 >> /home/ubuntu/vidformat.param
else
        echo "Invalid number of parameters [$#]: $@"
fi

sudo -H -u ubuntu screen -dm -S video /home/ubuntu/ROV-gstreamer/video_h264_stream/streamer.py
