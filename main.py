import os
from PyPDF2 import PdfMerger
from pypdf import PdfReader


def merge_pdfs(file_directory, output_filename="merged.pdf"):
    """
  Merges all PDF files in a given directory into a single PDF file.

  Args:
      file_directory (str): The path to the directory containing the PDF files.
      output_filename (str, optional): The name of the output PDF file.
          Defaults to "merged.pdf".

  Returns:
      None
  """

    pdf_merger = PdfMerger()

    for filename in os.listdir(file_directory):
        if filename.endswith(".pdf"):
            file_path = os.path.join(file_directory, filename)
            with open(file_path, 'rb') as pdf_file:
                pdf_merger.append(pdf_file)

    with open(os.path.join(file_directory, output_filename), 'wb') as output_file:
        pdf_merger.write(output_file)

    print(f"Merged PDFs successfully! Output file: {os.path.join(file_directory, output_filename)}")


def extract_text(pdf_file_path):
    """
    Extracts text from a PDF file.

    Args:
      pdf_file_path (str): The path to the PDF file.

    Returns:
      str: The extracted text from the PDF file.
    """
    reader = PdfReader(pdf_file_path)
    all_pages = reader.pages
    # Save to a text file
    text_file_path = pdf_file_path.replace(".pdf", ".txt")
    with open(text_file_path, "w") as text_file:
        for pages in all_pages:
            text_file.write(pages.extract_text())

    count = 0
    for image_file_object in all_pages[0].images:
        with open(str(count) + image_file_object.name, "wb") as fp:
            fp.write(image_file_object.data)
            count += 1


if __name__ == '__main__':
    current_dir = os.path.dirname(os.path.abspath(__file__))
    directory = os.path.join(current_dir, "pdf_files")
    merge_pdfs(directory)

    # merged_pdf = os.path.join(directory, "merged.pdf")
    # extract_text(merged_pdf)

