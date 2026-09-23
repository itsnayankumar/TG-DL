from os.path import splitext
import re

def is_media(message):
    """
    Extracts playable or downloadable media from a Pyrogram message.
    Prioritizes video and document over photo so video thumbnails don't override video files.
    """
    media_attrs = ["video", "document", "audio", "animation", "voice", "video_note", "photo"]
    return next((getattr(message, attr) for attr in media_attrs if getattr(message, attr)), None)


def get_media_properties(message):
    """
    Safely extracts title, file size, hash, and mime type for database indexing.
    """
    file = is_media(message)
    if not file:
        return None

    file_size = getattr(file, "file_size", 0)
    file_unique_id = getattr(file, "file_unique_id", "nohash")[:6]
    mime_type = getattr(file, "mime_type", "video/mp4") or "video/mp4"

    # Fallback title if video attribute has no filename
    raw_name = getattr(file, "file_name", None) or message.caption or f"Media_{message.id}"
    title, _ = splitext(raw_name)
    title = re.sub(r'[.,|_\',]', ' ', title).strip()

    return {
        "msg_id": message.id,
        "title": title,
        "hash": file_unique_id,
        "size": file_size,
        "type": mime_type,
        "chat_id": str(message.chat.id) if message.chat else ""
    }
