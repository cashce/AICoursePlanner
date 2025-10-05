import fitz  # PyMuPDF

# Empty keywords list - add your keywords here
keywords = []

def extract_table_rows_with_keywords(pdf_path, keywords):
    """
    Extract rows from tables in a PDF when any keyword is found in a cell.
    
    Args:
        pdf_path: Path to the PDF file
        keywords: List of keywords to search for
        
    Returns:
        List of tuples containing (page_number, table_index, row_data)
    """
    results = []
    
    # Open the PDF
    doc = fitz.open(pdf_path)
    
    # Iterate through each page
    for page_num in range(len(doc)):
        page = doc[page_num]
        
        # Find tables on the page
        tables = page.find_tables()
        
        if tables:
            for table_idx, table in enumerate(tables.tables):
                # Extract table data
                table_data = table.extract()
                
                # Check each row for keywords
                for row_idx, row in enumerate(table_data):
                    # Check if any cell in the row contains a keyword
                    row_matches = False
                    for cell in row:
                        if cell:  # Check if cell is not None or empty
                            cell_text = str(cell).lower()
                            for keyword in keywords:
                                if keyword.lower() in cell_text:
                                    row_matches = True
                                    break
                        if row_matches:
                            break
                    
                    # If keyword found, add the entire row
                    if row_matches:
                        results.append((
                            page_num + 1,
                            table_idx + 1,
                            row
                        ))
    
    doc.close()
    return results


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
    keywords = ["example", "important", "note"]  # Modify this list
    
    # Specify PDF path
    pdf_file = "your_document.pdf"  # Change to your PDF path
    
    try:
        print("=" * 60)
        print("EXTRACTING LINES WITH KEYWORDS")
        print("=" * 60)
        
        # Extract lines containing keywords
        matched_lines = extract_lines_with_keywords(pdf_file, keywords)
        
        # Display results
        if matched_lines:
            print(f"\nFound {len(matched_lines)} matching lines:\n")
            for page_num, line in matched_lines:
                print(f"Page {page_num}: {line}")
        else:
            print("No matching lines found.")
        
        print("\n" + "=" * 60)
        print("EXTRACTING TABLE ROWS WITH KEYWORDS")
        print("=" * 60)
        
        # Extract table rows containing keywords
        table_results = extract_table_rows_with_keywords(pdf_file, keywords)
        
        # Display table results
        if table_results:
            print(f"\nFound {len(table_results)} matching table rows:\n")
            for page_num, table_idx, row in table_results:
                print(f"Page {page_num}, Table {table_idx}:")
                print(f"  Row: {' | '.join([str(cell) if cell else '' for cell in row])}")
                print()
        else:
            print("\nNo matching table rows found.")
            
    except FileNotFoundError:
        print(f"Error: PDF file '{pdf_file}' not found.")
    except Exception as e:
        print(f"Error: {e}")
