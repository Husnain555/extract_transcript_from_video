from langchain_community.document_loaders import YoutubeLoader

url = input("Enter YouTube URL: ")
loader = YoutubeLoader.from_youtube_url(url,add_video_info=False)
doc = loader.load()

for do in doc:
    print(do)