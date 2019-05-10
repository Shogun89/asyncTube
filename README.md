![Screenshot](https://github.com/mosh47/asyncTube/blob/master/images/title.png)

## *Overview*
This tool is meant to be used to download your videos on YouTube in bulk asynchronusly. Use with only videos that YOU own or those which do not have copyright laws. I am not responsible for you getting in trouble using this.

## *Installation*
You will need ```pytube``` installed, checkout https://github.com/nficano/pytube
```sh
> pip install pytube
```

## *Running*
```Python
from asyncTube import asyncTube
import os

videos = {'video1':'vid1link',
          'video2':'vid2link',...,
         }

asyncTube(videos, path=os.getcwd()).GET()

```
