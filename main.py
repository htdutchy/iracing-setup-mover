import shutil
import yaml
from pathlib import Path

config_path = Path("config.yaml")
downloads_dir = Path.home() / "Downloads"
iracing_setups_base = Path.home() / "Documents/iRacing/setups"

def load_config():
    with open(config_path) as f:
        return yaml.safe_load(f)

def move_old_setups(setup_folder):
    old_dir = setup_folder / "old"
    old_dir.mkdir(exist_ok=True)
    for file in setup_folder.glob("VRS_*.sto"):
        print(f"  Moving old setup to: {old_dir / file.name}")
        shutil.move(str(file), old_dir / file.name)

def prompt_create_dir(path):
    response = input(f"  Folder '{path}' does not exist. Create it? (y/n): ").strip().lower()
    if response == 'y':
        path.mkdir(parents=True, exist_ok=True)
        print(f"  Created folder: {path}")
        return True
    return False

def move_new_setups():
    config = load_config()
    default_glob = config.get("default_glob", "VRS_*.sto")
    mappings = config.get("mappings", {})

    print("Starting setup file transfer...")

    for match, setup_subdir in mappings.items():
        setup_dir = iracing_setups_base / setup_subdir
        if not setup_dir.exists():
            print(f"\nTarget folder '{setup_dir}' not found.")
            if not prompt_create_dir(setup_dir):
                print(f"  Skipping: {setup_dir}")
                continue

        for file in downloads_dir.glob(default_glob):
            if match in file.name:
                print(f"\nFound: {file.name}")
                print(f"  Target folder: {setup_dir}")

                move_old_setups(setup_dir)
                shutil.move(str(file), setup_dir / file.name)
                print(f"  Moved new setup to: {setup_dir / file.name}")

    print("\nSetup transfer complete.")
    input("Press Enter to exit...")

if __name__ == "__main__":
    move_new_setups()
