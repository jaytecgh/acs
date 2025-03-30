import { Routes, Route } from "react-router-dom";
import Home from "../pages/Home";
import Dashboard from "../pages/Dashboard";
import Clients from "../pages/Clients";
import Inventory from "../pages/Inventory";
import AdminPanel from "../pages/AdminPanel";
import RoleBasedRoute from "../components/RoleBasedRoute";
import MainLayout from "../layouts/MainLayout";

const AppRouter = () => {
  return (
    <Routes>
      <Route path="/" element={<Home />} />

      <Route element={<MainLayout />}>
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/clients" element={<Clients />} />
        <Route path="/inventory" element={<Inventory />} />
        <Route path="/settings" element={<div>Settings Page</div>} />
        <Route path="/reports" element={<div>Reports Page</div>} />

        {/* Admin protected route */}
        <Route element={<RoleBasedRoute allowedRoles={["admin"]} />}>
          <Route path="/admin" element={<AdminPanel />} />
        </Route>
      </Route>
    </Routes>
  );
};

export default AppRouter;
