from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return transcript
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    video_id = "O6katN2_SQg"  # Replace with your YouTube video ID
    transcript = get_transcript(video_id)
    if transcript:
        for entry in transcript:
            #print(f"{entry['start']}: {entry['text']}")
            print(f"{entry['text']}")