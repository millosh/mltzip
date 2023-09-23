import os
import argparse
import subprocess

def transform_text(text, groups):
    """Transform the text based on the provided groups."""
    for group in groups:
        replace_char, chars = group.split(":")
        for char in chars.split(","):
            text = text.replace(char, replace_char)
            text = text.replace(char.upper(), replace_char.upper())  # Also replace the uppercase version of the character
    return text

def main():
    parser = argparse.ArgumentParser(description="Milos' Loosy Text Compression Tool")
    parser.add_argument('-i', '--input', type=str, required=True, help='Name of the file containing text to be compressed.')
    parser.add_argument('-g', '--group', action='append', help='Replacement group in format: <replacing character>:<replaced character 1>,<replaced character 2>,...')
    parser.add_argument('-l', '--language', type=str, default='English', help='Language of the text.')
    parser.add_argument('-c', '--compression', type=str, default='bzip2', choices=['gzip', 'bzip2', 'xz'], help='Compression algorithm to use.')
    parser.add_argument('-d', '--debug', action='store_true', help='Debug mode; retains the .mlt file.')
    parser.add_argument('-p', '--params', type=str, help='Parameters to pass to the compression tool.')

    args = parser.parse_args()

    with open(args.input, 'r') as f:
        input_text = f.read()

    transformed = transform_text(input_text, args.group)

    # Header Information
    header = f"Language: {args.language}\nReplacements: {', '.join(args.group)}\nVersion: 1.0\n\n"
    transformed = header + transformed

    # Write the transformed text to .mlt file
    mlt_filename = args.input + ".mlt"
    with open(mlt_filename, 'w') as f:
        f.write(transformed)

    # Compress the .mlt file
    compression_cmd = [args.compression, mlt_filename]
    if args.params:
        compression_cmd.extend(args.params.split(' '))
    subprocess.run(compression_cmd)

    # Remove .mlt file in non-debug mode
    if not args.debug and os.path.exists(mlt_filename):
        os.remove(mlt_filename)

    print(f"File compressed using {args.compression}.")

if __name__ == "__main__":
    main()
