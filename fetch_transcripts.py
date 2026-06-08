from youtube_transcript_api import YouTubeTranscriptApi
import os

videos = [
    ("kevin-indig", "kevin-indig-ai-seo-strategy", "JLpVV0sQrfg"),
    ("aleyda-solis", "aleyda-seo-tutorial", "hBef1MPnVN4"),
    ("kyle-roof", "kyle-roof-seo-experiment", "eYo1kqkKFBA"),
    ("bernard-huang", "bernard-huang-content-optimization", "4KyYqe1s_XY"),
    ("lazarina-stoy", "lazarina-stoy-seo", "GxFfDgQ7b_c"),
]

ytt = YouTubeTranscriptApi()

for author, slug, video_id in videos:
    try:
        fetched = ytt.fetch(video_id)
        text = "\n".join([snippet.text for snippet in fetched])
        out_dir = f"research/youtube-transcripts/{author}"
        os.makedirs(out_dir, exist_ok=True)
        with open(f"{out_dir}/{slug}.md", "w", encoding="utf-8") as f:
            f.write(f"# Transcript: {slug}\n\n")
            f.write(f"**Video:** https://www.youtube.com/watch?v={video_id}\n\n")
            f.write("---\n\n")
            f.write(text)
        print(f"Saved: {author}/{slug}")
    except Exception as e:
        print(f"Failed {author}: {e}")