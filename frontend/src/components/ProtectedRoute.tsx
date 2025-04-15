import { Navigate, Outlet } from "react-router-dom";
import { getUserRole, isAuthenticated } from "../utils/auth";

interface ProtectedRouteProps {
  allowedRoles: string[];
  children?: React.ReactNode;
}

const ProtectedRoute = ({ allowedRoles, children }: ProtectedRouteProps) => {
  const role = getUserRole();

  if (!isAuthenticated()) {
    return <Navigate to="/" replace />;
  }

  if (!role || !allowedRoles.includes(role)) {
    return (
      <div className="p-6 text-center">
        <h1 className="text-2xl font-semibold text-red-500">403 - Unauthorized</h1>
        <p className="text-gray-600 mt-2">You do not have permission to view this page.</p>
      </div>
    );
  }

  return children || <Outlet />;
};

export default ProtectedRoute;
