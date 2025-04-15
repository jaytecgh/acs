import { Routes, Route } from "react-router-dom";
import Home from "../pages/Home";
import MainLayout from "../layouts/MainLayout";
import Dashboard from "../pages/Dashboard";
import Clients from "../pages/Clients";
import Inventory from "../pages/Inventory";
import Products from "../pages/Products";
import ProtectedRoute from "../components/ProtectedRoute";
import Reports from "../pages/Reports";
import Supplier from "../pages/Supplier";
import Sales from "../pages/Sales";
import Purchases from "../pages/Purchases";
import AdminPanel from "../pages/settings/AdminPanel";
import ForgotPasswordPage from "../pages/ForgotPasswordPage";
import ResetPasswordPage from "../pages/ResetPasswordPage";
import PendingApproval from "../pages/PendingApproval";

import SettingsLayout from "../pages/settings/SettingsLayout";
import Profile from "../pages/settings/Profile";

const AppRouter = () => {
  return (
    <Routes>
      {/* Public Routes */}
      <Route path="/" element={<Home />} />
      <Route path="/forgot-password" element={<ForgotPasswordPage />} />
      <Route path="/reset-password/:token" element={<ResetPasswordPage />} />

      {/* Protected Routes inside layout */}
      <Route element={<MainLayout />}>
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/products" element={<Products />} />
        <Route path="/clients" element={<Clients />} />
        <Route path="/supplier" element={<Supplier />} />
        <Route path="/sales" element={<Sales />} />
        <Route path="/purchases" element={<Purchases />} />
        <Route path="/inventory" element={<Inventory />} />
        <Route path="/reports" element={<Reports />} />
        <Route path="/pending-approval" element={<PendingApproval />} />

        {/* Settings Nested Routes */}
        <Route path="/settings" element={<SettingsLayout />}>
          <Route index element={<Profile />} />
          <Route path="profile" element={<Profile />} />
          <Route
            path="admin"
            element={
              <ProtectedRoute allowedRoles={["admin"]}>
                <AdminPanel />
              </ProtectedRoute>
            }
          />
        </Route>
      </Route>
    </Routes>
  );
};

export default AppRouter;
