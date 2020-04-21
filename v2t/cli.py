import os
import click
from .help import BRANDING


@click.command()
@click.version_option(message=BRANDING)
def cli():
    """'AzatAI v2t tool : Extracts text from the video, This is not a subtitle extraction tool, this tool uses ASR to
    extract text from the video files."""
    click.echo('hello')


if __name__ == '__main__':
    cli()
