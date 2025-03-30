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