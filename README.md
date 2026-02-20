📂 Smart Download Sorter

A lightweight, automated Python utility designed to declutter your Downloads folder by intelligently categorizing files and directories into organized sub-folders.

✨ Features

Automated Categorization: Uses a comprehensive extension map to group files into logical categories like Images, Documents, Code, and more.

Smart Conflict Resolution: If a file with the same name already exists in the destination, the script automatically appends a counter (e.g., file_1.png) to prevent accidental overwrites.

Folder Organization: Not just for files—existing directories are moved into a dedicated Folders sub-directory.

Safe Execution: Automatically excludes its own output directory (sorter) to avoid recursive loops.

Cross-Platform Pathing: Built using pathlib to ensure it works smoothly across different operating systems.

🛠️ How It Works

The script scans your user Downloads directory and moves every item into a new folder named sorter located within Downloads. Inside sorter, items are distributed as follows:

Category

Extensions

Images

.jpg, .png, .gif, .svg, .webp, etc.

Documents

.pdf, .docx, .txt, .xlsx, .pptx, etc.

Audio

.mp3, .wav, .aac, .flac, etc.

Video

.mp4, .mkv, .mov, .avi, etc.

Archives

.zip, .rar, .7z, .tar.gz

Code

.py, .js, .html, .cpp, .json, etc.

Executables

.exe, .msi, .apk

Folders

Any existing directories

Others

Any unrecognized file extensions

🚀 Getting Started

Prerequisites

Python 3.6 or higher installed on your system.

Usage

Download or copy the sort_downloads.py script to your computer.

Open your terminal or command prompt.

Run the script:

python sort_downloads.py


📝 Customization

You can easily add new file types or change folder names by modifying the EXTENSION_MAP dictionary at the top of the script:

EXTENSION_MAP = {
    '.iso': 'Disk Images',
    '.psd': 'Design',
    # Add your own here!
}


⚠️ Note

This script moves files from the root of your Downloads folder into the sorter directory. It is always a good practice to review your files before running organization scripts on critical data.
