import 'package:flutter/material.dart';

void main() {
  runApp(const SyllabizeApp());
}

class SyllabizeApp extends StatelessWidget {
  const SyllabizeApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Syllabize',
      theme: ThemeData(
        primarySwatch: Colors.blue,
        useMaterial3: true,
      ),
      home: const HomeScreen(),
    );
  }
}

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  int _selectedIndex = 0;

  final List<Widget> _screens = [
    const UploadScreen(),
    const DashboardScreen(),
    const SettingsScreen(),
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: _screens[_selectedIndex],
      bottomNavigationBar: NavigationBar(
        selectedIndex: _selectedIndex,
        onDestinationSelected: (int index) {
          setState(() {
            _selectedIndex = index;
          });
        },
        destinations: const [
          NavigationDestination(
            icon: Icon(Icons.upload_file),
            label: 'Upload',
          ),
          NavigationDestination(
            icon: Icon(Icons.dashboard),
            label: 'Dashboard',
          ),
          NavigationDestination(
            icon: Icon(Icons.settings),
            label: 'Settings',
          ),
        ],
      ),
    );
  }
}

// Upload Screen
class UploadScreen extends StatelessWidget {
  const UploadScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Syllabize'),
        centerTitle: true,
      ),
      body: Center(
        child: Padding(
          padding: const EdgeInsets.all(24.0),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              const Icon(
                Icons.school,
                size: 80,
                color: Colors.blue,
              ),
              const SizedBox(height: 24),
              const Text(
                'Upload Your Syllabus',
                style: TextStyle(
                  fontSize: 28,
                  fontWeight: FontWeight.bold,
                ),
              ),
              const SizedBox(height: 16),
              const Text(
                'Automatically extract assignments, exams, and deadlines',
                textAlign: TextAlign.center,
                style: TextStyle(
                  fontSize: 16,
                  color: Colors.grey,
                ),
              ),
              const SizedBox(height: 48),
              Container(
                width: double.infinity,
                height: 200,
                decoration: BoxDecoration(
                  border: Border.all(color: Colors.blue, width: 2),
                  borderRadius: BorderRadius.circular(12),
                  color: Colors.blue.withOpacity(0.05),
                ),
                child: InkWell(
                  onTap: () {
                    Navigator.push(
                      context,
                      MaterialPageRoute(
                        builder: (context) => const ReviewScreen(),
                      ),
                    );
                  },
                  child: const Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      Icon(Icons.cloud_upload, size: 64, color: Colors.blue),
                      SizedBox(height: 16),
                      Text(
                        'Drag & drop or tap to upload',
                        style: TextStyle(fontSize: 16),
                      ),
                      SizedBox(height: 8),
                      Text(
                        'PDF, DOCX, TXT',
                        style: TextStyle(color: Colors.grey),
                      ),
                    ],
                  ),
                ),
              ),
              const SizedBox(height: 24),
              ElevatedButton.icon(
                onPressed: () {
                  Navigator.push(
                    context,
                    MaterialPageRoute(
                      builder: (context) => const ReviewScreen(),
                    ),
                  );
                },
                icon: const Icon(Icons.upload_file),
                label: const Text('Choose File'),
                style: ElevatedButton.styleFrom(
                  padding: const EdgeInsets.symmetric(
                    horizontal: 32,
                    vertical: 16,
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}

// Review Screen
class ReviewScreen extends StatefulWidget {
  const ReviewScreen({super.key});

  @override
  State<ReviewScreen> createState() => _ReviewScreenState();
}

class _ReviewScreenState extends State<ReviewScreen> {
  // Sample extracted events
  final List<Map<String, dynamic>> extractedEvents = [
    {
      'title': 'Essay 1: Critical Analysis',
      'date': DateTime(2025, 10, 15),
      'type': 'Assignment',
      'description': '5-7 pages on selected topic',
      'selected': true,
    },
    {
      'title': 'Midterm Exam',
      'date': DateTime(2025, 10, 28),
      'type': 'Exam',
      'description': 'Chapters 1-5',
      'selected': true,
    },
    {
      'title': 'Reading: Chapter 3',
      'date': DateTime(2025, 10, 10),
      'type': 'Reading',
      'description': 'The Social Contract',
      'selected': true,
    },
    {
      'title': 'Group Project Presentation',
      'date': DateTime(2025, 11, 12),
      'type': 'Assignment',
      'description': 'Final team presentation',
      'selected': true,
    },
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Review Events'),
        actions: [
          TextButton(
            onPressed: () {
              _showSuccessDialog(context);
            },
            child: const Text('Sync All'),
          ),
        ],
      ),
      body: ListView.builder(
        padding: const EdgeInsets.all(16),
        itemCount: extractedEvents.length,
        itemBuilder: (context, index) {
          final event = extractedEvents[index];
          return Card(
            margin: const EdgeInsets.only(bottom: 12),
            child: CheckboxListTile(
              value: event['selected'],
              onChanged: (bool? value) {
                setState(() {
                  event['selected'] = value ?? false;
                });
              },
              title: Text(
                event['title'],
                style: const TextStyle(fontWeight: FontWeight.bold),
              ),
              subtitle: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  const SizedBox(height: 4),
                  Row(
                    children: [
                      Icon(
                        _getIconForType(event['type']),
                        size: 16,
                        color: _getColorForType(event['type']),
                      ),
                      const SizedBox(width: 4),
                      Text(event['type']),
                      const SizedBox(width: 16),
                      const Icon(Icons.calendar_today, size: 16),
                      const SizedBox(width: 4),
                      Text(_formatDate(event['date'])),
                    ],
                  ),
                  const SizedBox(height: 4),
                  Text(
                    event['description'],
                    style: const TextStyle(color: Colors.grey),
                  ),
                ],
              ),
              secondary: IconButton(
                icon: const Icon(Icons.edit),
                onPressed: () {
                  _showEditDialog(context, event);
                },
              ),
            ),
          );
        },
      ),
    );
  }

  IconData _getIconForType(String type) {
    switch (type) {
      case 'Exam':
        return Icons.quiz;
      case 'Assignment':
        return Icons.assignment;
      case 'Reading':
        return Icons.book;
      default:
        return Icons.event;
    }
  }

  Color _getColorForType(String type) {
    switch (type) {
      case 'Exam':
        return Colors.red;
      case 'Assignment':
        return Colors.orange;
      case 'Reading':
        return Colors.green;
      default:
        return Colors.blue;
    }
  }

  String _formatDate(DateTime date) {
    return '${date.month}/${date.day}/${date.year}';
  }

  void _showEditDialog(BuildContext context, Map<String, dynamic> event) {
    showDialog(
      context: context,
      builder: (context) => AlertDialog(
        title: const Text('Edit Event'),
        content: const Text('Edit functionality would be implemented here'),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(context),
            child: const Text('Cancel'),
          ),
          TextButton(
            onPressed: () => Navigator.pop(context),
            child: const Text('Save'),
          ),
        ],
      ),
    );
  }

  void _showSuccessDialog(BuildContext context) {
    showDialog(
      context: context,
      builder: (context) => AlertDialog(
        title: const Text('Success!'),
        content: const Text('Events synced to your calendar'),
        actions: [
          TextButton(
            onPressed: () {
              Navigator.pop(context);
              Navigator.pop(context);
            },
            child: const Text('OK'),
          ),
        ],
      ),
    );
  }
}

