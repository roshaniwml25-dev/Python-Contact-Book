# Python Contact Book

A menu-driven contact manager written in Python for the *Python Programming Language (N-PCCCM304P)* Experiential Learning project.
Contacts are stored permanently in `contacts.json`.

## Features
- Add, view, search (by name or phone), edit and delete contacts
- Permanent storage using JSON file handling
- Input validation (10-digit phone, email format, no duplicate names)
- Exception handling for a missing/corrupt file, invalid menu input and Ctrl+C

## Run
```bash
python contact_book.py
```

## Sample session
```
===== CONTACT BOOK =====
1. Add Contact
2. View All Contacts
3. Search Contact
4. Edit Contact
5. Delete Contact
6. Exit
Enter your choice (1-6): 1
Name  : Roshani Wankhede
Phone : 9876543210
Email (optional): roshani@gmail.com
Contact added successfully.
```

## Tests
```bash
python -m unittest -v
```
11 unit tests cover add, duplicate/invalid input, search, edit, delete, save/load and corrupt-file handling.

## Files
| File | Purpose |
|---|---|
| `contact_book.py` | Main program |
| `test_contact_book.py` | Unit tests |
| `.gitignore` | Keeps personal `contacts.json` out of the repository |

## Author
Roshani B. Wankhede (CM25047), CSE (AI&ML), S. B. Jain Institute of Technology Management and Research, Nagpur
Guide: Mrs. Mayuri Getme
