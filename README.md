# Christiana Catherine White - Author Website

A beautiful, feminine, and faith-centered website for Christian author Christiana Catherine White, showcasing her debut book "Victory in His Blood" and sharing her Christian journey.

## Features

- **Home Page**: Hero section with book preview, featured Bible verses, and testimonials
- **About Page**: Author's testimony and journey of faith
- **Book Page**: Detailed information about "Victory in His Blood"
- **Contact Page**: Contact form and prayer request section
- **Christian Elements**: Bible verses, cross symbols, and faith-focused content throughout
- **Feminine Design**: Soft color palette, elegant typography, and graceful styling
- **Responsive Design**: Works beautifully on all devices

## Tech Stack

- **Django 4.2.7**: Backend framework
- **Bootstrap 5.3.2**: CSS framework for responsive design
- **Vanilla JavaScript**: No frameworks, pure JS for interactivity
- **Custom CSS**: Feminine, Christian-themed styling

## Installation

1. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   source venv/bin/activate  # On Mac/Linux
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

4. **Create a superuser** (optional, for admin access):
   ```bash
   python manage.py createsuperuser
   ```

5. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

6. **Visit the website**:
   Open your browser and go to `http://127.0.0.1:8000/`

## Project Structure

```
christy_project/
├── christy_project/          # Main project settings
│   ├── settings.py           # Django settings
│   ├── urls.py              # Main URL configuration
│   └── ...
├── website/                  # Main app
│   ├── templates/           # HTML templates
│   │   └── website/
│   │       ├── base.html    # Base template
│   │       ├── home.html    # Home page
│   │       ├── about.html   # About page
│   │       ├── book.html    # Book page
│   │       └── contact.html # Contact page
│   ├── views.py             # View functions
│   ├── urls.py              # App URLs
│   └── ...
├── static/                   # Static files
│   ├── css/
│   │   └── style.css        # Custom styles
│   └── js/
│       └── main.js          # JavaScript
├── manage.py
└── requirements.txt
```

## Customization

### Images

Replace the placeholder images with actual images:
- Book cover: Update in `home.html`, `book.html`, and `about.html`
- Author photo: Update in `home.html` and `about.html`
- Add images to `static/images/` and reference them in templates

### Content

- Update Bible verses and testimonies as needed
- Modify author bio and book description
- Update contact information (email, social media links)

### Colors

The color scheme is defined in `static/css/style.css` using CSS variables:
- Primary: `#8B6F7E` (Soft Purple-Pink)
- Secondary: `#D4C5B0` (Warm Beige)
- Accent: `#E8D5C4` (Light Peach)

## Contact Form

The contact form currently uses a simulated submission. To enable actual email functionality:

1. Configure email settings in `settings.py`
2. Update the contact form handler in `website/views.py`
3. Uncomment the actual AJAX code in `static/js/main.js`

## Deployment

1. Set `DEBUG = False` in `settings.py`
2. Update `ALLOWED_HOSTS` with your domain
3. Set a secure `SECRET_KEY`
4. Collect static files: `python manage.py collectstatic`
5. Configure a production database (PostgreSQL recommended)
6. Deploy to your hosting service (Heroku, AWS, etc.)

## Notes

- All images are currently placeholders and should be replaced
- Contact form submission needs backend implementation
- Social media links are placeholders and should be updated
- Purchase links are placeholders and should be linked to actual retailers

## License

© 2024 Christiana Catherine White. All rights reserved.

---

*"But thanks be to God, who gives us the victory through our Lord Jesus Christ."* - 1 Corinthians 15:57

