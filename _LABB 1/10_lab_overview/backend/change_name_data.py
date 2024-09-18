
# importera pathlib ge det namnet Path
from pathlib import Path
# importera shutil använd copytree och rmtree
from shutil import copytree, rmtree

#path till raw_data och cleaned_data i deta fall samma folder som scriptet i ligger i
raw_data_path = Path(__file__).parent / "raw_data"
cleaned_data_path = Path(__file__).parent / "cleaned_data"

# ifall cleaned_data finns ta bort hela trädet (folder strukturen som ser ut som ett träd)
if cleaned_data_path.is_dir():
    rmtree(cleaned_data_path)

#skapa cleaned_data folder
cleaned_data_path.mkdir(parents=True, exist_ok=True)

# för raw_data foldern, skapa nya folders som tar bort allt efter första meningen och kopiera det till cleaned_data med deras nya namn
for folder in raw_data_path.iterdir():
    new_name = folder.name.split()[0]
    copytree(folder, cleaned_data_path / new_name)

