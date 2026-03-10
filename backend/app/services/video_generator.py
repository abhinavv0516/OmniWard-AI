import subprocess
import uuid
import os


def generate_video(before_path, after_path):

    video_name = f"{uuid.uuid4()}.mp4"
    output_path = f"storage/generated_videos/{video_name}"

    command = [
        "ffmpeg",
        "-loop", "1",
        "-t", "3",
        "-i", before_path,
        "-loop", "1",
        "-t", "3",
        "-i", after_path,
        "-filter_complex",
        "xfade=transition=fade:duration=1:offset=2",
        "-y",
        output_path
    ]

    subprocess.run(command)

    return output_path