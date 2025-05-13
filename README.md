
# mergerPDF

A simple Python tool to automatically merge multiple PDF files into a single PDF document. This project is useful for combining separate PDF files quickly and efficiently.

---

## Features

- Merge all PDF files found in a specified folder (including subfolders)  
- Preserve the order of PDFs based on filename or folder traversal  
- Easy to use and extend  
- Cross-platform (Windows, macOS, Linux)  

---

## Requirements

- Python 3.6+  
- [`PyPDF2`](https://pypi.org/project/PyPDF2/) library for PDF merging  

---

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/pook1337/mergerPDF.git
   cd mergerPDF
   ```

2. Install the required Python package:

   ```
   pip install PyPDF2
   ```

---

## Usage

1. Place all the PDF files you want to merge inside a folder (e.g., `pdf_folder`).

2. Edit the script `mp.py` if needed to specify your folder path and output file name.

3. Run the script:

   ```
   python mp.py
   ```

4. The merged PDF will be saved to the output path specified in the script.

---

## How it works

- The script scans the specified folder and its subfolders for PDF files.  
- It merges all found PDFs into a single PDF file using PyPDF2's `PdfMerger`.  
- The output is saved as a new PDF file.

---

## Notes

- The merge order depends on the order in which the files are found. You can modify the script to sort files by name or date if needed.  
- Make sure all PDF files are not password protected, or extend the script to handle encrypted PDFs.  
- Backup your original files before merging to prevent accidental data loss.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

