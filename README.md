## Description ##
Directory Tree Generator is a command line application that creates and prints a Directory Tree for any directory passed.

## Options ##
* -d --dir-only Generates a directory-only tree
* -f --file-only Generates a file-only tree

## Files ##
* cli.py: Deals with the Command Line Interface and makes a call to GenerateTree
* rptree.py: Contains public class GenerateTree that uses a private class TreeGenerator which recursively adds sub-directories and files to the tree.
* tree.py: Entry-point script

