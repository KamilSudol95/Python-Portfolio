from lxml import etree as et
from pathlib import Path

folder = Path(r"C:\Users\kamil\Desktop\Pénz - Kamil Sudoł\JPK")

for file in folder.glob("*.xml"):
    print(f"\nPrzetwarzam: {file.name}")

    tree = et.parse(str(file))
    root = tree.getroot()

    year_list = root.xpath("//*[local-name()='Rok']/text()")
    month_list = root.xpath("//*[local-name()='Miesiac']/text()")

    if not year_list or not month_list:
        print("❌ Brak Rok lub Miesiac – pomijam plik")
        continue

    year = year_list[0]
    month = month_list[0].zfill(2)

    new_name = f"JPK_V7_{year}_{month}.xml"
    new_path = file.with_name(new_name)

    if new_path.exists():
        print("⚠️ Plik już istnieje – pomijam")
        continue

    file.rename(new_path)
    print(f"✅ Zmieniono na: {new_name}")