// Dashboard Screen
class DashboardScreen extends StatelessWidget {
  const DashboardScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Dashboard'),
      ),
      body: ListView(
        padding: const EdgeInsets.all(16),
        children: [
          const Text(
            'Upcoming Deadlines',
            style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
          ),
          const SizedBox(height: 16),
          _buildTaskCard(
            'Reading: Chapter 3',
            'Due in 6 days',
            Colors.green,
            Icons.book,
          ),
          _buildTaskCard(
            'Essay 1: Critical Analysis',
            'Due in 11 days',
            Colors.orange,
            Icons.assignment,
          ),
          _buildTaskCard(
            'Midterm Exam',
            'Due in 24 days',
            Colors.red,
            Icons.quiz,
          ),
          const SizedBox(height: 24),
          const Text(
            'Courses',
            style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
          ),
          const SizedBox(height: 16),
          _buildCourseCard('Philosophy 101', '12 upcoming tasks'),
          _buildCourseCard('Computer Science 202', '8 upcoming tasks'),
        ],
      ),
    );
  }

  Widget _buildTaskCard(String title, String subtitle, Color color, IconData icon) {
    return Card(
      margin: const EdgeInsets.only(bottom: 12),
      child: ListTile(
        leading: CircleAvatar(
          backgroundColor: color,
          child: Icon(icon, color: Colors.white),
        ),
        title: Text(title),
        subtitle: Text(subtitle),
        trailing: const Icon(Icons.chevron_right),
      ),
    );
  }

  Widget _buildCourseCard(String title, String subtitle) {
    return Card(
      margin: const EdgeInsets.only(bottom: 12),
      child: ListTile(
        leading: const CircleAvatar(
          child: Icon(Icons.school),
        ),
        title: Text(title),
        subtitle: Text(subtitle),
        trailing: const Icon(Icons.chevron_right),
      ),
    );
  }
}

