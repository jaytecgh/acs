# Backend - JayTec Inventory & Invoicing System

This is the **Django + DRF backend** for the JayTec Inventory & Invoicing System. It manages authentication, role-based access, inventory, sales, purchases, PDF/Excel export, and more.

---

## 🎯 Project Goals

- Provide secure and flexible API endpoints for frontend consumption
- Manage user roles and permissions
- Handle business logic for sales, purchases, and inventory
- Generate and email PDF invoices and financial reports

---

## ⚙️ Technologies Used

- **Python 3**
- **Django 4+**
- **Django REST Framework (DRF)**
- **SimpleJWT** for authentication
- **ReportLab** for PDF generation
- **Pandas / openpyxl** for Excel/CSV export
- **SQLite** (local), PostgreSQL (recommended for prod)

---

## 🛠️ Installation & Setup

1. Navigate into backend directory:
   ```bash
   cd backend
   ```

2. Create virtual environment:
   ```bash
   python -m venv virtual
   source virtual/Scripts/activate  # On Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create `.env` file:
   ```env
   SECRET_KEY=your_secret_key
   DEBUG=True
   EMAIL_HOST_USER=your_email@gmail.com
   EMAIL_HOST_PASSWORD=your_app_password
   ```

5. Apply migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Create superuser:
   ```bash
   python manage.py createsuperuser
   ```

7. Start server:
   ```bash
   python manage.py runserver
   ```

---

## 🗂️ Project Structure

```
backend/
├── acs_backend/          # Project root config
├── core/                 # Users, roles, employees
├── sales/                # Sales, Invoices
├── purchase/             # Purchase logic
├── inventory/            # Stock management
├── transport/            # Delivery/Logistics
├── media/                # PDF uploads and static assets
```

---

## 🔐 Authentication & Authorization

- Uses **SimpleJWT**:
  - `access` and `refresh` tokens
- Endpoints:
  - `/api/token/` - login
  - `/api/token/refresh/`
  - `/api/register/`
- Custom roles:
  - Admin, Operations, Sales, Account
- Admin can assign:
  - `can_edit`
  - `can_delete`

---

## 🔄 API Overview

Base URL: `/api/`

Common Endpoints:
```
/register/                   # Register user
/token/                      # Login
/token/refresh/              # Refresh token
/employees/                  # Employee management
/sales/, /purchase/, /transport/, /inventory/
/generate-pdf/, /export-excel/, /send-email/
```

---

## 📄 Features

- User registration & JWT auth
- Role-based access control
- Create/View/Update/Delete:
  - Sales, Purchases, Inventory
- Transportation costs included in invoice total
- PDF invoice generation (with logo, signature space)
- Export to Excel and CSV
- Email invoices to clients

---

## 🚦 Common Issues

- Email not sending: Check `EMAIL_HOST_USER` and App Password
- File not generating: Make sure media directory exists
- Role not applied: Admin must assign user role manually

---

## 🧪 Testing

- Use Postman for testing JWT endpoints
- Test PDF generation via `/generate-pdf/` with invoice number
- Validate export via `/export-excel/` with filters

---

## 🚀 Deployment Notes

1. Switch to PostgreSQL (update `DATABASES` in settings)
2. Set `DEBUG=False`
3. Use environment variables securely
4. Host media files using AWS S3 or cloud storage
5. Use Gunicorn + Nginx for production

Recommended platforms:
- Railway
- Render
- DigitalOcean

---

## 🧠 Developer Notes

- Extend user logic in `core/models.py`
- Override permissions per ViewSet
- Customize templates for PDF branding
- Use Django signals for post-save triggers (optional)

