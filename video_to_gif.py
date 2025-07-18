import argparse
import os
from moviepy.video.io.VideoFileClip import VideoFileClip


def convert_video_to_gif(video_path, output_gif_path, start_time, stop_time, fps=10):
    """
    Converts a video clip to a GIF, trimming it based on start and stop times.

    Args:
        video_path (str): Path to the input video file.
        output_gif_path (str): Path to save the output GIF file.
        start_time (float): Start time in seconds for trimming.
        stop_time (float): Stop time in seconds for trimming.
        fps (int): Frames per second for the output GIF.
    """
    try:
        if not os.path.exists(video_path):
            raise FileNotFoundError(
                f"Error: Input video file not found at '{video_path}'")

        print(f"Loading video: {video_path}")
        clip = VideoFileClip(video_path)

        if start_time < 0 or stop_time <= start_time or stop_time > clip.duration:
            raise ValueError(
                f"Error: Invalid start/stop times. "
                f"Video duration is {clip.duration:.2f} seconds. "
                f"Ensure 0 <= start < stop <= duration."
            )

        print(f"Trimming video from {start_time:.2f}s to {stop_time:.2f}s...")
        trimmed_clip = clip.subclipped(start_time, stop_time)

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
        description="Convert a video to a GIF, trimming it based on start and stop times, with given frames per second (fps; default=10)."
    )
    parser.add_argument(
        "video_path",
        type=str,
        help="Path to the input video file (e.g., path/to/video.mp4)."
    )
    parser.add_argument(
        "output_gif_path",
        type=str,
        help="Path to save the output gif file (e.g., path/to/output.gif)."
    )
    parser.add_argument(
        "--start",
        type=float,
        required=True,
        help="Start time in seconds for start of the clip."
    )
    parser.add_argument(
        "--stop",
        type=float,
        required=True,
        help="Stop time in seconds for the end of the clip."
    )
    parser.add_argument(
        "--fps",
        type=int,
        default=10,
        help="The framerate, in frames per second, for the output gif."
    )

    args = parser.parse_args()

    convert_video_to_gif(
        args.video_path,
        args.output_gif_path,
        args.start,
        args.stop,
        args.fps
    )


if __name__ == "__main__":
    main()
