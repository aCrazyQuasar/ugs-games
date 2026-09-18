from pathlib import Path
import tkinter as tk
from tkinter import filedialog


def main():
    root = tk.Tk()
    root.withdraw()

    # Choose the directory to scan
    directory = filedialog.askdirectory(
        title="Choose a directory to scan"
    )

    if not directory:
        print("No directory selected.")
        return

    directory = Path(directory)

    # Choose where to save the output file
    output_file = filedialog.asksaveasfilename(
        title="Save file list",
        defaultextension=".txt",
        filetypes=[
            ("Text files", "*.txt"),
            ("All files", "*.*")
        ]
    )

    if not output_file:
        print("No output file selected.")
        return

    # Get all files in the selected directory
    files = sorted(
        file.name
        for file in directory.iterdir()
        if file.is_file()
    )

    # Write the filenames to the text file
    Path(output_file).write_text(
        "\n".join(files),
        encoding="utf-8"
    )

    print(f"Found {len(files)} files.")
    print(f"Saved file list to: {output_file}")


if __name__ == "__main__":
    main()