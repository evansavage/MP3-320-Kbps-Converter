# MP3-320-Kbps-Converter

Python script for converting a folder of any format audio files to MP3 320 Kbps

# Description

This one goes out to all the DJs and musical folk out there who need to prepare their music to meet the rigid standard of Pioneer CDJs. 

FLACs, WAVs, AIFFs: if you're ever going to be able to reliably play your tunes on Pioneer CDJs, forget em. In late 2019, it was my first time on the decks, and I had some shimmering high-quality friggin tunes that I was anxious to play. Little did I know that legacy hardware and higher bitrate audio formats don't go together :(( The safest approach is to convert everything to an MP3 format, with a 320 kbps bitrate to boot. 

With this python script, I have found my own safe approach for converting my library of DJ tunes to MP3, and I would love to share it with you!

## Caveats

What about converting lower bit rate mp3s (lower-quality audio) to 320 kbps? Is any information lost? No, the audio now will be an oversampled version of the original, with all prior information maintained. 

Does this improve the quality of the audio? Not at all! That would be equivalent to creating information out of thin air, frequency information can not be newly rendered/perceived if it wasn't there in the first place. 

# Dependecies

You will need:
* A functional python installation (I used python 3.7 to write this) (https://www.python.org/)
* The ffmpeg python library (https://pypi.org/project/ffmpeg-python/)

# Usage

First, make sure you have two folders: one to read from (folder with all of your music) and one to write to (where the copies will be saved). I recommend making these folders parallel with one another (i.e. at the same level in your Finder or file explorer application). Then, place the `converter_mp3_320.py` file at the same level as those folders.

You will need to make a few edits to the `converter_mp3_320.py` file. The `srcDir` (line 4) and `destDir` (line 5) variables should be rewritten to the names of the folders that you would like to read from and write to, respectively. 

To execute the script, open a Terminal window and go to the location of the python file and source and destination directories. Type in: `python convert_mp3_320.py`, and the script will get to work!!

The array `ext_excl` (Extensions to exclude) is something that should be appended with file formats that are in your read folder and are not audio files. The extensions listed are what I have come across so far in my own music library. You will discover new ones when the script execution terminates with an error. Look at the file name that broke the execution (for example, `cover.js`), and add the extension to the end of the array (`'.js'`). 

**This also works for any and all nested directories you may have in your source folder.** The folder structures will be maintained in the destination folder as well :)

Please use the issues tab if you have any questions, unanticipated errors, suggestions, or concerns!!
