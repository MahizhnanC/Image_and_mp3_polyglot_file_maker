#!/usr/bin/env python3

import os

def read_binary(path):
    with open(path, 'rb') as f:
        return f.read()

def write_binary(path, data):
    with open(path, 'wb') as f:
        f.write(data)

def create_polyglot_image_mp3(image_path, mp3_path, output_path):
    # Read the image and mp3 data
    image_data = read_binary(image_path)
    mp3_data = read_binary(mp3_path)

    # Combine the image with the mp3
    polyglot_data = image_data + mp3_data
    write_binary(output_path, polyglot_data)

    print(f"\n[+] Polyglot file created at: {output_path}")
    print(" Rename it to .jpg/.png to view the image.")
    print(" Rename it to .mp3 to play the audio.\n")

def main():
    print("== Image + MP3 Polyglot Generator ==")
    
    image_path = input("Enter full path to the image file (.jpg/.png): ").strip()
    if not os.path.isfile(image_path):
        print("[-] Image file not found.")
        return

    mp3_path = input("Enter full path to the MP3 file: ").strip()
    if not os.path.isfile(mp3_path):
        print("[-] MP3 file not found.")
        return

    output_path = input("Enter full path for the output file (e.g., /path/to/output.mp3): ").strip()
    output_dir = os.path.dirname(output_path)
    if not os.path.isdir(output_dir):
        print("[-] Output directory does not exist.")
        return

    create_polyglot_image_mp3(image_path, mp3_path, output_path)

if __name__ == "__main__":
    main()
