import os
import shutil
from datetime import datetime
import platform

def get_minecraft_saves_folder():
    os_name = platform.system()
    if os_name == "Windows":
        return os.path.expanduser(r"~\AppData\Roaming\.minecraft\saves")
    elif os_name == "Darwin":
        return os.path.expanduser("~/Library/Application Support/minecraft/saves")
    elif os_name == "Linux":
        return os.path.expanduser("~/.minecraft/saves")
    else:
        raise OSError(f"Unsupported operating system: {os_name}")

def backup_worlds():
    try:
        MINECRAFT_WORLDS_DIR = get_minecraft_saves_folder()
    except OSError as e:
        print(e)
        return

    script_dir = os.path.dirname(os.path.abspath(__file__))
    BACKUP_DIR = os.path.join(script_dir, "backups")

    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)

    if not os.path.exists(MINECRAFT_WORLDS_DIR):
        print(f"Minecraft worlds directory not found: {MINECRAFT_WORLDS_DIR}")
        return

    worlds = [d for d in os.listdir(MINECRAFT_WORLDS_DIR) if os.path.isdir(os.path.join(MINECRAFT_WORLDS_DIR, d))]
    if not worlds:
        print("No worlds found to back up.")
        return

    for world in worlds:
        world_path = os.path.join(MINECRAFT_WORLDS_DIR, world)
        world_backup_dir = os.path.join(BACKUP_DIR, world)
        if not os.path.exists(world_backup_dir):
            os.makedirs(world_backup_dir)

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        backup_name = f"{world}_{timestamp}.zip"
        backup_zip_path = os.path.join(world_backup_dir, backup_name)

        print(f"Backing up {world} to {backup_zip_path}...")
        shutil.make_archive(backup_zip_path[:-4], 'zip', world_path)
        print(f"Backup saved: {backup_zip_path}")

if __name__ == "__main__":
    backup_worlds()