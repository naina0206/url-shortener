# URL Shortener

A Django-based URL shortener application with statistics tracking and a beautiful pastel pink/beige UI.

## Features

- Shorten long URLs into short, shareable links
- Track click statistics for shortened URLs
- View detailed analytics including:
  - Total clicks
  - Days active
  - Average clicks per day
  - Creation date
  - Last clicked timestamp
- Modern, responsive UI with pastel pink/beige color scheme
- Quick stats lookup by short code

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd URL_shortner
```

2. Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up the database:
   - Update database credentials in `URLshortener/URLshortener/settings.py`
   - Run migrations:
```bash
cd URLshortener
python manage.py migrate
```

5. Run the development server:
```bash
python manage.py runserver
```

6. Open your browser and navigate to `http://127.0.0.1:8000/`

## Usage

1. **Shorten a URL**: Enter a long URL in the form and click "Shorten URL"
2. **Access shortened URL**: Use the format `http://yourdomain.com/s/<code>/`
3. **View Statistics**: 
   - Click "View Statistics" after creating a URL, or
   - Enter a short code in the stats lookup section on the home page

## Project Structure

```
URL_shortner/
├── URLshortener/
│   ├── manage.py
│   ├── shortener/          # Main app
│   │   ├── models.py       # URL model
│   │   ├── views.py        # View functions
│   │   ├── urls.py         # URL routing
│   │   └── templates/      # HTML templates
│   └── URLshortener/       # Project settings
│       ├── settings.py
│       └── urls.py
├── requirements.txt
└── README.md
```

## Security Notes

⚠️ **Important**: Before deploying to production:
- Change the `SECRET_KEY` in `settings.py`
- Move database credentials to environment variables
- Set `DEBUG = False` in production
- Update `ALLOWED_HOSTS` with your domain

## Technologies Used

- Django 5.2.7
- PostgreSQL (psycopg2)
- HTML/CSS/JavaScript

## License

This project is open source and available for use.

