import subprocess

def merge_subtitles(video_path, subtitle_path, output_path):
    """
    Merges subtitles into a video file, creating a new video file.
    
    Args:
    video_path (str): The path to the video file.
    subtitle_path (str): The path to the subtitle file.
    output_path (str): The path to output the merged video file.
    """
    # Command to merge subtitles into video
    command = [
        'ffmpeg',
        '-i', video_path,             # Input video file
        '-vf', f"subtitles='{subtitle_path}'",  # Path to the subtitle file
        '-c:v', 'libx264',            # Video codec to use
        '-c:a', 'copy',               # Copy audio without re-encoding
        '-crf', '22',                 # Constant Rate Factor for quality (18-28 is a good range)
        output_path                   # Output file
    ]

    # Execute the command
    try:
        subprocess.run(command, check=True)
        print(f"Merge complete: {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error during merge: {e}")

# Example usage
video_file = "test-video.mp4"
subtitle_file = "out-ass.ass"
output_video_file = "output_with_subtitles.mp4"

merge_subtitles(video_file, subtitle_file, output_video_file)
