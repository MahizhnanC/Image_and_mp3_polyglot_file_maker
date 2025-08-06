# Image and MP3 Polyglot File Maker

A simple Python tool to create a **polyglot file** that acts both as an image and as an MP3 file — depending on the file extension used.

---

## How it works

This tool appends MP3 data to the end of an image file (JPG or PNG). Image viewers ignore the MP3 tail, and audio players ignore the image header — giving you a true dual-behaving polyglot file.

---

## Features

- Combine any `.jpg`/`.png` image with a `.mp3` file.
- Result can be renamed to `.jpg` or `.mp3` and used accordingly.
- Lightweight & offline — works with Python 3 on Linux.

---

## 🛠Usage

### 1. Clone the repo
```bash
git clone https://github.com/MahizhnanC/Image_and_mp3_polyglot_file_maker.git
cd Image_and_mp3_polyglot_file_maker
```

### 2. Make the script executable (optional)
```bash
chmod +x src/poly.py
```

### 3. Run the script
```bash
python3 src/poly.py
```

---

## Example

You’ll be prompted like:

```
Enter full path to the image file (.jpg/.png): /home/user/pic.png
Enter full path to the MP3 file: /home/user/music.mp3
Enter full path for the output file: /home/user/output.poly
```

Then you can:
- Rename `output.poly` to `output.jpg` to view the image.
- Rename `output.poly` to `output.mp3` to play the audio.

---

##  Tested On

- Kali Linux 2025
- Ubuntu 22.04
- Arch Linux

---

##  License

MIT License — see [LICENSE](LICENSE) file for full text.
