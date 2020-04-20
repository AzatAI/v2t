import os
import click
from .help import BRANDING
from .utils import validate_path, error, info


@click.command()
@click.version_option(message=BRANDING)
@click.argument('source', required=False)
@click.argument('destination', required=False)
def cli(source, destination):
    """'AzatAI v2t tool : Extracts text from the video, This is not a subtitle extraction tool, this tool uses ASR to
    extract text from the video files.
    Usage: v2t [options] <video_source_dir target_text_path> (OR <video_url>)
    INFO : canbe video url if [-by] or a sourcedir for videos and a destination path for text."""
    # TODO
    #  Download video from BiliBili Automatically. option -b --bilibili bilibili video url. flag
    #  Auto process v2t
    #  Get Youtube video subtitles (both auto generated and mannual added) option -y --youtube youtube video url flag
    #  OCR hardcore video subtitles.  option -o  --ocr  give video location and destination. flag
    args = []
    if not source and not destination:
        with click.get_current_context() as context:
            click.echo(context.get_help())
    elif source and destination:
        if validate_path(source):
            if validate_path(destination):
                ## first convert and save the audio

                ## second get the audio text
                ## save the audio text file to destination
                click.echo('ok')
            else:
                error(f'{destination}: Not a valid path!')
        else:
            error(f'{source}: Not a valid path!')
    elif source:
        # TODO if we only have the source, that means this is a url.
        pass
