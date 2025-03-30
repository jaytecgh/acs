import { useState, useEffect } from "react";
import {
  HomeIcon,
  UsersIcon,
  ClipboardDocumentListIcon,
  ChartBarIcon,
  Cog8ToothIcon,
  Bars3Icon,
  XMarkIcon,
  BellIcon,
  MoonIcon,
  SunIcon,
  MagnifyingGlassIcon,
  UserCircleIcon,
} from "@heroicons/react/24/outline";
import { Link, Outlet, useLocation } from "react-router-dom";

const menuItems = [
  { name: "Dashboard", icon: <HomeIcon className="h-6 w-6" />, path: "/dashboard" },
  { name: "Clients", icon: <UsersIcon className="h-6 w-6" />, path: "/clients" },
  { name: "Inventory", icon: <ClipboardDocumentListIcon className="h-6 w-6" />, path: "/inventory" },
  { name: "Reports", icon: <ChartBarIcon className="h-6 w-6" />, path: "/reports" },
  { name: "Settings", icon: <Cog8ToothIcon className="h-6 w-6" />, path: "/settings" },
];

const MainLayout = () => {
  const [collapsed, setCollapsed] = useState(false);
  const [dropdownOpen, setDropdownOpen] = useState(false);
  const [mobileSidebarOpen, setMobileSidebarOpen] = useState(false);
  const [darkMode, setDarkMode] = useState(() => localStorage.getItem("theme") === "dark");
  const location = useLocation();

  // Toggle Dark Mode
  useEffect(() => {
    if (darkMode) {
      document.documentElement.classList.add("dark");
      localStorage.setItem("theme", "dark");
    } else {
      document.documentElement.classList.remove("dark");
      localStorage.setItem("theme", "light");
    }
  }, [darkMode]);

  return (
    <div className={`flex h-screen ${darkMode ? "bg-gray-900 text-white" : "bg-gray-50 text-gray-900"}`}>
      {/* Mobile Sidebar Overlay */}
      {mobileSidebarOpen && (
        <div
          className="fixed inset-0 bg-black opacity-50 z-40 md:hidden"
          onClick={() => setMobileSidebarOpen(false)}
        ></div>
      )}

      {/* Sidebar */}
      <div
        className={`transition-all duration-300 bg-white-800 text-secondary fixed md:relative h-full z-50 
        ${collapsed ? "w-16" : "w-45"} md:block ${mobileSidebarOpen ? "block" : "hidden"}`}
      >
        <div className="flex items-center justify-between p-4">
        <img src="/src/assets/acs-logo.jpg" alt="Construction Supply" className={`h-10 w-auto ${collapsed ? "hidden" : "block"}`} />
          <button
            onClick={() => {
              setCollapsed(!collapsed);
              setMobileSidebarOpen(false);
            }}
            className="text-white md:hidden"
          >
            <XMarkIcon className="w-6 h-6" />
          </button>
        </div>

        <nav className="mt-4 space-y-2">
          {menuItems.map((item) => (
            <Link
              key={item.name}
              to={item.path}
              className={`flex items-center px-4 py-2 hover:bg-gray-700 ${
                location.pathname === item.path ? "bg-gray-700" : ""
              }`}
            >
              {item.icon}
              {!collapsed && <span className="ml-3">{item.name}</span>}
            </Link>
          ))}
        </nav>
      </div>

      {/* Main Content Area */}
      <div className="flex-1 flex flex-col">
        {/* Top Navbar */}
        <div className={`shadow-md p-4 flex items-center justify-between ${darkMode ? "bg-gray-800 text-white" : "bg-white"}`}>
          {/* Mobile Menu Button */}
          <button onClick={() => setMobileSidebarOpen(true)} className="md:hidden">
            <Bars3Icon className="w-6 h-6 text-gray-700 dark:text-white" />
          </button>

          {/* Left - Logo */}
          <div className="text-lg font-bold hidden md:block">Dashboard</div>

          {/* Center - Search Bar */}
          <div className="relative w-1/3 hidden md:block">
            <MagnifyingGlassIcon className="absolute left-2 top-2 w-5 h-5 text-gray-400" />
            <input
              type="text"
              placeholder="Search..."
              className="w-full pl-8 pr-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500 dark:bg-gray-700 dark:text-white"
            />
          </div>

          {/* Right - Dark Mode Toggle, Notifications & Profile */}
          <div className="flex items-center space-x-6">
            {/* Dark Mode Toggle */}
            <button onClick={() => setDarkMode(!darkMode)} className="focus:outline-none">
              {darkMode ? (
                <SunIcon className="w-6 h-6 text-yellow-400" />
              ) : (
                <MoonIcon className="w-6 h-6 text-gray-700 dark:text-white" />
              )}
            </button>

            {/* Notifications */}
            <div className="relative cursor-pointer">
              <BellIcon className="w-6 h-6 text-gray-700 dark:text-white" />
              <span className="absolute -top-2 -right-2 bg-red-600 text-white text-xs rounded-full px-2">3</span>
            </div>

            {/* Profile Dropdown */}
            <div className="relative">
              <button
                onClick={() => setDropdownOpen(!dropdownOpen)}
                className="flex items-center space-x-2 focus:outline-none"
              >
                <UserCircleIcon className="w-8 h-8 text-gray-600 dark:text-white" />
                <span className="hidden md:block">Admin</span>
              </button>

              {/* Dropdown Menu */}
              {dropdownOpen && (
                <div className="absolute right-0 mt-2 w-48 bg-white dark:bg-gray-700 border dark:border-gray-600 rounded-lg shadow-lg">
                  <Link to="/profile" className="block px-4 py-2 text-gray-800 dark:text-white hover:bg-gray-100 dark:hover:bg-gray-600">
                    Profile
                  </Link>
                  <Link to="/settings" className="block px-4 py-2 text-gray-800 dark:text-white hover:bg-gray-100 dark:hover:bg-gray-600">
                    Settings
                  </Link>
                  <button
                    className="w-full text-left px-4 py-2 text-red-600 hover:bg-gray-100 dark:text-red-400 dark:hover:bg-gray-600"
                    onClick={() => alert("Logging out...")}
                  >
                    Logout
                  </button>
                </div>
              )}
            </div>
          </div>
        </div>

        {/* Page Content */}
        <div className="p-6 flex-1 overflow-y-auto">
          <Outlet />
        </div>
      </div>
    </div>
  );
};

export default MainLayout;
