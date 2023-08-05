# Python Script for Corpus Configuration (corpus.csv)

Python version of devosl99's bash script corpusPopulator

This Python script creates a corpus configuration file, `corpus.csv`, for use with the Java Graphical Authorship Attribution Program (JGAAP) available at https://github.com/evllabs/JGAAP. This script is intended as a Python alternative to the bash script `corpusPopulator` available at https://github.com/devosl99/corpusPopulator.

## Description

The script works by scanning through a given directory (`corpus_dir`), which is expected to contain one sub-directory per author. Each sub-directory should contain one or more text files. The name of each sub-directory is used to derive the author's name. The script creates a CSV file (`corpus.csv`) with three columns: 'Author', 'Path to Text File', and 'FileName by Author'.

For each text file in the corpus directory, the script writes a row to the CSV file containing the author's name, the path to the text file, and a string in the format "{file_name} by {last_name}, {first_initial}".

## Usage

1. Set the `corpus_dir` variable to the path of the directory containing your corpus. This should be a directory containing one sub-directory per author, with each sub-directory containing one or more `.txt` files.
2. Set the `output_file` variable to the desired path of the output CSV file.
3. Run the script with the command `python3 script_name.py`, where `script_name.py` is the name of the file containing the script.

## Example

If your `corpus_dir` is set to 'assignment/enron_demo' and it contains a sub-directory 'allen-p' with a text file '0.txt', the script will write a row to the CSV file with 'allen-p' as the Author, 'assignment/enron_demo/allen-p/0.txt' as the Path to Text File, and '0.txt by Allen, P' as the FileName by Author.

## Requirements

- Python 3.6 or later
- Read access to the corpus directory and write access to the directory where `corpus.csv` will be stored

## Note

The script assumes that the author's name is always in the format "lastname-firstinitial", and it can handle hyphenated last names correctly. If the author's name format in your corpus is different, you may need to modify the script accordingly.

## Limitations

This script does not perform any error checking on the contents of the text files or the formatting of the author's names. It is assumed that the corpus is well-formed and follows the expected structure.
