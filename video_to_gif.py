import argparse
import os
from moviepy.video.io.VideoFileClip import VideoFileClip
import moviepy.video.fx as vfx


def convert_video_to_gif(video_path, output_gif_path, start_time, stop_time, fps=10, scale=1.0):
    """
    Converts a video clip to a GIF, trimming it based on start and stop times.

    Args:
        video_path (str): Path to the input video file.
        output_gif_path (str): Path to save the output GIF file.
        start_time (float): Start time in seconds for trimming.
        stop_time (float): Stop time in seconds for trimming.
        fps (int): Frames per second for the output GIF.
        scale (float): Factor to scale the video resolution.
    """
    try:
        if not os.path.exists(video_path):
            raise FileNotFoundError(
                f"Error: Input video file not found at '{video_path}'")

        print(f"Loading video: {video_path}")
        clip = VideoFileClip(video_path)
        if stop_time is None:
            stop_time = clip.duration
        if start_time < 0 or stop_time <= start_time or stop_time > clip.duration:
            raise ValueError(
                f"Error: Invalid start/stop times. "
                f"Video duration is {clip.duration:.2f} seconds. "
                f"Ensure 0 <= start < stop <= duration."
            )
        if stop_time is None:
            stop_time = clip.duration
        print(f"Trimming video from {start_time:.2f}s to {stop_time:.2f}s...")
        trimmed_clip = clip.subclipped(start_time, stop_time)

        if scale != 1.0:
            print(f"Scaling video by a factor of {scale}")
            trimmed_clip = trimmed_clip.with_effects([vfx.Resize(scale)])

        print(f"Converting trimmed clip to GIF: {output_gif_path}")
        # adjust the fps (frames per second) for gif quality & size
        # lower fps will result in a smaller file size but likely choppier quality.
        trimmed_clip.write_gif(output_gif_path, fps=fps,
                               logger='bar')  # loop=2))

        print(f"Successfully converted '{video_path}' to '{output_gif_path}'")

    except FileNotFoundError as e:
        print(e)
        return False
    except ValueError as e:
        print(e)
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False
    finally:
        if 'clip' in locals() and clip is not None:
            clip.close()
        if 'trimmed_clip' in locals() and trimmed_clip is not None:
            trimmed_clip.close()
    return True


def main():
    parser = argparse.ArgumentParser(
        description="Convert a video to a GIF, with options for trimming and scaling."
    )
    # Positional arguments
    parser.add_argument(
        "video_path",
        type=str,
        nargs='?',
        default=None,
        help="Path to the input video file (e.g., path/to/video.mp4)."
    )
    parser.add_argument(
        "output_gif_path",
        type=str,
        nargs='?',
        default=None,
        help="Path to save the output gif file (e.g., path/to/output.gif)."
    )
    # Optional arguments
    parser.add_argument(
        "-i", "--input",
        type=str,
        help="Path to the input video file (alternative to positional)."
    )
    parser.add_argument(
        "-o", "--output",
        type=str,
        help="Path to save the output gif file (alternative to positional)."
    )
    parser.add_argument(
        "--start",
        type=float,
        default=0,
        help="Start time in seconds for the clip (default: beginning)."
    )
    parser.add_argument(
        "--scale",
        type=float,
        default=1.0,
        help="Factor to scale video resolution (e.g., 0.5 for half size)."
    )
    parser.add_argument(
        "--stop",
        type=float,
        default=None,
        help="Stop time in seconds for the clip (default: end of video)."
    )
    parser.add_argument(
        "--fps",
        type=int,
        default=10,
        help="Framerate (frames per second) for the output GIF."
    )

    args = parser.parse_args()

    # Determine input and output paths
    video_path = args.video_path or args.input
    output_gif_path = args.output_gif_path or args.output

    if not video_path:
        parser.error("Input video path is required, either as a positional argument or with -i/--input.")
    if not output_gif_path:
        parser.error("Output GIF path is required, either as a positional argument or with -o/--output.")

    convert_video_to_gif(
        video_path,
        output_gif_path,
        args.start,
        args.stop,
        args.fps,
        args.scale
    )


if __name__ == "__main__":
    main()
