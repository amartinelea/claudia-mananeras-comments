import os
import pandas as pd
from dotenv import load_dotenv
from googleapiclient.discovery import build

# Cargar clave API desde .env
load_dotenv()
API_KEY = os.getenv("API_KEY")

# Inicializar cliente de YouTube
youtube = build("youtube", "v3", developerKey=API_KEY)

# Canal oficial de Claudia Sheinbaum
CHANNEL_ID = "UC6mvc52_1j0okpAaXJj2c_Q"

def get_video_ids(channel_id, max_results=10):
    """Obtiene los IDs de los últimos videos subidos al canal"""
    request = youtube.search().list(
        part="id",
        channelId=channel_id,
        maxResults=max_results,
        order="date",
        type="video"
    )
    response = request.execute()
    return [item["id"]["videoId"] for item in response["items"]]

def get_video_title(video_id):
    """Devuelve el título del video dado su ID"""
    response = youtube.videos().list(part="snippet", id=video_id).execute()
    items = response.get("items", [])
    return items[0]["snippet"]["title"] if items else "Unknown Title"

def get_comments(video_id, max_comments=200):
    """Extrae comentarios de un video específico"""
    comments = []
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=100,
        textFormat="plainText"
    )
    while request and len(comments) < max_comments:
        response = request.execute()
        for item in response["items"]:
            top_comment = item["snippet"]["topLevelComment"]["snippet"]
            comments.append({
                "comment_id": item["id"],
                "text": top_comment["textDisplay"],
                "video_id": video_id,
                "video_title": get_video_title(video_id)
            })
        request = youtube.commentThreads().list_next(request, response)
    return comments[:max_comments]


def save_to_csv(comments, filename="data/dataset.csv"):
    """Guarda todos los comentarios en un archivo CSV"""
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    df = pd.DataFrame(comments)
    df.to_csv(filename, index=False)
    print(f"Guardado en {filename} ({len(comments)} comentarios)")

def main():
    all_comments = []
    video_ids = get_video_ids(CHANNEL_ID, max_results=10)
    for video_id in video_ids:
        print(f"Extrayendo de video {video_id}")
        try:
            comments = get_comments(video_id, max_comments=100)
            all_comments.extend(comments)
        except Exception as e:
            print(f"Error: {e}")
    save_to_csv(all_comments)

if __name__ == "__main__":
    main()
