# MLTZIP - Milos' Loosy Text Compression

MLTZIP is an experimental text compression tool developed collaboratively by Milos and ChatGPT from OpenAI. The tool aims to improve compression ratios by combining character-based transformations with traditional compression algorithms.

## Idea

The primary concept behind MLTZIP revolves around the transformation of text before its compression. By replacing certain characters or groups of characters in the text with a single character, the entropy of the text is reduced. This transformation makes the text more amenable to further compression using traditional algorithms like gzip, bzip2, or xz.

Once the text undergoes this transformation, it's further compressed using a traditional algorithm. Decompression involves two steps: First, the file is decompressed using the standard tool. Then, a language model or algorithm reverses the character-based transformations to restore the text to its original form (or as close to it as possible).

## Experimental Results

For our tests, we used the text "A Tale of Two Cities" by Charles Dickens, sourced from [Project Gutenberg](https://www.gutenberg.org/files/98/98-0.txt). The original file was processed using the `dos2unix` command to standardize line endings, resulting in a file size of 790,943 bytes.

The MLTZIP method demonstrated promising improvements in compression ratios:

- **bzip2**: Direct compression using bzip2 achieved a file size of 220,386 bytes. When pre-processed with MLTZIP and then compressed using bzip2, the file size was reduced to 211,232 bytes, marking an improvement of approximately 4.15%.  
- **gzip**: Direct compression using gzip yielded a file size of 299,085 bytes. With MLTZIP pre-processing followed by gzip compression, the size was 271,808 bytes, showing an improvement of roughly 9.12%.
- **xz**: Direct xz compression resulted in a file size of 247,324 bytes. After MLTZIP pre-processing and xz compression, the size came down to 229,236 bytes, an improvement of about 7.31%.

## Usage Instructions

To use MLTZIP for text compression, follow the steps below:

1. Clone the repository:
```
```git clone <repository_link>
cd mltzip```
```

2. Run the MLTZIP tool:
`python mltzip.py -i <input_file> -g <replacement_rule> [-c <compression_algorithm> -l <language> -d -p <compression_params>]`

Arguments:
- `-i, --input`: Input file for compression.
- `-g, --group`: Replacement rule in the format `<replacing character>:<replaced character 1>,<replaced character 2>,...`.
- `-c, --compression`: Compression algorithm to use (choices: gzip, bzip2, xz; default: bzip2).
- `-l, --language`: Language of the text (default: English).
- `-d, --debug`: Debug mode; retains the .mlt file.
- `-p, --params`: Parameters to pass to the compression tool.

3. The compressed file will be created in the same directory.

## Potential Improvements and Ideas

- **Iterative Testing**: Continuously test with various texts to refine the character replacement rules for optimal compression without losing too much information.
- **Expand Support**: Consider adding support for other languages or specialized texts.
- **Advanced Decompression**: Use more advanced language models or algorithms for the decompression step to improve accuracy.

## Contribution

Contributions to the project are welcome! Whether it's improving the compression logic, adding support for more languages, or fixing bugs, your contributions will be highly appreciated.

1. Fork the repository.
2. Create a new branch for your changes.
3. Make the necessary changes in your branch.
4. Push your changes and create a pull request.

## License

MLTZIP is released under "The Unlicense", which means it is free and unencumbered software released into the public domain. You can use, modify, distribute, and include the work in your own projects without any restrictions.

For the full license text and details, see the `LICENSE` file in the repository or visit [The Unlicense website](https://unlicense.org/).
