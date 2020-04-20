import os
import click

here = os.getcwd()


def validate_path(path):
    """Validate a path"""
    return os.path.isdir(path)


def validate_video(file):
    """Validate the given file, Return True if a ffmpeg supported video format"""
    pass


def error(msg):
    return click.secho(msg, fg='red')


def info(msg):
    return click.secho(msg, fg='blue')


def success(msg):
    return click.secho(msg, fg='green')


def video2audio(video):
    """Extracts audio(wav format) from the given video and saves to the ./.tmp folder """
    audio_path = os.path.join(here, '.tmp/audio/')
    if not validate_path(audio_path):
        os.mkdir(audio_path)
    audio_name = f"{video}.wav"
    cmd = f"ffmpeg -i {video} -f wav -vn {os.path.join(audio_path, audio_name)}"
    return audio_name


def recognize(audio, destination):
    """Do speech recognition on the AUDIO and saves the extracted text to the DESTIONATION folder"""
    pass


def clean():
    """Cleans temporary directories that used by the program"""
    cmd = f"rm -rf {here}/.tmp"
    os.system(cmd)
