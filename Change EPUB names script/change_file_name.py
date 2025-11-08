import os
import re
from difflib import SequenceMatcher

#Folder paths
pdf_dir = r"C:\Users\kamil\Desktop\Books\Security"
epub_dir = r"C:\Users\kamil\Desktop\Books\Security\EPUB"

def normalize_name(filename):
    """deletes space, special characters and converts name to lowercase."""
    name = os.path.splitext(filename)[0]
    name = re.sub(r'[^a-z0-9]', '', name.lower())
    return name

# Download files within each directory
pdf_files = [f for f in os.listdir(pdf_dir) if f.lower().endswith('.pdf')]
epub_files = [f for f in os.listdir(epub_dir) if f.lower().endswith('.epub')]

#  PDF ↔ EPUB mapping based on name similarity
for pdf in pdf_files:
    norm_pdf = normalize_name(pdf)
    best_match = None
    best_ratio = 0.0
    for epub in epub_files:
        norm_epub = normalize_name(epub)
        ratio = SequenceMatcher(None, norm_pdf, norm_epub).ratio()
        if ratio > best_ratio:
            best_match = epub
            best_ratio = ratio

    # Rename if similarity is above threshold
    if best_ratio > 0.8 and best_match:
        old_path = os.path.join(epub_dir, best_match)
        new_name = os.path.splitext(pdf)[0] + ".epub"
        new_path = os.path.join(epub_dir, new_name)

        #name change
        if old_path != new_path:
            os.rename(old_path, new_path)
            print(f"✅ Changed name: '{best_match}' → '{new_name}' (similarity: {round(best_ratio, 2)})")
    else:
        print(f"⚠️ A match was not found for: {pdf}")
