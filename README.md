# Minecraft Backup Tool

A simple Python script to automatically back up Minecraft Java Edition worlds, organising them with timestamps for easy management and restoration.

## Features

- Automatically detects the Minecraft saves folder based on your operating system (Windows, macOS, Linux).
- Backs up all Minecraft worlds in the saves directory.
- Organises backups into folders named after each world.
- Adds a timestamp to each backup for easy versioning.
- Creates a `.zip` archive for each world backup.

## Requirements

- Python 3.x
- `shutil` and `os` (both are included in Python's standard library)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/MinecraftWorldBackup.git
2. Navigate to the project directory:

	```bash
	cd MinecraftWorldBackup
3. Run the script

	```bash
    python backup_worlds.py
## How It Works
- The script detects your Minecraft saves folder based on your operating system:
  - **Windows**: AppData/Roaming/.minecraft/saves
  - **macOS**: Library/Application Support/minecraft/saves
  - **Linux**: ~/.minecraft/saves

- It then creates a backup of each world in a backups folder within the script's directory.
- Each backup is stored in a .zip file, named after the world and the timestamp of when the backup was made.
