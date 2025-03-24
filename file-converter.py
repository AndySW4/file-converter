import sys
import markdown


def convert_markdown_to_html(input_file, output_file):

    try:
        with open(input_file, 'r') as mdfile:
            mdcontent = mdfile.read()
        
        htmlcontent = markdown.markdown(mdcontent)

        with open(output_file, 'w') as htmlfile:
            htmlfile.write(htmlcontent)

        print('Success')
    
    except FileNotFoundError:
        print('File not found')
    except Exception as e:
        print(f'{e}')

if __name__ == '__main__':

    if len(sys.argv) != 4 or sys.argv[1] != "markdown":
        print("Usage: python3 file-converter.py markdown inputfile.md outputfile.html")
        sys.exit(1)

    input_path = sys.argv[2]
    output_path = sys.argv[3]

    convert_markdown_to_html(input_path, output_path)