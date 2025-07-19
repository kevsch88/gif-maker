# GIF Maker

A simple Python script to convert video files into high-quality animated GIFs.

## Usage

This project provides a command-line script, `video_to_gif.py`, to handle the conversion.

### Installation
#### Using included environment files
A `pyproject.toml`, `requirements.txt` and `uv.lock` are included for ease of installation.

To use them install with preferred env manager.  
E.g., with pip:  
```bash
pip install -e .
```

With uv:  
```bash
uv sync
```
*or*
```bash 
uv pip install -e .
```

With pixi:  
```bash
pixi install
```

#### Creating new environment
If installing into new environment from scratch, after creating environment, ensure you have Python and the following libraries installed:
- MoviePy

If installing to a new environment, you can install MoviePy using pip:
```bash
pip install moviepy
```

### Command-Line Instructions

Run the script from your terminal using the following format:

```bash
python video_to_gif.py --input <path_to_video> [options]
```

#### Arguments

*   `-i`, `--input`: **(Required)** The path to the input video file.
*   `-o`, `--output`: (Optional) The path for the output GIF file. If not provided, the output will be saved in the same directory as the input file with a `.gif` extension.
*   `--fps`: Frames per second for the output GIF. Defaults to `10`.
*   `--start`: The start time in the video from which to create the GIF. Can be in seconds (e.g., `30`) or in `HH:MM:SS` format (e.g., `00:00:30`). Defaults to `0`.
*   `--stop`: The stop time in the video from which to create the GIF. Can be in seconds (e.g., `35`) or in `HH:MM:SS` format (e.g., `00:00:35`). If not specified, the script will process the video from `start` to the end of the video.
*   `--scale`: (Optional) A float value to scale the output GIF's resolution. For example, `0.5` for half resolution. Defaults to `1.0` (original resolution).

### Example

To create a 5-second GIF from `my_awesome_video.mp4`, starting at the 30-second mark, with 15 FPS and half the original resolution:

```bash
python video_to_gif.py -i my_video.mp4 -o cool_moment.gif --fps 15 --start 30 --stop 35 --scale 0.5
```