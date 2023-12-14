import PyPDF2
import tabula
import sys
# Open the PDF file
pdf_file = open(sys.argv[1], 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Extract all tables from the PDF
tables = tabula.read_pdf(pdf_file, pages='all')

# Iterate over the tables and extract the data
table_data = []
for table in tables:
	# Get the table data as a list of lists
	table_data.append(table.values)

# Print the table data
print(table_data)

# Close the PDF file
pdf_file.close()
