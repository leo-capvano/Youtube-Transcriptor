from langchain_community.document_loaders.youtube import YoutubeLoader


def transcript_video(yt_video_url: str, add_video_info: bool, languages: list, translation: str):
    loader = YoutubeLoader.from_youtube_url(
        yt_video_url,
        add_video_info=add_video_info,
        language=languages,
        translation=translation
    )
    return loader.load()
