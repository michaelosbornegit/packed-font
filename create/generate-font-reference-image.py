import os
import sys
import math
from PIL import Image, ImageDraw, ImageFont

def load_font(font_size):
    # Try to load a font that supports a wide range of Unicode characters
    font_paths = [
        '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',  # Linux
        '/usr/share/fonts/truetype/freefont/FreeSans.ttf',  # Linux
        '/Library/Fonts/Arial Unicode.ttf',  # macOS
        '/System/Library/Fonts/Supplemental/Arial Unicode.ttf',  # macOS
        'C:\\Windows\\Fonts\\arial.ttf',  # Windows
        'C:\\Windows\\Fonts\\arialuni.ttf',  # Windows
        'C:\\Windows\\Fonts\\DejaVuSans.ttf',  # Windows
    ]
    for font_path in font_paths:
        if os.path.exists(font_path):
            try:
                font = ImageFont.truetype(font_path, font_size)
                font.path = font_path  # Store path for later use
                return font
            except Exception:
                continue
    # Use default font if none found
    font = ImageFont.load_default()
    font.path = None  # Default font has no path
    return font

def get_codepoint_from_filename(filename):
    # Extract codepoint from filename like 'U225.bmp' (decimal)
    name, ext = os.path.splitext(filename)
    if name.startswith('U'):
        code_str = name[1:]
        try:
            code = int(code_str, 10)  # Parse as decimal
            return code
        except ValueError:
            pass
    return None

def codepoint_to_pystring_repr(codepoint):
    # Returns a string representation suitable for a Python string
    if codepoint <= 0xFF:
        return '\\x{:02x}'.format(codepoint)
    elif codepoint <= 0xFFFF:
        return '\\u{:04x}'.format(codepoint)
    else:
        return '\\U{:08x}'.format(codepoint)

def create_text_image(text, height, font):
    # Create an image to draw the text
    # Adjust font size to match the desired height
    font_size = height
    if font.path is None:
        # If default font, we cannot adjust size, use existing font
        temp_font = font
    else:
        while font_size > 0:
            try:
                temp_font = ImageFont.truetype(font.path, font_size)
            except Exception:
                font_size -= 1
                continue
            # Get the size of the text
            bbox = temp_font.getbbox(text)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            if text_height <= height:
                break
            font_size -= 1
        else:
            raise ValueError("Could not fit text into the given height.")
    # Get text size
    bbox = temp_font.getbbox(text)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    # Create an image large enough to hold the text
    image = Image.new('RGBA', (text_width, height), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)
    # Calculate vertical position to center the text
    y = (height - text_height) // 2 - bbox[1]
    # Draw the text onto the image
    draw.text((-bbox[0], y), text, font=temp_font, fill='black')
    return image

def create_title_image(text, width, font):
    # Adjust font size to fit the text into the width
    max_font_size = 64
    font_size = max_font_size
    if font.path is None:
        temp_font = font
    else:
        while font_size > 0:
            try:
                temp_font = ImageFont.truetype(font.path, font_size)
            except Exception:
                font_size -= 1
                continue
            bbox = temp_font.getbbox(text)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            if text_width <= width:
                break
            font_size -= 1
        else:
            raise ValueError("Could not fit title text into the given width.")
    bbox = temp_font.getbbox(text)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    # Create an image with desired width and calculated height
    image = Image.new('RGBA', (width, text_height), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)
    # Center the text horizontally
    x = (width - text_width) // 2 - bbox[0]
    y = -bbox[1]
    draw.text((x, y), text, font=temp_font, fill='black')
    return image

