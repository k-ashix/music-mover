# music-mover
A Python command-line tool that scans Windows drives for MP3 files and consolidates them into a single organized folder. Features drive detection, recursive file search, size calculation, file list export, and real-time progress tracking.
--------------------------------------------------------------------------

# A command line 🎵 Music Organizer

A lightweight Python script designed to help you organize scattered MP3 files across your Windows system. Simply select a drive, create a destination folder, and let the script find and consolidate all your music files automatically.

## Overview

Music Organizer is a command-line utility that automates the tedious task of locating and organizing MP3 files spread across multiple folders and drives. Built with Python's standard library, it provides an interactive interface for scanning, previewing, and moving your music collection to a centralized location.

## Key Features

- **Automatic Drive Detection** - Scans and displays all available drives on your Windows system
- **Recursive File Search** - Finds MP3 files in all subdirectories of the selected drive
- **Smart Size Calculation** - Displays total file size in human-readable format (B, KB, MB, GB, TB)
- **Interactive Preview** - Option to view all discovered files before moving them
- **List Export** - Saves a detailed inventory of found files to a text document
- **Progress Tracking** - Real-time feedback during file operations (V.2)
- **User-Friendly Interface** - Clear prompts, emoji indicators, and organized output

## How It Works

1. Detects available drives on your system
2. Prompts you to select a drive to scan
3. Creates a custom-named destination folder
4. Recursively searches the entire drive for .mp3 files
5. Displays file count and total size
6. Offers preview and export options
7. Moves all files to the destination with progress updates

## Technical Details

- **Language:** Python
- **Dependencies:** None (uses standard library only)
- **Platform:** Windows
- **Libraries Used:** `shutil`, `os`, `pathlib`, `string`,

## Use Cases

- Consolidating music from multiple external drives
- Organizing downloads scattered across folders
- Preparing music libraries for backup
- Cleaning up duplicate folder structures
- Creating a centralized music collection
