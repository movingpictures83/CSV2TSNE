# CSV2TSNE
# Language: Python
# Input: TXT
# Output: PREFIX
# Tested with: PluMA 1.1, Python 3.6

Convert a CSV file of abundances to TSV format

The plugin accepts as input a tab-delimited file of
keyword-value pairs:

csvfile: CSV file where rows correspond to sample and columns taxa; entry (i, j) is the abundance of taxa j in sample i
metafile: Metadata file with Samples and Groups; sample names must match names in CSV

TSNE files will be output, each with the user-specified prefix

