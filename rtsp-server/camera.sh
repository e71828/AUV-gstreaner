#!/bin/bash
if  lsof -Pi :8555 -sTCP:LISTEN -t >/dev/null ; then  echo "already running" ; elif [ -c /dev/video0 ] ; then  v4l2rtspserver -H 480 -W 640 -F 25 -P 8555 /dev/video0 ; else echo "Device error"; fi
