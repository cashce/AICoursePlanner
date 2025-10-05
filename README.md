# Syllabize 📚

> Your AI-powered academic calendar assistant

Syllabize helps students stay organized by automatically extracting key dates (assignments, exams, readings) from course syllabi and populating their digital calendar with reminders and deadlines.

## Features ✨

### Core Features
- **Syllabus Upload**: Drag-and-drop or select PDF, DOCX, or TXT syllabus files
- **AI Parsing Engine**: Automatically extracts dates, assignment names, exam info, and descriptions
- **Calendar Integration**: Syncs with Google Calendar, Outlook, and Apple Calendar
- **Review Interface**: Preview and edit extracted events before syncing
- **Smart Notifications**: Customizable reminders for upcoming deadlines

### Additional Features
- **Course Dashboard**: Overview of all courses and upcoming tasks
- **Progress Tracking**: Visual indicators for task priorities
- **Multi-format Support**: Handles varied syllabus formatting and language styles

## Screenshots 📱

- Landing page with app introduction
- Upload screen with drag-and-drop interface
- Review screen to edit extracted events
- Dashboard with upcoming deadlines
- Settings for calendar integration and notifications

## Tech Stack 🛠️

### Frontend
- **Flutter**: Cross-platform mobile app (iOS & Android)
- **Material Design 3**: Modern, responsive UI components

### Backend (Planned)
- **Python**: Flask or FastAPI
- **AI/NLP**: 
  - PyMuPDF, pdfminer, python-docx for file parsing
  - spaCy, transformers, or OpenAI API for NLP
  - dateparser for intelligent date extraction
- **Calendar APIs**: Google Calendar API, Microsoft Graph API

## Getting Started 🚀

### Prerequisites
- Flutter SDK (3.0 or higher)
- Dart 3.0+
- Android Studio / Xcode for mobile development

### Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/syllabize.git
cd syllabize
```

2. Install dependencies
```bash
flutter pub get
```

3. Run the app
```bash
flutter run
```

### Running on Different Platforms

**iOS**
```bash
flutter run -d ios
```

**Android**
```bash
flutter run -d android
```

**Web** (for testing)
```bash
flutter run -d chrome
```

## Project Structure 📁

```
syllabize/
├── lib/
│   ├── main.dart                 # App entry point
│   ├── screens/
│   │   ├── landing_page.dart     # Welcome screen
│   │   ├── upload_screen.dart    # Syllabus upload
│   │   ├── review_screen.dart    # Event review/edit
│   │   ├── dashboard_screen.dart # Course overview
│   │   └── settings_screen.dart  # App settings
│   ├── models/
│   │   └── event.dart            # Event data models
│   └── services/
│       ├── file_service.dart     # File handling
│       ├── api_service.dart      # Backend communication
│       └── calendar_service.dart # Calendar integration
├── assets/                        # Images and resources
└── test/                         # Unit and widget tests
```

## Roadmap 🗺️

- [x] Landing page
- [x] Upload interface
- [x] Review screen with edit functionality
- [x] Dashboard with upcoming tasks
- [x] Settings page
- [ ] Backend AI parsing integration
- [ ] Calendar API implementation
- [ ] File upload functionality
- [ ] Push notifications
- [ ] Progress tracking
- [ ] Multi-course support

## Usage 💡

1. **Upload Syllabus**: Tap the upload button and select your course syllabus
2. **AI Processing**: The app extracts all assignments, exams, and readings
3. **Review Events**: Check and edit extracted dates and descriptions
4. **Sync Calendar**: Confirm to add events to your connected calendar
5. **Stay Organized**: Receive reminders and track your progress

## Success Metrics 📊

- 90%+ accuracy in date extraction
- <5 minutes average time to process and sync a syllabus
- 80%+ user satisfaction in usability surveys

## Contributing 🤝

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Privacy & Security 🔒

- Secure file handling with automatic deletion after processing
- No permanent storage of syllabus content
- Calendar access only with explicit user permission
- Data encryption in transit

## License 📄

This project is licensed under the MIT License - see the LICENSE file for details.

## Support 💬

For questions or support, please open an issue on GitHub or contact support@syllabize.app

## Acknowledgments 🙏

- Built with Flutter and Material Design 3
- AI parsing powered by state-of-the-art NLP models
- Inspired by the needs of busy students everywhere

---

Made with ❤️ for students by students
