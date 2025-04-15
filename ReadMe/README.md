# JayTec Inventory & Invoicing System

A full-stack inventory, sales, and financial management system tailored for businesses. Built using:

- **Frontend:** React (Vite) + TypeScript + TailwindCSS
- **Backend:** Django + Django REST Framework + JWT
- **Authentication:** JWT with role-based access
- **PDF & Excel Support**: ReportLab & Pandas

---

## 📦 Project Structure

```
acs/
├── frontend/      # React + Vite client
├── backend/       # Django + DRF server
├── virtual/       # Python virtual environment (excluded via .gitignore)
└── .gitignore
```

---

## ⚙️ Quick Start

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/acs.git
   cd acs
   ```

2. Set up the backend and frontend by following their respective `README.md` files.

3. Make sure you:
   - Activate the virtual environment
   - Install Node + npm
   - Set up `.env` files in both frontend and backend

---

## 🚀 Getting Started

- Run backend first:
  ```bash
  cd backend
  source ../virtual/Scripts/activate
  python manage.py runserver
  ```

- Run frontend:
  ```bash
  cd frontend
  npm run dev
  ```

---

## 🧠 Tip for Devs

- Always create new features in a new branch.
- Pull from `main` regularly to avoid conflicts.
- Use Postman or Swagger to test APIs during integration.

See `frontend/README.md` and `backend/README.md` for full guides.
