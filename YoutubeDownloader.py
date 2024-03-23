from pytube import YouTube

# Enter the YouTube video URL
url = input("Enter the URL of the YouTube video: ")

# Create a YouTube object
yt = YouTube(url)

# Get the available video streams
streams = yt.streams

# Filter the streams to get the ones with the desired resolution
video_streams = streams.filter(progressive=True)

# Print the available video streams
print("Available video streams:")
for i, stream in enumerate(video_streams):
    print(f"{i+1}. {stream.resolution}")

# Ask the user to choose the desired resolution
choice = int(input("Enter the number corresponding to the desired resolution: "))
selected_stream = video_streams[choice - 1]

# Download the video
print(f"Downloading {yt.title}...")
selected_stream.download()
print("Download complete!")