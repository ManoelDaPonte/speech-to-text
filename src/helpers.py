import os
os.environ["IMAGEIO_FFMPEG_EXE"] = "/Users/mano/miniconda3/envs/speech-to-text/bin/ffmpeg"
from moviepy.editor import VideoFileClip

def write_audio_file(audio, path = "/Users/mano/Documents/GitHub/speech-to-text/data/data_vincent_artaud/Vincent Artaud - Interview_clip.wav"):
    audio.write_audiofile(path)

def read_video_file(path = "/Users/mano/Documents/GitHub/speech-to-text/data/data_vincent_artaud/Vincent Artaud - Interview.mov"):
    clip = VideoFileClip(path)
    audio = clip.audio
    return audio

def extract_audio_from_video(video):
    audio = video.audio
    return audio

def subclip_audio(audio, start, end):
    audio_segment = audio.subclip(t_start=start, t_end=end)
    return audio_segment
