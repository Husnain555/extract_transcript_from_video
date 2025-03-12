from langchain_community.document_loaders import YoutubeLoader

url = input("Enter YouTube URL: ")
loader = YoutubeLoader.from_youtube_url(url, add_video_info=False)

doc = loader.load()
print(f"Raw Output: {doc}")  # Debugging Step

for do in doc:
    print(f"Document: {do.page_content}")  # Debugging Step
