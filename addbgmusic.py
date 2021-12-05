import moviepy.editor as mymovie

inputvideo = "video.mp4"
inputaudio = "audio.mp3"
outputvideo = "output.mp4"

videoclip = mymovie.VideoFileClip(inputvideo)
audioclip = mymovie.AudioFileClip(inputaudio)
finalclip = videoclip.set_audio(audioclip)
finalclip.write_videofile(outputvideo, fps=60)