// Settings Screen
class SettingsScreen extends StatefulWidget {
  const SettingsScreen({super.key});

  @override
  State<SettingsScreen> createState() => _SettingsScreenState();
}

class _SettingsScreenState extends State<SettingsScreen> {
  bool _notificationsEnabled = true;
  String _selectedCalendar = 'Google Calendar';

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Settings'),
      ),
      body: ListView(
        children: [
          const Padding(
            padding: EdgeInsets.all(16),
            child: Text(
              'Calendar Integration',
              style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
            ),
          ),
          ListTile(
            leading: const Icon(Icons.calendar_today),
            title: const Text('Connected Calendar'),
            subtitle: Text(_selectedCalendar),
            trailing: const Icon(Icons.chevron_right),
            onTap: () {
              _showCalendarDialog();
            },
          ),
          const Divider(),
          const Padding(
            padding: EdgeInsets.all(16),
            child: Text(
              'Notifications',
              style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
            ),
          ),
          SwitchListTile(
            secondary: const Icon(Icons.notifications),
            title: const Text('Enable Notifications'),
            subtitle: const Text('Get reminders for upcoming deadlines'),
            value: _notificationsEnabled,
            onChanged: (bool value) {
              setState(() {
                _notificationsEnabled = value;
              });
            },
          ),
          ListTile(
            leading: const Icon(Icons.access_time),
            title: const Text('Reminder Time'),
            subtitle: const Text('1 day before deadline'),
            trailing: const Icon(Icons.chevron_right),
          ),
          const Divider(),
          const Padding(
            padding: EdgeInsets.all(16),
            child: Text(
              'About',
              style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
            ),
          ),
          const ListTile(
            leading: Icon(Icons.info),
            title: Text('Version'),
            subtitle: Text('1.0.0'),
          ),
          ListTile(
            leading: const Icon(Icons.privacy_tip),
            title: const Text('Privacy Policy'),
            trailing: const Icon(Icons.chevron_right),
            onTap: () {},
          ),
        ],
      ),
    );
  }

  void _showCalendarDialog() {
    showDialog(
      context: context,
      builder: (context) => AlertDialog(
        title: const Text('Select Calendar'),
        content: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            ListTile(
              title: const Text('Google Calendar'),
              leading: Radio<String>(
                value: 'Google Calendar',
                groupValue: _selectedCalendar,
                onChanged: (value) {
                  setState(() {
                    _selectedCalendar = value!;
                  });
                  Navigator.pop(context);
                },
              ),
            ),
            ListTile(
              title: const Text('Outlook'),
              leading: Radio<String>(
                value: 'Outlook',
                groupValue: _selectedCalendar,
                onChanged: (value) {
                  setState(() {
                    _selectedCalendar = value!;
                  });
                  Navigator.pop(context);
                },
              ),
            ),
            ListTile(
              title: const Text('Apple Calendar'),
              leading: Radio<String>(
                value: 'Apple Calendar',
                groupValue: _selectedCalendar,
                onChanged: (value) {
                  setState(() {
                    _selectedCalendar = value!;
                  });
                  Navigator.pop(context);
                },
              ),
            ),
          ],
        ),
      ),
    );
  }
}
