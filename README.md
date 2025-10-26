# qrcode_for_weblinks
Generate your own QR code image for any weblink

## Description
This project provides a simple Python script to generate QR code images for web links. The generated QR codes can be scanned with any QR code reader to quickly access the encoded URL.

## Features
- Generate QR codes for any web link
- Customizable output filename
- Command-line interface
- URL validation
- High-quality PNG output

## Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/kajin88/qrcode_for_weblinks.git
cd qrcode_for_weblinks
```

2. Create and activate a virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage
Generate a QR code with the default filename (`qrcode.png`):
```bash
python generate_qrcode.py https://www.example.com
```

### Custom Filename
Generate a QR code with a custom filename:
```bash
python generate_qrcode.py https://www.example.com my_custom_qrcode.png
```

### Using as a Module
You can also import and use the function in your own Python code:
```python
from generate_qrcode import generate_qrcode

# Generate QR code
output_path = generate_qrcode("https://www.example.com", "output.png")
print(f"QR code saved to: {output_path}")
```

## Examples

Generate a QR code for GitHub:
```bash
python generate_qrcode.py https://github.com github_qr.png
```

Generate a QR code for Google:
```bash
python generate_qrcode.py https://www.google.com google_qr.png
```

## Dependencies
- `qrcode[pil]` - QR code generation library with PIL support for image creation

See `requirements.txt` for the complete list of dependencies.

## Output
The script generates a PNG image file containing the QR code. The default settings create:
- Black QR code on white background
- Border of 4 boxes around the QR code
- Box size of 10 pixels

## License
This project is open source and available under the MIT License.

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## Author
kajin88
