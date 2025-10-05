import fitz  # PyMuPDF

# Empty keywords list - add your keywords here
keywords = []

def extract_lines_with_keywords(pdf_path, keywords):
    """
    Extract full lines of text from a PDF when any keyword is found.
    
    Args:
        pdf_path: Path to the PDF file
        keywords: List of keywords to search for
        
    Returns:
        List of tuples containing (page_number, line_text)
    """
    results = []
    
    # Open the PDF
    doc = fitz.open(pdf_path)
    
    # Iterate through each page
    for page_num in range(len(doc)):
        page = doc[page_num]
        
        # Extract text from the page
        text = page.get_text()
        
        # Split into lines
        lines = text.split('\n')
        
        # Check each line for keywords
        for line in lines:
            # Check if any keyword is in the line (case-insensitive)
            for keyword in keywords:
                if keyword.lower() in line.lower():
                    results.append((page_num + 1, line.strip()))
                    break  # Avoid duplicate entries if multiple keywords match
    
    doc.close()
    return results


# Example usage:
if __name__ == "__main__":
    # Add keywords to search for
    keywords = ["assignment", "exam", "test", "project",
                 "disscusion", "final", "midterm"]  # Modify this list
    
    # Specify PDF path
    pdf_file = "TestSyllabus1.pdf"  # Change to your PDF path
    
    try:
        # Extract lines containing keywords
        matched_lines = extract_lines_with_keywords(pdf_file, keywords)
        
        # Display results
        if matched_lines:
            print(f"Found {len(matched_lines)} matching lines:\n")
            for page_num, line in matched_lines:
                print(f"Page {page_num}: {line}")
        else:
            print("No matching lines found.")
            
    except FileNotFoundError:
        print(f"Error: PDF file '{pdf_file}' not found.")
    except Exception as e:
        print(f"Error: {e}")
