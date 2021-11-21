import os, shutil
import ffmpeg

srcDir = 'YOUR_SOURCE_DIRECTORY/'
destDir = 'YOUR_DEST_DIRECTORY/'

ext_excl = ['', '.asd', '.m3u', '.reapeaks', '.nfo', \
    '.sfv', '.jpg', '.png', '.jpeg', '.txt', '.url', '.log', '.cue', '.db']

# loop through source directory
for root, dirs, files in os.walk(srcDir, topdown=True):
    for file in files:
        src = os.path.join(root, file)
        target = os.path.join(destDir, '/'.join(src.split('/')[1:]))

        # check for duplicate first?
        print('\n\n' + src)
        print(target)

        # If the mp3 copy does not exist
        if not os.path.exists(os.path.splitext(target)[0] + '.mp3') \
            and os.path.splitext(target)[1] not in ext_excl:
            try:
                os.makedirs(os.path.dirname(target))
            except:
                pass
            out, _ = (ffmpeg
                .input(src)
                .output(os.path.splitext(target)[0] + '.mp3', format="mp3", audio_bitrate=320000)
                .run(capture_stdout=True)
            )
