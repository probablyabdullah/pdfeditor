import streamlit as st
import PyPDF2
from io import BytesIO
st.set_page_config(page_title="PDF Editor", page_icon="favicon.png", layout="centered", initial_sidebar_state="auto", menu_items=None)
st.title("PDF Merger App")



# Use st.file_uploader to allow users to upload files with drag-and-drop support
pdf_files_input = st.file_uploader("Drag and drop PDF files here to merge (you can also click to upload):", type="pdf", accept_multiple_files=True)

if pdf_files_input is not None:
    merger = PyPDF2.PdfMerger()

    # Loop through uploaded files
    for pdf_file in pdf_files_input:
        # Save the uploaded file temporarily
        with open(pdf_file.name, "wb") as temp_file:
            temp_file.write(pdf_file.getbuffer())
        
        # Add the file to the merger
        merger.append(pdf_file.name)

    # Use st.text_input for getting the output filename
    output_filename = st.text_input("Enter the desired name for the merged PDF (without extension): ")

    # Ensure .pdf extension is added if not already present
    if not output_filename.endswith(".pdf"):
        output_filename += ".pdf"

    # Save the merged PDF to a BytesIO object
    merged_pdf_bytes = BytesIO()
    merger.write(merged_pdf_bytes)

    # Display success message only when merging occurs
    if len(merger.pages) > 0:
        st.success("PDF files merged successfully!")

       

    # Add a download button for the merged PDF
    st.download_button(
        label="Download Merged PDF",
        data=merged_pdf_bytes.getvalue(),
        file_name=output_filename,
        key="download_button"
    )


# Add a line indicating the creator
st.write("Made by Abdullah Amal Khan")
