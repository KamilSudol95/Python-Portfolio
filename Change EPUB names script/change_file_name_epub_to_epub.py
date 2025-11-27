import os
import re
import wordninja

# Folder path
epub_dir = r"C:\Users\kamil\Desktop\Books\Data Engineering & Science"

def prettify_name(filename):

    name = os.path.splitext(filename)[0]

    #Separators to spaces
    name = re.sub(r'[_\-\.]+', ' ', name)

    #Word segmentation
    parts = []
    for chunk in name.split():
        segmented = wordninja.split(chunk)
        parts.extend(segmented)

    #Joining and cleaning
    clean = " ".join(parts)
    clean = re.sub(r'\s+', ' ', clean).strip()

    # Init caps
    clean = clean.title()

    return clean + ".epub"

#Catch list of EPUB files
epub_files = [f for f in os.listdir(epub_dir) if f.lower().endswith('.epub')]

# Renaming
for epub in epub_files:
    old_path = os.path.join(epub_dir, epub)
    new_name = prettify_name(epub)
    new_path = os.path.join(epub_dir, new_name)

    if old_path != new_path:
        os.rename(old_path, new_path)
        print(f"✅ '{epub}' → '{new_name}'")
    else:
        print(f"ℹ️ Already formatted: {epub}")
