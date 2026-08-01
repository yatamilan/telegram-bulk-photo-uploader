from telethon import TelegramClient
from pathlib import Path
import asyncio

# ==============================
# TELEGRAM SETTINGS
# ==============================

api_id = 31601941
api_hash = "c054722cb5161ad9617d05f310c597b8"

channel_id = 5374330402

PHOTO_FOLDER = "PHOTO"

client = TelegramClient("session", api_id, api_hash)


async def main():

    files = sorted(Path(PHOTO_FOLDER).glob("*"))

    total = len(files)

    if total == 0:
        print("No files found.")
        return

    print(f"Found {total} files.\n")

    for i, file in enumerate(files, start=1):

        print(f"[{i}/{total}] Uploading {file.name}")

        try:
            await client.send_file(
                channel_id,
                str(file)
            )

            print("Uploaded successfully.\n")

            # Small pause to avoid flooding
            await asyncio.sleep(2)

        except Exception as e:
            print(f"Failed: {e}\n")

    print("=" * 40)
    print("ALL FILES UPLOADED")
    print("=" * 40)


with client:
    client.loop.run_until_complete(main())