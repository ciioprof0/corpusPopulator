import os
import csv

def create_corpus_config(corpus_dir, output_file):
    """
    Creates a corpus configuration CSV file for the Java Graphical Authorship Attribution Program (JGAAP).
    
    The CSV file will have three columns: 'Author', 'Path to Text File', and 'FileName by Author'.
    For each text file in the corpus directory, this function will write a row to the CSV file containing
    the author's name (derived from the directory name), the path to the text file, and a string in the format
    "{file_name} by {last_name}, {first_initial}".

    Args:
        corpus_dir (str): The path to the directory containing the corpus. This should be a directory
                          containing one sub-directory per author, with each sub-directory containing one
                          or more text files.
        output_file (str): The path to the CSV file to be created.

    Returns:
        None
    """
    # get all directories from the main directory
    author_dirs = [d for d in os.listdir(corpus_dir) if os.path.isdir(os.path.join(corpus_dir, d))]

    # open the output file in write mode
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        # write the header
        writer.writerow(['Author', 'Path to Text File', 'FileName by Author'])
        
        # iterate over the author directories
        for author_dir in author_dirs:
            # derive the author name from the directory name (e.g., allen-p or mimis-thurstan-p)
            author = author_dir
            
            # get all text files for this author
            text_files = [f for f in os.listdir(os.path.join(corpus_dir, author_dir)) if f.endswith('.txt')]
            
            # iterate over the text files
            for text_file in text_files:
                # get the full path of the file
                filepath = os.path.join(corpus_dir, author_dir, text_file)
                
                # construct the third column content
                split_author = author.split("-")
                last_name = "-".join(split_author[:-1]).title()  # Handle hyphenated last names
                first_initial = split_author[-1].upper()
                file_name_by_author = f"{text_file} by {last_name}, {first_initial}"
                
                # write the author, filepath and the third column content to the CSV file
                writer.writerow([author, filepath, file_name_by_author])

# directory containing the text files
corpus_dir = '/path/to/your/corpus/directory'

# output CSV file
output_file = 'corpus.csv'

create_corpus_config(corpus_dir, output_file)
