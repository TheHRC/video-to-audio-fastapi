import os
import logging

from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import FileResponse
from tempfile import NamedTemporaryFile
from moviepy.editor import VideoFileClip
from pydub import AudioSegment

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


def video_to_audio(video_path: str, file_name: str):
    """
    This to convert a video file to audio in the temp folder

    :param video_path: The video path
    :param file_name: The original video name
    :return: The temp audio file location
    """
    # Load video file
    video = VideoFileClip(video_path)

    # Extract audio from video
    audio = video.audio

    # Save extracted audio as WAV file
    temp_audio_file = NamedTemporaryFile(suffix=".wav", delete=False)
    audio.write_audiofile(temp_audio_file.name, verbose=False, logger=None)

    # Load WAV file
    wav_audio = AudioSegment.from_wav(temp_audio_file.name)

    # Get video file name without extension
    video_file_name = os.path.splitext(os.path.basename(file_name))[0]

    # Generate audio file path with the same name as the video file
    audio_file_path = os.path.join(os.path.dirname(video_path), f"{video_file_name}.mp3")

    # Convert WAV to MP3
    wav_audio.export(audio_file_path, format="wav")

    # Closing the files
    temp_audio_file.close()
    video.close()

    return audio_file_path


@app.post("/convert/")
async def convert_video_to_audio(file: UploadFile = File(...)):
    if file.content_type.startswith("video/"):
        # Creating a temporary file
        with NamedTemporaryFile(suffix=".mp4", delete=False) as video_file:
            video_content = await file.read()
            video_file.write(video_content)
            video_file_path = video_file.name
        try:
            # Conversion from video to audio
            logger.info(f"Converting video file: {file.filename}")
            audio_file_path = video_to_audio(video_file_path, file.filename)
            logger.info(f"Conversion successful. Audio file saved at: {audio_file_path}")
            return FileResponse(audio_file_path, media_type="audio/mpeg", filename=os.path.basename(audio_file_path))
        except Exception as e:
            logger.error(f"Error occurred during conversion: {str(e)}")
            raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
        finally:
            os.remove(video_file_path)
    else:
        raise HTTPException(status_code=400, detail="Uploaded file is not a video.")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
