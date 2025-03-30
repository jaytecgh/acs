# Project Setup Guide

## Step 1: Install Node.js
Node.js is required to run the frontend development environment.

### Installation:
1. Download the latest **LTS** version of Node.js from [Node.js Official Website](https://nodejs.org/)
2. Install Node.js following the on-screen instructions.
3. Verify installation by running the following command:
   ```sh
   node -v
   npm -v
   ```
   If both commands return version numbers, Node.js and npm (Node Package Manager) are installed successfully.

## Step 2: Set Up React with Vite
Vite is a fast build tool that enhances React development.

### Installation:
1. Open a terminal and navigate to the desired project directory.
2. Run the following command to create a new Vite project:
   ```sh
   npm create vite@latest my-inventory-app --template react-ts
   ```
3. Navigate into the project folder:
   ```sh
   cd my-inventory-app
   ```
4. Install dependencies:
   ```sh
   npm install
   ```
5. Start the development server:
   ```sh
   npm run dev
   ```
   This should start the local development server and provide a URL to preview the project.

## Step 3: Install Tailwind CSS (Using Vite Plugin)
Tailwind CSS will be used for styling the frontend.

### Installation:
1. Run the following command to install Tailwind CSS with Vite:
   ```sh
   npm install -D tailwindcss @tailwindcss/vite
   ```
2. Initialize Tailwind configuration:
   ```sh
   npx tailwindcss init -p
   ```
3. Configure `vite.config.ts`:
   ```ts
   import { defineConfig } from 'vite';
   import tailwindcss from '@tailwindcss/vite';

   export default defineConfig({
     plugins: [
       tailwindcss(),
     ],
   });
   ```
4. Configure `tailwind.config.js`:
   ```js
   /** @type {import('tailwindcss').Config} */
   export default {
     content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
     theme: {
       extend: {},
     },
     plugins: [],
   };
   ```
5. Add Tailwind directives to `src/index.css`:
   ```css
   @tailwind base;
   @tailwind components;
   @tailwind utilities;
   ```
6. Restart the development server:
   ```sh
   npm run dev
   ```

## Step 4: Set Up Axios for API Requests
Axios is a promise-based HTTP client for making API requests.

### Installation:
1. Install Axios using npm:
   ```sh
   npm install axios
   ```

### Usage:
1. Create an `api.ts` file inside `src/utils/`:
   ```ts
   import axios from 'axios';

   const API_BASE_URL = 'http://localhost:8000/api'; // Update with your backend URL

   export const apiClient = axios.create({
     baseURL: API_BASE_URL,
     headers: {
       'Content-Type': 'application/json',
     },
   });
   ```

## Step 5: Configure React Router
React Router will be used for handling navigation between different pages.

### Installation:
1. Install React Router:
   ```sh
   npm install react-router-dom
   ```

## Step 6: Implement User Roles and Permissions
User roles and permissions will be used to control access to different sections of the system.

### Define User Roles:
1. Update the authentication utility (`auth.ts`) to store user roles:
   ```ts
   import jwtDecode from 'jwt-decode';

   export const getUserRole = (): string | null => {
     const token = getToken();
     if (!token) return null;
     const decoded: any = jwtDecode(token);
     return decoded.role || null;
   };
   ```

2. Create a `RoleBasedRoute.tsx` component inside `src/components/`:
   ```tsx
   import { Navigate, Outlet } from 'react-router-dom';
   import { getUserRole } from '../utils/auth';

   interface RoleBasedRouteProps {
     allowedRoles: string[];
   }

   const RoleBasedRoute = ({ allowedRoles }: RoleBasedRouteProps) => {
     const userRole = getUserRole();
     return userRole && allowedRoles.includes(userRole) ? <Outlet /> : <Navigate to="/" />;
   };

   export default RoleBasedRoute;
   ```

3. Update `Router.tsx` to use `RoleBasedRoute`:
   ```tsx
   import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
   import Home from '../pages/Home';
   import Dashboard from '../pages/Dashboard';
   import AdminPanel from '../pages/AdminPanel';
   import RoleBasedRoute from '../components/RoleBasedRoute';

   const AppRouter = () => {
     return (
       <Router>
         <Routes>
           <Route path="/" element={<Home />} />
           <Route element={<RoleBasedRoute allowedRoles={["admin"]} />}>
             <Route path="/admin" element={<AdminPanel />} />
           </Route>
           <Route path="/dashboard" element={<Dashboard />} />
         </Routes>
       </Router>
     );
   };

   export default AppRouter;
   ```

## Step 7: Enhance UI with Dashboard Components
To improve user experience, we will create a visually appealing dashboard.

### Install UI Components:
1. Install a UI library like **ShadCN** for modern components:
   ```sh
   npm install @shadcn/ui
   ```

### Create Dashboard Layout:
1. Create `Dashboard.tsx` with widgets:
   ```tsx
   import React from 'react';
   import { Card, CardContent } from '@/components/ui/card';

   const Dashboard = () => {
     return (
       <div className="p-6 grid grid-cols-3 gap-4">
         <Card><CardContent>Inventory Stats</CardContent></Card>
         <Card><CardContent>Sales Reports</CardContent></Card>
         <Card><CardContent>User Activity</CardContent></Card>
       </div>
     );
   };

   export default Dashboard;
   ```

## Next Steps:
- Implement advanced reporting
- Add notifications and alerts

### More steps will be added as we proceed.











/*@import "tailwindcss";

:root {
  font-family: system-ui, Avenir, Helvetica, Arial, sans-serif;
  line-height: 1.5;
  font-weight: 400;

  color-scheme: light dark;
  color: rgba(255, 255, 255, 0.87);
  background-color: #242424;

  font-synthesis: none;
  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

a {
  font-weight: 500;
  color: #646cff;
  text-decoration: inherit;
}
a:hover {
  color: #535bf2;
}

body {
  margin: 0;
  display: flex;
  place-items: center;
  min-width: 320px;
  min-height: 100vh;
}

h1 {
  font-size: 3.2em;
  line-height: 1.1;
}

button {
  border-radius: 8px;
  border: 1px solid transparent;
  padding: 0.6em 1.2em;
  font-size: 1em;
  font-weight: 500;
  font-family: inherit;
  background-color: #1a1a1a;
  cursor: pointer;
  transition: border-color 0.25s;
}
button:hover {
  border-color: #646cff;
}
button:focus,
button:focus-visible {
  outline: 4px auto -webkit-focus-ring-color;
}

@media (prefers-color-scheme: light) {
  :root {
    color: #213547;
    background-color: #ffffff;
  }
  a:hover {
    color: #747bff;
  }
  button {
    background-color: #f9f9f9;
  }
}
*/