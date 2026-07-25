# # from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled


# from youtube_transcript_api import YouTubeTranscriptApi



# video_id = "Gfr50f6ZBvo" # only the ID, not full URL
# try:
#     # If you don’t care which language, this returns the “best” one
#     api = YouTubeTranscriptApi()
#     transcript_data = api.fetch(video_id, languages=["en"])

#     # Flatten it to plain text
#     transcript = " ".join(snippet.text for snippet in transcript_data)
#     print(transcript)

# except:
#     print("No captions available for this video.")


from youtube_transcript_api import YouTubeTranscriptApi


def get_transcript(video_id: str):

    try:
        api = YouTubeTranscriptApi()

        transcript_data = api.fetch(
            video_id,
            languages=["en"]
        )

        transcript = " ".join(
            snippet.text for snippet in transcript_data
        )

        return transcript

    except Exception as e:
        print(e)
        return None