import string

def preprocess_text(text):
    """
    Cleans the text by converting it to lowercase and removing punctuation,
    then splits it into a list of words.
    """
    text = text.lower()
    # Remove punctuation using string.punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text.split()

def read_essay(file_path):
    """
    Reads an essay file, handles potential errors, and returns a list of words.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            return preprocess_text(content)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except Exception as e:
        print(f"An error occurred while reading {file_path}: {e}")
        return None

def get_word_frequencies(word_list):
    """
    Creates a dictionary containing the frequency of each word.
    """
    freq_dict = {}
    for word in word_list:
        freq_dict[word] = freq_dict.get(word, 0) + 1
    return freq_dict

def search_word(word, freq1, freq2):
    """
    Searches for a specific word in both essays.
    Returns True if found in both, False otherwise.
    Also prints the individual counts.
    """
    word = word.lower().strip()
    count1 = freq1.get(word, 0)
    count2 = freq2.get(word, 0)
    
    print(f"\nResults for '{word}':")
    print(f"  - Appears in Essay 1: {count1} time(s)")
    print(f"  - Appears in Essay 2: {count2} time(s)")
    
    # Per instructions: Return False if not found in either or just one of them
    if count1 > 0 and count2 > 0:
        return True
    return False

def calculate_plagiarism(words1, words2):
    """
    Calculates plagiarism percentage using set intersections and unions.
    """
    set1 = set(words1)
    set2 = set(words2)
    
    # Set operations
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    
    if not union:
        return 0.0, intersection, union
        
    # Formula: (Intersection / Union) * 100
    percentage = (len(intersection) / len(union)) * 100
    return percentage, intersection, union

def main():
    print("=== Plagiarism Detector Application ===")
    
    # 1. Compare Two Essays (File names from prompt)
    essay1_path = "essay1.txt"
    essay2_path = "essay2.txt"
    
    words1 = read_essay(essay1_path)
    words2 = read_essay(essay2_path)
    
    # Validation check
    if words1 is None or words2 is None:
        print("Please ensure both 'essay1.txt' and 'essay2.txt' exist in the same folder.")
        return

    # Generate frequency dictionaries for counting
    freq1 = get_word_frequencies(words1)
    freq2 = get_word_frequencies(words2)

    # 2. Calculate Plagiarism Percentage and Decision
    percentage, intersection, union = calculate_plagiarism(words1, words2)
    
    print("\n--- Analysis Report ---")
    print(f"Total unique words across both essays (Union): {len(union)}")
    print(f"Common unique words (Intersection): {len(intersection)}")
    print(f"Calculated Plagiarism Percentage: {percentage:.2f}%")
    
    # Plagiarism Decision Threshold (50%)
    if percentage >= 50.0:
        print("Decision: PLAGIARISM DETECTED (50% or higher threshold met).")
    else:
        print("Decision: NO PLAGIARISM DETECTED (Below 50% threshold).")

    # 3. Find and Display Common Words with Frequencies
    print("\n--- Common Words Breakdown ---")
    if not intersection:
        print("No common words found.")
    else:
        for word in sorted(intersection):
            print(f"• '{word}': {freq1[word]} time(s) in Essay 1 | {freq2[word]} time(s) in Essay 2")

    # 4. Search for a Specific Word
    print("\n--- Interactive Word Search ---")
    while True:
        user_word = input("Enter a word to search (or press Enter to exit): ").strip()
        if not user_word:
            break
        
        found = search_word(user_word, freq1, freq2)
        print(f"Function returned: {found}")

if __name__ == "__main__":
    main()