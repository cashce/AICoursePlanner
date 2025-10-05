# Syllabize 📚

> Your AI-powered academic calendar assistant

Syllabize helps students stay organized by automatically extracting key dates (assignments, exams, readings) from course syllabi and populating their digital calendar with reminders and deadlines.

## 📁 Project Files

This project consists of two main components:

1. **NLP_AI_reader.py** - Python backend for PDF parsing and keyword extraction
2. **SyllabizePrototype2.dart** - Flutter mobile application frontend

---

## 🐍 Backend: NLP_AI_reader.py

### Overview
Python script that uses PyMuPDF to extract text and tables from PDF syllabus files, identifying key information through keyword matching.

### Features
- **Text Extraction**: Searches entire PDF for lines containing specified keywords
- **Table Detection**: Identifies tables within PDFs and extracts rows where keywords appear in any cell
- **Keyword Matching**: Case-insensitive keyword search across both regular text and table data
- **Structured Output**: Returns page numbers, line/row content, and table indices

### Installation

```bash
pip install PyMuPDF
```

### Usage

```python
# Define your keywords
keywords = ["assignment", "exam", "due date", "midterm", "quiz"]

# Specify PDF path
pdf_file = "syllabus.pdf"

# Extract lines with keywords
matched_lines = extract_lines_with_keywords(pdf_file, keywords)

# Extract table rows with keywords
table_results = extract_table_rows_with_keywords(pdf_file, keywords)
```

### Functions

#### `extract_lines_with_keywords(pdf_path, keywords)`
Extracts full text lines containing any of the specified keywords.

**Returns:** List of tuples `(page_number, line_text)`

#### `extract_table_rows_with_keywords(pdf_path, keywords)`
Detects tables and extracts entire rows when keywords are found in any cell.

**Returns:** List of tuples `(page_number, table_index, row_data)`

### Example Output

```
EXTRACTING LINES WITH KEYWORDS
==============================================================
Found 3 matching lines:

Page 2: Assignment 1 due October 15th
Page 3: Midterm exam scheduled for November 3rd
Page 5: Final project submission deadline: December 10th

EXTRACTING TABLE ROWS WITH KEYWORDS
==============================================================
Found 2 matching table rows:

Page 4, Table 1:
  Row: Week 5 | October 15 | Assignment 1 Due | 20% of grade

Page 4, Table 1:
  Row: Week 8 | November 3 | Midterm Exam | Chapters 1-5
```

---

## 📱 Frontend: SyllabizePrototype2.dart

### Overview
Flutter mobile application providing a user-friendly interface for syllabus upload, event review, and calendar synchronization.

### Features

#### Landing Page
- Welcome screen with app branding
- Feature highlights (Upload, AI Extraction, Calendar Sync)
- Get Started and Sign In buttons

#### Upload Screen
- Drag-and-drop syllabus upload interface
- Supports PDF, DOCX, and TXT formats
- File picker integration

#### Review Screen
- Display AI-extracted events (assignments, exams, readings)
- Color-coded event types:
  - 🔴 Exams (Red)
  - 🟠 Assignments (Orange)
  - 🟢 Readings (Green)
- Checkbox selection for events to sync
- Edit functionality for individual events
- "Sync All" button for calendar integration

#### Dashboard
- Upcoming deadlines with countdown
- Course overview with task counts
- Quick access to all activities

#### Settings
- Calendar integration options (Google, Outlook, Apple)
- Notification preferences
- Reminder customization
- Version and privacy information

### Installation

#### Prerequisites
- Flutter SDK (3.0+)
- Dart 3.0+
- Android Studio or Xcode

#### Setup

```bash
# Clone repository
git clone https://github.com/yourusername/syllabize.git
cd syllabize

# Install dependencies
flutter pub get

# Run the app
flutter run
```

### Screen Navigation

```
LandingPage
    ↓
HomeScreen (Bottom Navigation)
    ├── UploadScreen → ReviewScreen
    ├── DashboardScreen
    └── SettingsScreen
```

### UI Components

**Sample Event Data Structure:**
```dart
{
  'title': 'Essay 1: Critical Analysis',
  'date': DateTime(2025, 10, 15),
  'type': 'Assignment',
  'description': '5-7 pages on selected topic',
  'selected': true,
}
```

---

## 🔗 Integration Architecture

```
┌─────────────────────┐
│  Flutter App (UI)   │
│  SyllabizePrototype │
└──────────┬──────────┘
           │
           │ File Upload
           ↓
┌─────────────────────┐
│   Backend API       │
│   (To be built)     │
└──────────┬──────────┘
           │
           │ PDF Processing
           ↓
┌─────────────────────┐
│  NLP_AI_reader.py   │
│  PyMuPDF + Keywords │
└──────────┬──────────┘
           │
           │ Extracted Data
           ↓
┌─────────────────────┐
│  Calendar APIs      │
│  Google/Outlook/    │
│  Apple Calendar     │
└─────────────────────┘
```

## 🚀 Quick Start

### 1. Test the Python Parser

```bash
# Edit keywords in NLP_AI_reader.py
keywords = ["assignment", "exam", "quiz", "project"]

# Run the script
python NLP_AI_reader.py
```

### 2. Run the Flutter App

```bash
# Start the app
flutter run

# Or for specific platform
flutter run -d ios      # iOS
flutter run -d android  # Android
flutter run -d chrome   # Web (testing)
```

## 🎯 Roadmap

### Phase 1: Core Functionality
- [x] Python PDF parser with keyword extraction
- [x] Table detection and row extraction
- [x] Flutter UI with all screens
- [x] Landing page and navigation
- [ ] Backend API development (Flask/FastAPI)
- [ ] Connect Flutter to Python backend

### Phase 2: AI Enhancement
- [ ] Advanced NLP for date parsing
- [ ] Event type classification
- [ ] Course name detection
- [ ] Assignment weight extraction

### Phase 3: Calendar Integration
- [ ] Google Calendar API
- [ ] Microsoft Outlook API
- [ ] Apple Calendar sync
- [ ] iCal export option

### Phase 4: Polish
- [ ] File upload functionality
- [ ] Push notifications
- [ ] Progress tracking
- [ ] Multi-course management
- [ ] Cloud storage integration

## 🛠️ Tech Stack

**Backend:**
- Python 3.8+
- PyMuPDF (fitz) for PDF processing
- Future: Flask/FastAPI for REST API

**Frontend:**
- Flutter 3.0+
- Material Design 3
- Dart 3.0+

**APIs (Planned):**
- Google Calendar API
- Microsoft Graph API (Outlook)
- Apple Calendar

## 📝 File Structure

```
syllabize/
├── NLP_AI_reader.py              # Backend PDF parser
├── SyllabizePrototype2.dart      # Flutter app
├── README.md                     # This file
└── (future)
    ├── backend/
    │   ├── api/
    │   ├── models/
    │   └── services/
    └── frontend/
        ├── lib/
        ├── assets/
        └── test/
```

## 🤝 Contributing

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🔒 Privacy & Security

- Secure file handling with automatic deletion after processing
- No permanent storage of syllabus content
- Calendar access only with explicit user permission
- Data encryption in transit
- Local processing when possible

## 📄 License

This project is licensed under the MIT License.

## 📧 Contact

For questions or support, please open an issue on GitHub

---

**Made with ❤️ for students by students**
