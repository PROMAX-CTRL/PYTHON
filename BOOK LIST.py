import csv

filename = "books.csv"
books = [] # Stores book data

def validateAddBooks(title, author, description): #REFERENCE GPT 1
    try:
        with open(filename, 'r', newline='') as file:
            first = file.readline().strip()
    except:
        first = ""

    # Create file with header if it doesn't exist or is empty
    if first != "Title,Author,Description":
        print("No books found in this list. Creating a new list.")
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Title", "Author", "Description"])
            
    duplicate = 0
    try:
        with open(filename, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Title'].lower().strip() == title.lower().strip():
                    duplicate = 1 # Check for duplicate book titles
                    break
    except:
        print("No books found. Creating a new list.")

    if duplicate == 1:
        print("Book with this title already exists. Cannot add duplicate.\n")
        return
    
    # Add book to the CSV file
    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([title, author, description])
        print("Book added successfully!\n")

def addBook():
    while True:  # outer loop for adding books
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        description = input("Enter book description: ")

        if title == "" or author == "" or description == "":
            print("All fields must be filled in. Please try again.\n")  #REFERENCE GPT 2
            continue

        while True:  # confirmation loop
            confirm = input("Are you happy with this entry? (Y/N): ").lower()
            if confirm == 'y':
                validateAddBooks(title, author, description)
                break  
            if confirm == 'n':
                print("Please enter the details again.\n")
                break 
            print("Invalid input. Please enter 'Y' or 'N'.")

        if confirm != 'y':
            continue  # re enter book details

        while True:  # ask to add another book
            anotherBook = input("Do you want to add another book? (Y/N): ").lower()
            if anotherBook == 'y':
                break 
            if anotherBook == 'n':
                print("Thank you!")
                return  # exit addBook() entirely
            print("Invalid input. Please enter 'Y'es or 'N'o.")
            
def readBook():
    while True:
        try:
            with open(filename, 'r', newline='') as file:
                reader = csv.DictReader(file)
                books.clear() #reference
                validBookCount = 0
                for row in reader:
                    books.append(row)
                    validBookCount = validBookCount + 1
                if validBookCount > 0:
                    break # Break if books exist
        except:
            pass  # File doesn't exist, create it below

        print("No books found. Adding default books.")
        headerNames = ["Title", "Author", "Description"]
        with open(filename, "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headerNames)
            writer.writeheader()
            # Write default books
            writer.writerow({'Title': 'GERONIMO STILTON',
                             'Author': 'Elisabetta Dami',
                             'Description': 'Adventure stories for children'})
            writer.writerow({'Title': 'THE HIDDEN STAIRCASE',
                             'Author': 'NANCY DREW',
                             'Description': 'Classic mystery novel'})
            writer.writerow({'Title': 'OLIVER TWIST',
                             'Author': 'CHARLES DICKENS',
                             'Description': 'Classic Victorian novel'})
            
    # Display the books
    for book in books:
        print("Title: " + book["Title"])
        print("Author: " + book["Author"])
        print("Description: " + book["Description"])
        print()

def searchBook():
    title = input("Enter title to search: ").lower()
    try:
        with open(filename, "r", newline="") as file:
            reader = csv.DictReader(file)
            for book in reader:
                if book["Title"].lower() == title:
                    print("\nBook Found:")
                    print("Title:", book["Title"])
                    print("Author:", book["Author"])
                    print("Description:", book["Description"])
                    return # Exit if book found
        print("Book '" + title + "' not found in the file.")
    except:
        print("No book list file found. Cannot search for books.")

def deleteBook():
    while True:
        title = input("Enter the title of the book to delete: ").lower()
        booksToKeep = []
        found = 0

        try:
            with open(filename, 'r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row['Title'].strip().lower() == title:
                        found = 1 # Mark as found
                    else:
                        booksToKeep.append(row)# Keep non-matching books
        except:
            print("No book list file found. Nothing to delete.")
            return

        headerNames = ["Title", "Author", "Description"]
        with open(filename, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=headerNames)
            writer.writeheader()
            for book in booksToKeep:
                writer.writerow(book)# Write remaining books back to file

        if found == 1:
            print("Book titled '" + title + "' deleted successfully.")
        else:
            print("Book titled '" + title + "' not found.")

        while True:  # ask to delete another book
            anotherBook = input("\nDo you want to remove another book? (Y/N): ").lower()
            if anotherBook == 'y':
                break 
            if anotherBook == 'n':
                print("Thank you!")
                return  # exit deleteBook() entirely
            print("Invalid input. Please enter 'Y'es or 'N'o.")


print("Book List Tracker Menu:")
print("Type '1' to Add a Book")
print("Type '2' to View Current Books")
print("Type '3' to Search for a Book")
print("Type '4' to Delete a Book")
print("Type '5' to Exit")

while True:# Main menu loop
    choice = input("\nEnter your choice: ")
    if choice == '1':
        addBook()
    elif choice == '2':
        readBook()
    elif choice == '3':
        searchBook()
    elif choice == '4':
        deleteBook()
    elif choice == '5':
        print("Exiting Book Tracker. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
