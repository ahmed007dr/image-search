import os
import openpyxl
from bing_image_downloader import downloader
import time

def create_output_directory(output_directory):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

def load_excel_sheet(excel_file):
    # Load Excel file
    return openpyxl.load_workbook(excel_file).active

def search_and_download_images(sheet, output_directory):
    # Loop through each row in the first column of the Excel sheet
    for row in sheet.iter_rows(min_row=1, max_col=1, max_row=sheet.max_row, values_only=True):
        name = row[0]
        if name:
            print(f"Searching for images of '{name}'...")
            # Search for images on Bing Images
            downloader.download(name, limit=1, output_dir=output_directory, adult_filter_off=True, force_replace=False, timeout=60)
            print(f"Downloaded image for '{name}'")
            
            # Introduce a delay between each image download request
            time.sleep(1)  # Adjust the delay time as needed

if __name__ == "__main__":
    # Specify the path to your Excel file
    excel_file = "F:/django-5/image/src/Drug.xlsx"
    
    # Specify the output directory for downloaded images
    output_directory = "F:/django-5/image/src/output_directory"

    create_output_directory(output_directory)
    sheet = load_excel_sheet(excel_file)
    search_and_download_images(sheet, output_directory)
