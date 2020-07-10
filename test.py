from markdown import markdown
import pdfkit
input_filename = 'FDA_Submission.md'
output_filename = 'FDA_Submission.pdf'

with open(input_filename, 'r') as f:
    html_text = markdown(f.read(), output_format='html4')

pdfkit.from_string(html_text, output_filename)
