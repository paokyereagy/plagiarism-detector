Plagiarism Detector Application

Project Overview
This Python application is designed to compare two text-based essays (essay1.txt and essay2.txt) to analyze their content and detect potential plagiarism .
The program processes raw text data, performs frequency calculations, provides an interactive keyword search, and utilizes mathematical set operations to determine an objective plagiarism percentage based on a 50% threshold

Core Features & Implementation Details

The program fulfills all core requirements of the coding lab assignment using structural programming workflows

1. File Handling & Robust Validation
Reading Files:The read_essay() function safely opens and extracts content from text files using Python's context managers (with open...)
Error Handling: Built-in validation blocks (try-except) actively check for errors such as missing files (FileNotFoundError), preventing the application from crashing and providing clear alerts to the user.

2. Advanced String Manipulation
To ensure fair mathematical comparisons, text strings must be cleaned before evaluation. The preprocess_text() function automates this workflow:
Converts all text to lowercase so that words like "The" and "the" match exactly.
Strips away all punctuation marks using Python's string.punctuation mapping table to prevent attached punctuation from corrupting individual word tokens.
Splits the clean block text into an iterable list of words.

3. Word Frequency Mapping (Data Structures)
The application builds tracking dictionaries (freq1 and freq2) using loops to map out word instance
For every word identified, it calculates its exact recurrence, allowing the program to display comprehensive breakdowns of common terms across both documents.

 4. Mathematical Plagiarism Decision (Set Operations)
 5. To formulate an explicit plagiarism score, the lists of words are converted into mathematical sets.
