# Telegram Bulk Photo Uploader

Automatically upload hundreds or thousands of photos from your computer to a Telegram channel using **Python** and **Telethon**.

Perfect for:
- 📷 Photo backup
- ☁️ Cloud storage
- 📁 Image archiving
- 📸 Gallery migration
- 🤖 Automation projects

---

## Features

- ✅ Upload unlimited photos
- ✅ Upload an entire folder automatically
- ✅ Supports JPG, JPEG, PNG, WEBP and other image formats
- ✅ Progress counter
- ✅ Error handling
- ✅ Simple and lightweight
- ✅ Uses the official Telegram API (Telethon)
- ✅ Beginner-friendly

---

## Project Structure

```text
project/
│
├── upload.py
├── PHOTO/
│   ├── img1.jpg
│   ├── img2.jpg
│   ├── img3.jpg
│   ├── img4.png
│   └── ...
```

Place all your photos inside the **PHOTO** folder.

---

## Requirements

- Python 3.10+
- Telethon

Install Telethon:

```bash
pip install telethon
```

---

## Get Telegram API Credentials

Visit:

https://my.telegram.org

Login with your Telegram account and create an application to get:

- API ID
- API Hash

---

## Configuration

Open `upload.py` and replace:

```python
api_id = YOUR_API_ID
api_hash = "YOUR_API_HASH"

channel_id = YOUR_CHANNEL_ID
```

Example:

```python
api_id = 12345678
api_hash = "xxxxxxxxxxxxxxxxxxxxxxxx"

channel_id = -1001234567890
```

---

## Run

```bash
python upload.py
```

---

## Example Output

```text
Found 250 files.

[1/250] Uploading img1.jpg
Uploaded successfully.

[2/250] Uploading img2.jpg
Uploaded successfully.

...

========================================
ALL FILES UPLOADED
========================================
```

---

## Supported Files

- JPG
- JPEG
- PNG
- WEBP
- GIF
- BMP

---

## Built With

- Python
- Telethon
- Asyncio

---

## Notes

- Keep all images inside the `PHOTO` folder.
- Large uploads may take time depending on your internet speed.
- A small delay between uploads helps prevent Telegram flood limits.

---

## License

MIT License

---

## Keywords

telegram uploader, telegram bulk uploader, telegram photo uploader, telegram image uploader, telethon uploader, python telegram bot, telegram automation, bulk image upload, telegram channel uploader, python automation, telethon script, telegram cloud storage, upload photos to telegram, telegram backup, telegram media uploader
