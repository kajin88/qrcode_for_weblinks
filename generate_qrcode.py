"""
QR Code Generator for Web Links
This script generates a QR code image for a given web link.
"""

import qrcode
import sys
from pathlib import Path


def generate_qrcode(url: str, output_filename: str = "qrcode.png"):
    """
    Generate a QR code for the given URL and save it as an image.
    
    Args:
        url (str): The web link to encode in the QR code
        output_filename (str): The filename for the output image (default: qrcode.png)
    
    Returns:
        str: Path to the generated QR code image
    """
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR code
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,  # Size of each box in pixels
        border=4,  # Border size in boxes
    )
    
    # Add data to the QR code
    qr.add_data(url)
    qr.make(fit=True)
    
    # Create an image from the QR code
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save the image
    img.save(output_filename)
    
    return output_filename


def main():
    """Main function to handle command-line usage."""
    if len(sys.argv) < 2:
        print("Usage: python generate_qrcode.py <URL> [output_filename]")
        print("\nExample:")
        print("  python generate_qrcode.py https://www.example.com")
        print("  python generate_qrcode.py https://www.example.com my_qrcode.png")
        sys.exit(1)
    
    url = sys.argv[1]
    output_filename = sys.argv[2] if len(sys.argv) > 2 else "qrcode.png"
    
    # Validate URL format (basic check)
    if not (url.startswith('http://') or url.startswith('https://')):
        print("Warning: URL should start with 'http://' or 'https://'")
        response = input("Continue anyway? (y/n): ")
        if response.lower() != 'y':
            sys.exit(0)
    
    # Generate QR code
    try:
        output_path = generate_qrcode(url, output_filename)
        print(f"✓ QR code successfully generated: {output_path}")
        print(f"  URL: {url}")
    except Exception as e:
        print(f"✗ Error generating QR code: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
