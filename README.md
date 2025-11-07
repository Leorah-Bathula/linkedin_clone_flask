# 💼 LinkedIn Clone – Simple Social Media Website

A mini LinkedIn-style web app built with **Flask + MySQL** that allows users to sign up, log in, create posts, like, edit, and delete posts.
This project demonstrates **full-stack development skills** — frontend (HTML, CSS, JS), backend (Flask), and database (MySQL).

---

## 🚀 Features Implemented

### 🔐 User Authentication

* Register new users with name, email, and password
* Login and logout using secure session management
* Passwords stored using hashing (Werkzeug)

### 📝 Posts

* Create text posts (with optional image upload)
* Display all posts in a public feed (latest first)
* Edit and delete your own posts
* Like and unlike posts
* Show total like count per post

### 👤 Profile Page

* View all posts created by a particular user
* Each user has a dedicated profile page

---

## 🧰 Tech Stack Used

| Layer          | Technology                                       |
| -------------- | ------------------------------------------------ |
| **Frontend**   | HTML, CSS, Vanilla JavaScript                    |
| **Backend**    | Flask (Python)                                   |
| **Database**   | MySQL (via SQLAlchemy ORM)                       |
| **Libraries**  | Flask-Login, Flask-SQLAlchemy, PyMySQL, Werkzeug |
| **Deployment** | Render (Backend hosting)                         |

---

## ⚙️ How to Run the Project Locally

### 1️⃣ Clone this repository

```bash
git clone https://github.com/Leorah-Bathula/linkedin_clone_flask.git
cd linkedin_clone_flask
```

### 2️⃣ Create a virtual environment

```bash
python -m venv venv
.\venv\Scripts\activate    # for Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Set up the MySQL Database

Open MySQL Workbench and run:

```sql
CREATE DATABASE linkedin_clone;
```

Then, open `config.py` and update this line:

```python
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:your_password@localhost/linkedin_clone"
```

*(Replace `your_password` with your MySQL password)*

### 5️⃣ Run the application

```bash
python app.py
```

Now open your browser and go to → [http://localhost:5000](http://localhost:5000)

---

## 🧑‍💼 Demo Login Credentials

To save time, use these demo accounts to test quickly:

| Name               | Email                                     | Password |
| ------------------ | ----------------------------------------- | -------- |
| **Chris**          | [chris@gmail.com](mailto:chris@gmail.com) | chris!@  |
| **Priya**          | [priya@gmail.com](mailto:priya@gmail.com) | 12345    |


Or, register a new account using the **Sign Up** page.

---

## 🌐 Deployment (Render)

1. Push your project to **GitHub**.
2. Go to [https://render.com](https://render.com) → **New Web Service**.
3. Connect your GitHub repository.
4. In the settings:

   * Runtime: Python 3
   * Start Command: `python app.py`
   * Environment Variable: `SECRET_KEY = yoursecretkey`
5. Deploy 🚀
   You’ll get a live link like:
   `https://linkedin-clone-flask.onrender.com`

---

## 🧾 Evaluation Criteria (AppDost)

| Requirement                                     | Implemented |
| ----------------------------------------------- | ----------- |
| Working Signup/Login System                     | ✅           |
| Create and View Posts                           | ✅           |
| Clean UI and Responsive Design                  | ✅           |
| Extra Features (Like/Edit/Delete/Profile/Image) | ✅           |

---

## 📸 Screenshots

| Screenshot            | File Name       | Example Location                   |
| --------------------- | --------------- | ---------------------------------- |
| Signup Page           | signup.png      | static/screenshots/signup.png      |
| Login Page            | login.png       | static/screenshots/login.png       |
| Feed Page             | feed.png        | static/screenshots/feed.png        |
| Profile Page (Leorah) | profile.png     | static/screenshots/profile.png     |
| Create Post Page      | create_post.png | static/screenshots/create_post.png |

Add these screenshots to your repository in the path mentioned above so they appear on GitHub.

---

## 👨‍💻 Author

**Name:** Leorah Bathula
**Email:** [leorahbathula@gmail.com](mailto:leorahbathula@gmail.com)
**City:** Hyderabad, Telangana
**Phone:** 6281538403
**Role:** Full Stack Developer Intern Applicant (AppDost)

---

## 🏁 Submission Links

* 🔗 **GitHub Repository:** [https://github.com/Leorah-Bathula/linkedin_clone_flask](https://github.com/Leorah-Bathula/linkedin_clone_flask)
* 🌍 **Live Project Link (Render):** [https://linkedin-clone-flask.onrender.com](https://linkedin-clone-flask.onrender.com)

⭐ *This project was developed as part of the Full Stack Developer Internship assignment for AppDost, demonstrating frontend, backend, and database integration.*
