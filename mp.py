import os
from PyPDF2 import PdfMerger

def fetch_all_pdfs(folder_path):
    """Recursively fetch all PDF file paths from the folder."""
    pdf_files = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith('.pdf'):
                pdf_files.append(os.path.join(root, file))
    return pdf_files

def merge_pdfs(pdf_list, output_path):
    """Merge multiple PDFs into a single PDF file."""
    merger = PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write(output_path)
    merger.close()
    print(f"Merged {len(pdf_list)} PDFs into {output_path}")

if __name__ == "__main__":
    folder = "./pdf_folder"  # Folder containing PDFs to merge
    output_pdf = "./merged_output.pdf"  # Output merged PDF file
    
    pdf_files = fetch_all_pdfs(folder)
    if not pdf_files:
        print("No PDF files found in the specified folder.")
    else:
        merge_pdfs(pdf_files, output_pdf)
