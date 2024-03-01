import os
import sys
from PyPDF2 import PdfReader
import django

# Add the directory containing your Django project to the path
project_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_directory)
os.environ['DJANGO_SETTINGS_MODULE'] = 'accommodation_search.settings'

# Configure Django
django.setup()

# Now import the Django models
from accommodations.models import Accommodation

def extract_residences_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PdfReader(file)

        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()

            # Extract data and create Residence objects
            residence_data = parse_residence_data(text)
            
            if residence_data:
                Accommodation.objects.create(**residence_data)

def parse_residence_data(text):
    # Implement your parsing logic based on the actual structure of the PDF text
    # Example parsing logic:
    residence_data = {
        'name': extract_value(text, 'Residence name'),
        'address': extract_value(text, 'Street Address'),
        'contact_details': extract_value(text, 'Cell Number'),
        'number_of_beds': int(extract_value(text, 'Number of Beds', default='0')),
        # Add other fields based on your PDF columns
    }

    return residence_data

def extract_value(text, field_name, default=''):
    # Helper function to extract the value associated with a field name
    start_index = text.find(field_name)
    if start_index != -1:
        start_index += len(field_name)
        end_index = text.find('\n', start_index)
        value = text[start_index:end_index].strip()
        return value
    else:
        return default

if __name__ == "__main__":
    pdf_path = 'Public-List-of-Accreditation_8.xlsx'  # Assuming the PDF is in the same directory
    extract_residences_from_pdf(pdf_path)
