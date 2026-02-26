# 🔖 Smart Bookmark Manager

A full-stack Bookmark CRUD Application** built with **Django** and **Django REST Framework**, featuring a clean responsive frontend and a fully functional REST API.

---

## 🌐 Live Demo

🚀 **Deployed on Render:** https://smart-bookmark-manager-45pf.onrender.com/

---

## 📌 Features

- ✅ Add a new bookmark (Title + URL)
- ✅ View all saved bookmarks
- ✅ Edit / Update an existing bookmark
- ✅ Delete a bookmark
- ✅ REST API for all CRUD operations
- ✅ Clean and responsive frontend UI
- ✅ Deployed and accessible online

---

## 🛠️ Tech Stack

| Layer       | Technology                        |
|-------------|-----------------------------------|
| Backend     | Django 4.x                        |
| REST API    | Django REST Framework             |
| Database    | SQLite (local) / PostgreSQL (prod)|
| Frontend    | HTML, CSS, Vanilla JavaScript     |
| CORS        | django-cors-headers               |
| Static Files| WhiteNoise                        |
| Deployment  | Render.com                        |

---

## 📁 Project Structure

```
bookmark_manager/
├── manage.py
├── requirements.txt
├── build.sh
├── Procfile
├── README.md
├── bookmarks/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── serializers.py
│   ├── admin.py
│   └── templates/
│       └── bookmarks/
│           └── index.html
└── bookmark_manager/
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

---

## 🔗 API Endpoints

| Method   | Endpoint                    | Description             |
|----------|-----------------------------|-------------------------|
| `GET`    | `/api/bookmarks/`           | Get all bookmarks       |
| `POST`   | `/api/bookmarks/`           | Create a new bookmark   |
| `GET`    | `/api/bookmarks/<id>/`      | Get a single bookmark   |
| `PUT`    | `/api/bookmarks/<id>/`      | Update a bookmark       |
| `DELETE` | `/api/bookmarks/<id>/`      | Delete a bookmark       |

### 📦 Sample Request & Response

**POST** `/api/bookmarks/`

Request Body:
```json
{
  "title": "Google",
  "url": "https://www.google.com"
}
```

Response `201 Created`:
```json
{
  "id": 1,
  "title": "Google",
  "url": "https://www.google.com",
  "created_at": "2024-01-01T10:00:00Z",
  "updated_at": "2024-01-01T10:00:00Z"
}
```

---

## ⚙️ Local Setup Instructions

Follow these steps to run the project on your local machine.

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/bookmark-manager.git
cd bookmark-manager
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On Mac/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. (Optional) Create Admin Superuser

```bash
python manage.py createsuperuser
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

### 7. Open in Browser

```
http://127.0.0.1:8000/
```

---

## ☁️ Deployment on Render

This project is deployed using [Render](https://render.com).

Follow the steps below to deploy your own instance.

### Prerequisites
- A [Render](https://render.com) account (free)
- A [GitHub](https://github.com) account with this project pushed

---

### Step 1 — Push Code to GitHub

```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR_USERNAME/bookmark-manager.git
git branch -M main
git push -u origin main
```

---

### Step 2 — Create a Web Service on Render

1. Go to [https://render.com](https://render.com) and log in
2. Click **"New +"** → Select **"Web Service"**
3. Connect your GitHub account and select the `bookmark-manager` repo
4. Fill in the following settings:

| Field            | Value                                          |
|------------------|------------------------------------------------|
| Name             | `bookmark-manager`                             |
| Runtime          | `Python 3`                                     |
| Build Command    | `./build.sh`                                   |
| Start Command    | `gunicorn bookmark_manager.wsgi:application`   |
| Plan             | `Free`                                         |

---

### Step 3 — Set Environment Variables

In the Render dashboard under **Environment**, add:

| Key             | Value                              |
|-----------------|------------------------------------|
| `SECRET_KEY`    | *(generate a secure random key)*   |
| `DEBUG`         | `False`                            |
| `PYTHON_VERSION`| `3.11.0`                           |

To generate a SECRET_KEY locally:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

---

### Step 4 — Deploy

Click **"Create Web Service"**. Render will:
- Install all dependencies from `requirements.txt`
- Collect static files
- Run database migrations
- Start the server with Gunicorn

Your app will be live at:
```
(https://smart-bookmark-manager-45pf.onrender.com/)
```

---

### 🔄 Auto-Deploy on Every Push

Every time you push to the `main` branch, Render will **automatically redeploy** your app.

```bash
git add .
git commit -m "your update"
git push origin main
# Render redeploys automatically ✅
```

---

## 🐛 Common Issues & Fixes

| Issue                       | Fix                                                                            |
|-----------------------------|--------------------------------------------------------------------------------|
| Build fails on Render        | Ensure `requirements.txt` is up to date (`pip freeze > requirements.txt`)     |
| Static files not loading     | Confirm `whitenoise` is in `MIDDLEWARE` in `settings.py`                      |
| `DisallowedHost` error       | Set `ALLOWED_HOSTS = ['*']` in `settings.py`                                  |
| Database resets on redeploy  | Add a PostgreSQL database via Render dashboard                                 |
| App crashes on start         | Verify start command matches your project name in `wsgi.py`                   |

---

## 📸 Screenshots

<img width="1919" height="1006" alt="image" src="https://github.com/user-attachments/assets/216f3084-0450-424e-b438-01ef60a17527" />

.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙋‍♂️ Author

**R SUCHARITHA REDDY**

- GitHub: (https://github.com/sucharitha6711)

---

> ⭐ If you found this project helpful, please give it a star on GitHub!
