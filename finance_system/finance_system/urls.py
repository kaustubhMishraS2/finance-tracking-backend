from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Finance API</title>
        <style>
            body {
                margin: 0;
                font-family: Arial, sans-serif;
                background: linear-gradient(to right, #1e3c72, #2a5298);
                color: white;
                text-align: center;
            }

            .container {
                padding: 50px;
            }

            h1 {
                font-size: 45px;
            }

            p {
                font-size: 18px;
            }

            .card {
                background: white;
                color: black;
                margin: 20px auto;
                padding: 20px;
                border-radius: 10px;
                width: 60%;
                box-shadow: 0 4px 10px rgba(0,0,0,0.2);
            }

            .btn {
                display: inline-block;
                margin: 10px;
                padding: 10px 20px;
                background: #ff9800;
                color: white;
                text-decoration: none;
                border-radius: 5px;
                font-weight: bold;
            }

            .btn:hover {
                background: #e68900;
            }

            footer {
                margin-top: 30px;
                font-size: 14px;
                opacity: 0.8;
            }
        </style>
    </head>

    <body>
        <div class="container">
            <h1>🚀 Finance Tracking API</h1>
            <p>Backend system built using Django REST Framework</p>

            <div class="card">
                <h2>📌 Features</h2>
                <p>✔ CRUD Operations (Create, Read, Update, Delete)</p>
                <p>✔ Filtering by Category & Type</p>
                <p>✔ Summary Analytics (Income, Expense, Balance)</p>
                <p>✔ User-based Data Security</p>
            </div>

            <div class="card">
                <h2>⚙️ Tech Stack</h2>
                <p>Django | Django REST Framework | SQLite</p>
            </div>

            <div class="card">
                <h2>🔗 Quick Links</h2>
                <a href="/api/transactions/" class="btn">View API</a>
                <a href="/admin/" class="btn">Admin Panel</a>
                <a href="/api-auth/login/" class="btn">Login</a>
                <a href="/api/register/" class="btn">Register</a>
            </div>

            <footer>
                👨‍💻 Developed by Kaustubh Mishra
            </footer>
        </div>
    </body>
    </html>
    """)

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/', include('finance.urls')),
    path('api-auth/', include('rest_framework.urls')),
]