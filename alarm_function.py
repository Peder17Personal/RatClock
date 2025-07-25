import pygame
import time
import webbrowser
import os

# Initialize pygame mixer
pygame.init()
pygame.mixer.init()

# Local path to alarm tones
ALARM_DIR = "C:/Users/LassePedersen/Documents/GitHub/RatClock/Alarm_tones"


def play_local_alarm(version = 1):
    filename = f"{version}.mp3"
    alarm_path = os.path.join(ALARM_DIR, filename)

    if not os.path.exists(alarm_path):
        print(f"Alarm tone '{filename}' not found.")
        return

    pygame.mixer.music.load(alarm_path)
    pygame.mixer.music.play()
    print(f"Playing local alarm tone: {filename}")
    time.sleep(15)  # Let it play for 15 seconds
    pygame.mixer.music.stop()

def play_spotify_playlist():
    """Opens a Spotify playlist in the default browser."""
    playlist_url = "https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M"  # Example: "Today's Top Hits"
    print("Opening Spotify playlist...")
    webbrowser.open(playlist_url)

def play_radio_stream():
    """Plays an online radio stream using VLC or the system's default player."""
    radio_url = "https://stream.live.vc.bbcmedia.co.uk/bbc_radio_one"  # BBC Radio 1 stream
    print("Streaming internet radio...")
    os.system(f'start {radio_url}')  # Windows; use 'xdg-open' on Linux or 'open' on macOS

def play_news():
    """Simulates playing a news voice file or stream (placeholder)."""
    news_audio_path = "C:/Path/To/Your/News_Clip.mp3"  # Replace with actual news audio
    if os.path.exists(news_audio_path):
        pygame.mixer.music.load(news_audio_path)
        pygame.mixer.music.play()
        print("Playing news audio...")
        time.sleep(20)
        pygame.mixer.music.stop()
    else:
        print("News audio file not found. You could integrate a text-to-speech feed here.")

def play_text_to_speech(text="Good morning! Here's your schedule for today..."):
    """Converts text to speech and plays it (requires pyttsx3)."""
    import pyttsx3
    engine = pyttsx3.init()
    print("Speaking text...")
    engine.say(text)
    engine.runAndWait()

# Example usage:
if __name__ == "__main__":
    print("Choose an audio type to play:")
    print("1. Local Alarm")
    print("2. Spotify Playlist")
    print("3. Internet Radio")
    print("4. News Audio")
    print("5. Text-to-Speech")

    choice = input("Enter number: ")

    if choice == "1":
        play_local_alarm(2)
    elif choice == "2":
        play_spotify_playlist()
    elif choice == "3":
        play_radio_stream()
    elif choice == "4":
        play_news()
    elif choice == "5":
        play_text_to_speech()
    else:
        print("Invalid choice.")
