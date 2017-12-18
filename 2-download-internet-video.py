#!/usr/bin/env python
# -*- coding: utf-8 -*-
import youtube_dl


ydl_opts = {
    'outtmpl': 'temp.mp4',
    'format': 'mp4',

}

'''
I choose a sporty video and detailed information as below:
Input #0, mov,mp4,m4a,3gp,3g2,mj2, from 'temp.mp4':
  Metadata:
    major_brand     : mp42
    minor_version   : 0
    compatible_brands: isommp42
    creation_time   : 2017-12-16T06:38:56.000000Z
  Duration: 00:03:13.24, start: 0.000000, bitrate: 1294 kb/s
    Stream #0:0(und): Video: h264 (Main) (avc1 / 0x31637661), yuv420p(tv, bt709), 1280x720 [SAR 1:1 DAR 16:9], 1164 kb/s, 29.97 fps, 29.97 tbr, 90k tbn, 59.94 tbc (default)
    Metadata:
      creation_time   : 2017-12-16T06:38:56.000000Z
      handler_name    : ISO Media file produced by Google Inc. Created on: 12/15/2017.
    Stream #0:1(und): Audio: aac (LC) (mp4a / 0x6134706D), 44100 Hz, stereo, fltp, 125 kb/s (default)
    Metadata:
      creation_time   : 2017-12-16T06:38:56.000000Z
      handler_name    : ISO Media file produced by Google Inc. Created on: 12/15/2017.
'''
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=3RMiGRLnkBE'])