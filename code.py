# from google import genai

# client = genai.Client(api_key="AkhilIzaSyCZhmMhR9jZglN8UZ0eZmzzv7IzpHrrFmc")
# response = client.models.generate_content(
#     model="gemini-2.0-flash", contents="Explain how AI works in 10 words"
# )
# print(response.text)



# import os
# from PyPDF2 import PdfReader
# from reportlab.lib import colors
# from reportlab.lib.pagesizes import A4
# from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
# from reportlab.lib.styles import getSampleStyleSheet
# from google import genai

# # Step 1: Read PDF content
# def read_pdf(file_path):
#     pdf_reader = PdfReader(file_path)
#     text = ""
#     for page in pdf_reader.pages:
#         text += page.extract_text()
#     return text

# # Step 2: Use GenAI to summarize content
# def summarize_text(text):
#     client = genai.Client(api_key="AkhilIzaSyCZhmMhR9jZglN8UZ0eZmzzv7IzpHrrFmc")
#     prompt = f"Summarize the following text concisely:\n{text}"
#     response = client.models.generate_content(model="gemini-2.0-flash", contents=prompt)
#     return response.text

# # Step 3: Save summary as a PDF
# def save_summary_as_pdf(summary, output_file):
#     doc = SimpleDocTemplate(output_file, pagesize=A4)
#     styles = getSampleStyleSheet()
#     elements = []

#     elements.append(Paragraph("Summary", styles['Heading1']))
#     elements.append(Spacer(1, 12))
#     elements.append(Paragraph(summary, styles['BodyText']))

#     doc.build(elements)

# # Main function to execute the process
# input_pdf = "C:/Users/byred/Downloads/FRONTIER SPRING.pdf"       # Replace with your input PDF file path
# output_pdf = "C:/Users/byred/Downloads/summary_output.pdf"  # Replace with your desired output PDF file path

# pdf_content = read_pdf(input_pdf)
# summary = summarize_text(pdf_content)
# save_summary_as_pdf(summary, output_pdf)

# print(f"Summary saved to {output_pdf}")



# import os
# from PyPDF2 import PdfReader
# from reportlab.lib.pagesizes import A4
# from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
# from reportlab.lib.styles import getSampleStyleSheet
# from google import genai

# # 🔑 Read API Key from Environment Variable
# api_key = 'AIzaSyCZhmMhR9jZglN8UZ0eZmzzv7IzpHrrFmc'
# if not api_key:
#     raise ValueError("Google GenAI API key not found. Please set the GENAI_API_KEY environment variable.")
# client = genai.Client(api_key=api_key)

# # 📄 Read PDF content
# def read_pdf(file_path):
#     try:
#         pdf_reader = PdfReader(file_path)
#         text = ""
#         for page in pdf_reader.pages:
#             text += page.extract_text()
#         return text
#     except Exception as e:
#         print(f"Error reading {file_path}: {e}")
#         return ""

# # 🤖 Use GenAI to summarize content
# def summarize_text(text):
#     try:
#         prompt = f"Summarize the following text concisely:\n{text}"
#         response = client.models.generate_content(model="gemini-2.0-flash", contents=prompt)
#         return response.text
#     except Exception as e:
#         print(f"Error summarizing text: {e}")
#         return "Summary unavailable due to an error."

# # 📄 Save summary as a PDF
# def save_summary_as_pdf(summary, output_file):
#     doc = SimpleDocTemplate(output_file, pagesize=A4)
#     styles = getSampleStyleSheet()
#     elements = []

#     elements.append(Paragraph("Main Summary", styles['Heading1']))
#     elements.append(Spacer(1, 12))
#     elements.append(Paragraph(summary, styles['BodyText']))

#     doc.build(elements)

# # 🗂 Main function to process all PDFs in the directory
# def main():
#     input_dir = "C:/Users/byred/Downloads/FILES" # Replace with your PDF directory path
#     output_pdf = os.path.join(input_dir, "C:/Users/byred/Downloads/combined_summary.pdf")