def main(folder_path, title=None):
    # Load font
    font_size = 64  # Initial font size
    font = load_font(font_size)
    if not font:
        print("Could not load a font. Please install a font that supports Unicode characters.")
        sys.exit(1)

    # Get list of .bmp files in the folder
    files = os.listdir(folder_path)
    bmp_files = [f for f in files if f.lower().endswith('.bmp') and f.startswith('U')]
    combined_images = []

    for filename in sorted(bmp_files):
        code = get_codepoint_from_filename(filename)
        if code is None:
            continue
        # Generate Python string representation of the codepoint
        text_representation = codepoint_to_pystring_repr(code)

        bmp_path = os.path.join(folder_path, filename)
        try:
            bmp_image = Image.open(bmp_path).convert('RGBA')
        except Exception as e:
            print(f"Error opening image {bmp_path}: {e}")
            continue

        # Create text image
        height = bmp_image.height
        try:
            text_image = create_text_image(text_representation, height, font)
        except Exception as e:
            print(f"Error creating text image for codepoint {code}: {e}")
            continue

        # Create a new image with the text image and bmp image side by side
        total_width = text_image.width + bmp_image.width
        combined_image = Image.new('RGBA', (total_width, height), (255, 255, 255, 0))
        combined_image.paste(text_image, (0, 0))
        combined_image.paste(bmp_image, (text_image.width, 0))

        combined_images.append(combined_image)

    # Determine the layout for multiple columns
    if not combined_images:
        print("No images to combine.")
        sys.exit(1)

    num_columns = 6  # Adjust the number of columns here
    total_images = len(combined_images)
    num_rows = math.ceil(total_images / num_columns)

    # Arrange images into a grid
    grid_images = []
    for row in range(num_rows):
        row_images = []
        for col in range(num_columns):
            index = row * num_columns + col
            if index < len(combined_images):
                row_images.append(combined_images[index])
            else:
                row_images.append(None)
        grid_images.append(row_images)

    # Calculate column widths and row heights
    column_widths = [0] * num_columns
    row_heights = [0] * num_rows

    for row_idx, row_images in enumerate(grid_images):
        for col_idx, img in enumerate(row_images):
            if img is not None:
                w, h = img.size
                column_widths[col_idx] = max(column_widths[col_idx], w)
                row_heights[row_idx] = max(row_heights[row_idx], h)

    # Create the output image
    total_width = sum(column_widths)
    total_height = sum(row_heights)
    output_image = Image.new('RGBA', (total_width, total_height), (255, 255, 255, 0))

    # Paste images into the output image
    y_offset = 0
    for row_idx, row_images in enumerate(grid_images):
        x_offset = 0
        row_height = row_heights[row_idx]
        for col_idx, img in enumerate(row_images):
            col_width = column_widths[col_idx]
            if img is not None:
                img_w, img_h = img.size
                # Center the image horizontally within the column
                x_img = x_offset + (col_width - img_w) // 2
                # Center the image vertically within the row
                y_img = y_offset + (row_height - img_h) // 2
                output_image.paste(img, (x_img, y_img))
            x_offset += col_width
        y_offset += row_height

    # Add title at the top if provided
    if title:
        try:
            title_image = create_title_image(title, output_image.width, font)
            # Combine title image and output image
            total_height = title_image.height + output_image.height
            combined_image = Image.new('RGBA', (output_image.width, total_height), (255, 255, 255, 0))
            combined_image.paste(title_image, (0, 0))
            combined_image.paste(output_image, (0, title_image.height))
            output_image = combined_image
        except Exception as e:
            print(f"Error creating title image: {e}")
            # Proceed without title

    # Save the output image
    if title:
        # Remove any illegal characters from title for filename
        import string
        valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
        sanitized_title = ''.join(c for c in title if c in valid_chars)
        output_filename = f"{sanitized_title}.png"
    else:
        output_filename = 'output.png'
    output_path = os.path.join(folder_path, output_filename)
    output_image.convert('RGB').save(output_path)
    print(f"Output image saved as {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <folder_path> [title]")
        sys.exit(1)
    folder_path = sys.argv[1]
    title = sys.argv[2] if len(sys.argv) > 2 else None
    main(folder_path, title)
