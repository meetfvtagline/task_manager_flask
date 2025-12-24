task_manager/
│
├── app/
│   ├── __init__.py
│   ├── routes/
│   │   ├── auth.py        # login, register, logout
│   │   ├── tasks.py       # task CRUD logic
│   │
│   ├── models/
│   │   ├── user.py        # user database model
│   │   ├── task.py        # task database model
│   │
│   ├── templates/
│   │   ├── auth/
│   │   │   ├── login.html
│   │   │   ├── register.html
│   │   │
│   │   ├── tasks/
│   │   │   ├── dashboard.html
│   │   │   ├── edit_task.html
│   │   │
│   │   └── base.html
│   │
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   │
│   ├── config.py          # app configuration
│   └── extensions.py     # db, login manager
│
├── migrations/            # database migrations
├── tests/                 # optional but professional
│
├── .env                   # environment variables
├── requirements.txt       # project dependencies
├── main.py                 # app entry point
└── README.md
