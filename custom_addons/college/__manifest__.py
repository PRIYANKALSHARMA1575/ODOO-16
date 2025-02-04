{
    'name': 'College Management System',
    'author' : 'Priyanka L Sharma',
    'website' : 'www.citchennai.net',
    'category' : 'Education',
    'summary' : 'A module set up to manage courses, student information and attendance',
    'depends' : ['mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'data/attendance_sequence.xml',
        'views/subject.xml',
        'views/menu.xml',
        'views/student.xml',
        'views/teacher.xml',
        'views/department.xml',
        'views/classroom.xml',
        'views/attendance.xml', # New subject view
        'views/timetable.xml',
    ],
    'license': 'LGPL-3',
    'installable' : True,
    'application' : True
}
