
---

# FastAPI Video to MP3 Converter

This is a simple FastAPI application that provides a REST API endpoint for converting video files to MP3 audio files.

## Features

- Upload a video file (MP4, AVI, etc.) to the server.
- Convert the uploaded video file to an MP3 audio file.
- Download the converted MP3 audio file.

## Prerequisites

- Python 3.6+
- pip (Python package installer)

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/TheHRC/video-to-audio-fastapi.git
   ```

2. Navigate to the project directory:

   ```bash
   cd fastapi-video-to-mp3-converter
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the FastAPI server:

   ```bash
   uvicorn main:app --reload
   ```

   The server will start running on `http://localhost:8000`.

2. Open your web browser or use a tool like [Postman](https://www.postman.com/) to interact with the API.

3. Upload a video file using the `/convert/` endpoint. The server will return the converted MP3 audio file.

## API Endpoints

### `/convert/` (POST)

- **Request Parameters**:
  - `file` (multipart/form-data): The video file to be converted.
  

- **Response**:
  - Returns the converted MP3 audio file.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request if you have any suggestions or improvements.

## License

This project is licensed under the [MIT License](LICENSE).

---
