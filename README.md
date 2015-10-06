datefiles.py
============

This is a small tool that I created to help me organize digital camera photos.
In the past, I would copy them to my computer and then use exiftool to read the
metadata of the image and move the files into `YYYY/MM-DD/` directories.
However, this did not work for non-JPG files, such as videos or screenshots
from my phone.


This tool moves files into a `YYYY/MM-DD` scheme based on the mtime of the file
retrieved using `stat`.


Usage
-----

`./datefiles.py --target /my/base/path IMG_0001.JPG` will move `IMG_0001.JPG`
into a path like `/my/base/path/2015/10-05/IMG_0001.JPG`.


To do
-----

Maybe someone could add custom date formats? Some people would probably prefer
`YYYY/MM/DD` instead.
