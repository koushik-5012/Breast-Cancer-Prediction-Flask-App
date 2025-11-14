Breast Cancer Prediction – End-to-End Machine Learning & Deployment
This project is an end-to-end implementation of a Breast Cancer Prediction System using:



# Breast Cancer Prediction — End-to-End Machine Learning & Deployment

 🔗 Live Demo
http://13.126.224.49/

This project is an end-to-end implementation...


Machine Learning Model (Random Forest)

Flask Web Application

AWS EC2 Deployment using Nginx + Gunicorn

I built this project to learn how a real ML solution goes from:
data → model → web app → cloud deployment.

It is fully functional and hosted on an AWS EC2 server.

1. Project Overview

The goal of this project was to create a simple but complete breast cancer prediction system.
I trained a classifier using the Breast Cancer Wisconsin dataset and exposed it through a basic Flask UI where a user can enter input features and instantly get:

The prediction (Cancer / Not cancer)

Confidence score

Finally, I deployed the entire application on AWS EC2, using:

Gunicorn (Python WSGI server)

Nginx (Reverse proxy for production)

Virtual environment

PM2-style service using systemd to run Flask in background

2. Live Demo Screenshot

Place your screenshot file as:

ui_screenshot.png


Then the preview will appear below:

3. What I Learned / Key Highlights
✔ Machine Learning Model Building

Preprocessed dataset

Selected features

Trained Random Forest

Achieved high accuracy

Prepared model input pipeline

✔ Flask App Development

Built a fully working Flask backend

Created web forms to collect model inputs

Processed user input and returned prediction + confidence

Used Jinja2 templates for rendering UI

✔ AWS EC2 Deployment (Production-Level)

I deployed the app entirely from scratch, learning a lot along the way:

Creating and securing an EC2 instance

Using .pem SSH keys

Using Cyberduck to upload project files

Setting up virtual environment

Installing Python dependencies

Running Flask using Gunicorn

Configuring Nginx reverse proxy

Creating systemd service (flaskapp.service)

Debugging deployment errors

This helped me understand the real-world production workflow of ML apps.

4. Challenges I Faced & How I Solved Them
1. File Location Issues in Cyberduck

At first, my app.py was inside the wrong folder (inside venv).
This caused the error:
“Could not import app”
I fixed it by moving files to:

/home/ubuntu/flask_app/

2. Gunicorn not stopping (CTRL+C not working)

Gunicorn kept running, blocking commands.
I solved it using:

ps aux | grep gunicorn
sudo kill -9 <PID>

3. Form Submission Error – “Access to localhost was denied”

This happened because my HTML form still pointed to:

http://localhost:5000


I changed it to:

<form action="/" method="POST">


After updating the template and restarting services, everything worked.

4. Nginx Conflicts

Nginx gave a “duplicate server_name” warning.
I fixed it by disabling the default config:

sudo unlink /etc/nginx/sites-enabled/default


Then restarted Nginx.

5. Service Creation Confusion

Learning systemd (CTRL + O, CTRL + X steps, file paths, ExecStart) took some time.
Finally, I successfully created:

/etc/systemd/system/flaskapp.service


and enabled it.

5. Project Structure
Breast Cancer Prediction/
│
├── app.py
├── requirements.txt
├── README.md
├── ## Application UI
![Breast Cancer Prediction Screenshot](Screenshot.png)

│
└── templates/
    └── home.html

6. How to Run the Project Locally
1. Clone the repo
git clone https://github.com/<koushik-5012>/breast-cancer-prediction.git
cd breast-cancer-prediction

2. Create virtual environment
python3 -m venv venv
source venv/bin/activate

3. Install libraries
pip install -r requirements.txt

4. Run Flask
python3 app.py


Visit:

http://127.0.0.1:5000

7. Deployment Architecture (AWS EC2)
Backend

Ubuntu EC2 instance

Python virtual environment

Flask app served with Gunicorn

Frontend / Routing

Nginx reverse proxy

Port 80 open in inbound rules

Handles traffic and forwards to Gunicorn

Service Management
sudo systemctl restart flaskapp
sudo systemctl restart nginx
sudo systemctl status flaskapp

8. Technologies Used

Python

Pandas, NumPy

Scikit-learn

Flask

Bootstrap

Gunicorn

Nginx

AWS EC2

Cyberduck

SSH

9. Future Improvements

Improve UI design

Add more features from the dataset

Add model saving/loading instead of retraining every request

Add HTTPS (LetsEncrypt)

Add logging

Add Docker support

10. Author

Kethan Koushik
