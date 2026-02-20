import os
import shutil
from pathlib import Path

# Common file extensions and their corresponding category folders
EXTENSION_MAP = {
    # Images
    '.jpg': 'Images', '.jpeg': 'Images', '.png': 'Images', '.gif': 'Images',
    '.bmp': 'Images', '.svg': 'Images', '.webp': 'Images',
    # Documents
    '.pdf': 'Documents', '.doc': 'Documents', '.docx': 'Documents',
    '.txt': 'Documents', '.rtf': 'Documents', '.csv': 'Documents',
    '.xls': 'Documents', '.xlsx': 'Documents', '.ppt': 'Documents',
    '.pptx': 'Documents',
    # Audio
    '.mp3': 'Audio', '.wav': 'Audio', '.aac': 'Audio', '.flac': 'Audio',
    '.ogg': 'Audio',
    # Video
    '.mp4': 'Video', '.mkv': 'Video', '.avi': 'Video', '.mov': 'Video',
    '.wmv': 'Video', '.flv': 'Video',
    # Archives
    '.zip': 'Archives', '.rar': 'Archives', '.7z': 'Archives',
    '.tar': 'Archives', '.gz': 'Archives',
    # Executables/Installers
    '.exe': 'Executables', '.msi': 'Executables', '.apk': 'Executables',
    # Code/Scripts
    '.py': 'Code', '.js': 'Code', '.html': 'Code', '.css': 'Code',
    '.cpp': 'Code', '.c': 'Code', '.java': 'Code', '.json': 'Code'
}

def sort_downloads():
    # Define paths
    home_dir = Path.home()
    downloads_dir = home_dir / 'Downloads'
    sorter_dir = downloads_dir / 'sorter'

    # Check if Downloads directory exists
    if not downloads_dir.exists():
        print(f"Error: Could not find Downloads folder at {downloads_dir}")
        return

    # Create the base 'sorter' directory if it doesn't exist
    sorter_dir.mkdir(exist_ok=True)
    print(f"Sorting files into: {sorter_dir}")

    # Keep track of how many files we moved
    moved_count = 0

    # Iterate over all items in the Downloads directory
    for item in downloads_dir.iterdir():
        # Skip the sorter directory itself to avoid recursive moving
        if item.name == 'sorter':
            continue

        if item.is_file():
            file_extension = item.suffix.lower()
            
            # Determine the subfolder name based on the extension
            folder_name = EXTENSION_MAP.get(file_extension, 'Others')
            
        elif item.is_dir():
            # If it's a directory, put it in the 'Folders' subfolder
            folder_name = 'Folders'
        else:
            continue
            
        # Create the specific subfolder inside 'sorter'
        target_folder = sorter_dir / folder_name
        target_folder.mkdir(exist_ok=True)
        
        # Define the target path for the item
        target_path = target_folder / item.name
        
        # Check if an item with the same name already exists in the target folder
        # If it does, we can append a number to the name to avoid overwriting
        counter = 1
        while target_path.exists():
            if item.is_file():
                new_name = f"{item.stem}_{counter}{item.suffix}"
            else:
                new_name = f"{item.name}_{counter}"
            target_path = target_folder / new_name
            counter += 1
            
        try:
            # Move the item
            shutil.move(str(item), str(target_path))
            print(f"Moved: {item.name} -> {folder_name}/")
            moved_count += 1
        except Exception as e:
            print(f"Error moving {item.name}: {e}")

    print(f"\nSorting complete! Successfully moved {moved_count} items...")

if __name__ == "__main__":
    sort_downloads()