#     # 🗂 Find all PDFs in the directory
#     pdf_files = [f for f in os.listdir(input_dir) if f.endswith('.pdf')]
#     if not pdf_files:
#         print("No PDF files found in the directory.")
#         return

#     combined_summary = ""
#     for pdf_file in pdf_files:
#         file_path = os.path.join(input_dir, pdf_file)
#         print(f"Processing {pdf_file}...")
#         pdf_content = read_pdf(file_path)
#         if pdf_content:
#             summary = summarize_text(pdf_content)
#             combined_summary += f"Summary for {pdf_file}:\n{summary}\n\n"

#     # 📝 Save the combined summary as a PDF
#     if combined_summary:
#         save_summary_as_pdf(combined_summary, output_pdf)
#         print(f"Combined summary saved to {output_pdf}")
#     else:
#         print("No content to summarize.")

# # 🚀 Run the script
# main()






import os
from PyPDF2 import PdfReader
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, ListItem, ListFlowable
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from google import genai

# 🔑 Read API Key from Environment Variable
api_key = 'AkhilIzaSyCZhmMhR9jZglN8UZ0eZmzzv7IzpHrrFmc'
if not api_key:
    raise ValueError("Google GenAI API key not found. Please set the GENAI_API_KEY environment variable.")
client = genai.Client(api_key=api_key)

# 📄 Read PDF content
def read_pdf(file_path):
    try:
        pdf_reader = PdfReader(file_path)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return ""

# 🤖 Use GenAI to summarize content
def summarize_text(text):
    try:
        prompt = f"Summarize the following text concisely as bullet points:\n{text}"
        response = client.models.generate_content(model="gemini-2.0-flash", contents=prompt)
        return response.text
    except Exception as e:
        print(f"Error summarizing text: {e}")
        return "Summary unavailable due to an error."

# 📄 Save summary as a PDF with better formatting
def save_summary_as_pdf(summaries, output_file):
    doc = SimpleDocTemplate(output_file, pagesize=A4)
    styles = getSampleStyleSheet()
    elements = []

    # Main Title
    elements.append(Paragraph("Main Summary", styles['Title']))
    elements.append(Spacer(1, 12))

    # Adding each summary with a new page for each
    for i, (pdf_file, summary) in enumerate(summaries, 1):
        elements.append(Paragraph(f"Summary for {pdf_file}", styles['Heading1']))
        elements.append(Spacer(1, 6))
        
        # Convert summary to bullet points
        bullet_points = summary.split('\n')
        formatted_list = ListFlowable(
            [ListItem(Paragraph(point.strip(), styles['BodyText'])) for point in bullet_points if point.strip()],
            bulletType='bullet'
        )
        elements.append(formatted_list)
        if i < len(summaries):
            elements.append(PageBreak())  # Start a new page for each PDF summary

    doc.build(elements)

# 🗂 Main function to process all PDFs in the directory
def main():
    input_dir = "C:/Users/byred/Downloads/FILES" # Replace with your PDF directory path
    output_pdf = os.path.join(input_dir, "C:/Users/byred/Downloads/combined_summary.pdf")

    # 🗂 Find all PDFs in the directory
    pdf_files = [f for f in os.listdir(input_dir) if f.endswith('.pdf')]
    if not pdf_files:
        print("No PDF files found in the directory.")
        return

    summaries = []
    for pdf_file in pdf_files:
        file_path = os.path.join(input_dir, pdf_file)
        print(f"Processing {pdf_file}...")
        pdf_content = read_pdf(file_path)
        if pdf_content:
            summary = summarize_text(pdf_content)
            summaries.append((pdf_file, summary))

    # 📝 Save the combined summary as a PDF
    if summaries:
        save_summary_as_pdf(summaries, output_pdf)
        print(f"Combined summary saved to {output_pdf}")
    else:
        print("No content to summarize.")

# 🚀 Run the script
main()


