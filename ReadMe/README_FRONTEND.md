# Frontend - JayTec Inventory & Invoicing System

This is the **React-based frontend** for the JayTec Inventory & Invoicing System. It's designed for speed, responsiveness, and secure role-based interaction with the backend API.

---

## 🎯 Project Goals

- Allow role-based access to inventory, sales, purchases, and financial reports
- Generate PDF invoices and export data to Excel
- Enable Admin to assign roles and permissions to users
- Provide a user-friendly dashboard and UI for business staff

---

## ⚙️ Technologies Used

- **React + Vite**
- **TypeScript**
- **Tailwind CSS v4**
- **Axios** for HTTP requests
- **React Router DOM**
- **JWT (JSON Web Tokens)** for secure session handling

---

## 🛠️ Installation & Setup

1. Navigate into the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Create a `.env` file in the root of `frontend/`:
   ```env
   VITE_API_BASE_URL=http://127.0.0.1:8000/api
   ```

4. Start the development server:
   ```bash
   npm run dev
   ```

---

## 🧩 Folder Structure

```
src/
├── auth/             # Login, register, forgot/reset password
├── components/       # UI components (Sidebar, Cards, Charts, etc.)
├── layouts/          # Dashboard layouts (AdminPanel, Settings)
├── pages/            # Page-level components
├── utils/            # Axios config and helper functions
├── routes.tsx        # App routing
├── main.tsx          # Entry point
```

---

## 🔐 Authentication & Roles

- Users log in using email and password
- JWT tokens are stored securely
- Role-based protection:
  - Admin: Full access
  - Operations: Reports, Inventory, Products
  - Sales: Sales only
  - Account: Payments & Expenses

---

## ✅ Features

- Login, Register, Forgot Password, Reset
- Admin Panel: User and role assignment
- Invoices: PDF download, Excel export
- Sidebar navigation with collapsible behavior
- Secure routing based on role
- Dark mode support (optional)
- Dashboard stats and charts

---

## 🚦 Common Issues

- `401 Unauthorized`: Token expired or user role not assigned
- Styling not working: Check Tailwind installation
- Axios errors: Confirm `VITE_API_BASE_URL` is correct

---

## 📦 Deployment

To deploy with **Vercel** or **Netlify**:

1. Build the app:
   ```bash
   npm run build
   ```

2. Upload the `/dist` folder or link the GitHub repo

3. Set environment variable `VITE_API_BASE_URL` on the deployment platform

---

## 👨‍💻 Developer Notes

- Use `src/utils/api.ts` for all API interactions
- Use role context to guard routes and show/hide components
- Test API endpoints using Postman before full integration

