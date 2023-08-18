# MIT License

# Copyright (c) [2023] [David Lapetina]

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import csv
import argparse

def replace_variables(svg_content, variable_data):
    for key, value in variable_data.items():
        placeholder = "@@" + key
        svg_content = svg_content.replace(placeholder, str(value))
    return svg_content

def main(svg_file_path, csv_file_path, output_svg_radix):
    file_data = {}
    line = 0
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            variable_data = {}
            for key, value in row.items():
                variable_data[key] = value
            file_data[line] = variable_data
            line += 1
    
    with open(svg_file_path, 'r') as svg_file:
        svg_content = svg_file.read()

    for key, values in file_data.items():
        replaced_svg_content = replace_variables(svg_content, values)
        output_svg_path = f'{output_svg_radix}{key}.svg'
        with open(output_svg_path, 'w') as output_svg_file:
            output_svg_file.write(replaced_svg_content)
    
        print(f"SVG file '{output_svg_path}' generated successfully!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate modified SVG files from CSV data.")
    parser.add_argument("svg_file", help="Path to input SVG file")
    parser.add_argument("csv_file", help="Path to CSV data file")
    parser.add_argument("output_radix", help="Radix for output SVG files")
    args = parser.parse_args()

    main(args.svg_file, args.csv_file, args.output_radix)
