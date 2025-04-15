import { useState, useEffect } from "react";
import {
  HomeIcon,
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
  TruckIcon,
  BanknotesIcon,
  BuildingStorefrontIcon,
  ClipboardIcon,
  ChevronDownIcon,
  ChevronRightIcon,
} from "@heroicons/react/24/outline";
import { Link, Outlet, useLocation, useNavigate } from "react-router-dom";
import LightLogo from "../assets/acs-logo.png";
import DarkLogo from "../assets/acs-logo.jpg";

const user = JSON.parse(localStorage.getItem("user") || "{}");
const role = user?.employee?.role;

const menuItems = [
  { name: "Dashboard", icon: <HomeIcon className="h-6 w-6" />, path: "/dashboard" },
  { name: "Products", icon: <ClipboardDocumentListIcon className="h-6 w-6" />, path: "", children: [
    { name: "| Product", path: "/products" },
    { name: "| Inventory", path: "/inventory" },
  ]},
  { name: "Invoices", icon: <ClipboardIcon className="h-6 w-6" />, path: "", children: [
    { name: "| Purchases", path: "/purchases" },
    { name: "| Sales", path: "/sales" },
  ]},
  { name: "Services", icon: <BuildingStorefrontIcon className="h-6 w-6" />, path: "", children: [
    { name: "| Suppliers", path: "/suppliers" },
    { name: "| Clients", path: "/clients" },
    { name: "| Employees", path: "/employees" },
  ]},
  { name: "Expenses", icon: <BanknotesIcon className="h-6 w-6" />, path: "", children: [
    { name: "| Payments", path: "/payments" },
    { name: "| Expenses", path: "/expenses" },
  ]},
  { name: "Transport", icon: <TruckIcon className="h-6 w-6" />, path: "/transport" },
  { name: "Reports", icon: <ChartBarIcon className="h-6 w-6" />, path: "/reports" },
  {
    name: "Settings",
    icon: <Cog8ToothIcon className="h-6 w-6" />,
    path: "/settings",
    children: [
      { name: "| Profile", path: "/settings/profile" },
      ...(role === "admin"
        ? [{ name: "| Admin Panel", path: "/settings/admin" }]
        : [])
    ]
  }
  
];



const MainLayout = () => {
  const [collapsed, setCollapsed] = useState(false);
  const [dropdownOpen, setDropdownOpen] = useState(false);
  const [mobileSidebarOpen, setMobileSidebarOpen] = useState(false);
  const [darkMode, setDarkMode] = useState(() => localStorage.getItem("theme") === "dark");
  const [openMenus, setOpenMenus] = useState<{ [key: number]: boolean }>({});
  const location = useLocation();
  const navigate = useNavigate();

  useEffect(() => {
    if (darkMode) {
      document.documentElement.classList.add("dark");
      localStorage.setItem("theme", "dark");
    } else {
      document.documentElement.classList.remove("dark");
      localStorage.setItem("theme", "light");
    }
  }, [darkMode]);

  const toggleMenu = (index: number) => {
    setOpenMenus((prev) => ({ ...prev, [index]: !prev[index] }));
  };

  const handleItemClick = (item: any, index: number) => {
    if (item.children) {
      toggleMenu(index);
    } else if (item.path) {
      navigate(item.path);
    }
  };

  return (
    <div className={`flex h-screen transition-colors duration-300 ${darkMode ? "bg-gray-900 text-white" : "bg-gray-100 text-gray-900"}`}>
      {mobileSidebarOpen && (
        <div className="fixed inset-0 bg-black opacity-50 z-40 md:hidden" onClick={() => setMobileSidebarOpen(false)}></div>
      )}

      <div className={`transition-all duration-300 bg-white dark:bg-gray-800 text-gray-800 dark:text-white fixed md:relative h-full z-50 ${collapsed ? "w-20" : "w-64"} md:block ${mobileSidebarOpen ? "block" : "hidden"}`}>
        <div className="flex items-center justify-between p-4">
          <img src={darkMode ? DarkLogo : LightLogo} alt="Construction Supply" className="h-10 w-auto" />
          <button onClick={() => setCollapsed(!collapsed)} className="text-gray-600 dark:text-white md:hidden">
            <XMarkIcon className="w-6 h-6" />
          </button>
        </div>

        <nav className="mt-4 space-y-1">
          {menuItems.map((item, index) => (
            <div key={index}>
              <button
                onClick={() => handleItemClick(item, index)}
                className={`w-full flex items-center justify-between px-3 py-3 hover:bg-yellow-500 hover:text-white rounded transition-colors ${location.pathname === item.path ? "bg-yellow-500 text-white font-semibold" : ""}`}
              >
                <div className="flex items-center space-x-3">
                  {item.icon}
                  {!collapsed && <span>{item.name}</span>}
                </div>
                {item.children && !collapsed && (
                  openMenus[index] ? <ChevronDownIcon className="h-4 w-4" /> : <ChevronRightIcon className="h-4 w-4" />
                )}
              </button>
              {!collapsed && item.children && openMenus[index] && (
                <div className="ml-10 space-y-1">
                  {item.children.map((sub) => (
                    <Link
                      key={sub.name}
                      to={sub.path}
                      className={`block text-sm text-gray-800 dark:text-gray-300 hover:text-yellow-500 ${location.pathname === sub.path ? "text-yellow-500 font-semibold" : ""}`}
                    >
                      {sub.name}
                    </Link>
                  ))}
                </div>
              )}
            </div>
          ))}
        </nav>
      </div>

      <div className="flex-1 flex flex-col">
        <div className={`p-4 shadow-md flex items-center justify-between ${darkMode ? "bg-gray-800 text-white" : "bg-white text-gray-900"}`}>
          <button onClick={() => setMobileSidebarOpen(true)} className="md:hidden">
            <Bars3Icon className="w-6 h-6" />
          </button>

          <div className="text-lg font-bold hidden md:block text-gray-600 dark:text-white">Dashboard</div>

          <div className="relative w-1/3 hidden md:block">
            <MagnifyingGlassIcon className="absolute left-3 top-2.5 w-5 h-5 text-yellow-600" />
            <input
              type="text"
              placeholder="Search..."
              className="w-full pl-10 pr-4 py-2 border border-yellow-600 rounded-md focus:outline-none focus:ring-2 focus:ring-yellow-600 dark:bg-gray-700 dark:text-white"
            />
          </div>

          <div className="flex items-center space-x-4">
            <button onClick={() => setDarkMode(!darkMode)} className="focus:outline-none">
              {darkMode ? <SunIcon className="w-6 h-6 text-yellow-400" /> : <MoonIcon className="w-6 h-6 text-gray-700" />}
            </button>

            <div className="relative cursor-pointer">
              <BellIcon className="w-6 h-6" />
              <span className="absolute -top-2 -right-2 bg-red-600 text-white text-xs rounded-full px-2">3</span>
            </div>

            <div className="relative">
              <button onClick={() => setDropdownOpen(!dropdownOpen)} className="flex items-center space-x-2 focus:outline-none">
                <UserCircleIcon className="w-8 h-8" />
                <span className="hidden md:block">Admin</span>
              </button>
              {dropdownOpen && (
                <div className="absolute right-0 mt-2 w-48 bg-white dark:bg-yellow-700 border rounded-lg shadow-lg">
                  <Link to="/profile" className="block px-4 py-2 hover:bg-gray-100 dark:text-white hover:bg-yellow-600 rounded">Profile</Link>
                  <Link to="/settings/admin" className="block px-4 py-2 hover:bg-gray-100 dark:text-white hover:bg-yellow-600 rounded">Settings</Link>
                  <button
                    className="w-full text-left px-4 py-2 text-red-600 dark:text-red-400 hover:bg-gray-100 dark:hover:bg-gray-600"
                    onClick={() => alert("Logging out...")}
                  >
                    Logout
                  </button>
                </div>
              )}
            </div>
          </div>
        </div>

        <div className="p-6 flex-1 overflow-y-auto">
          <Outlet />
        </div>
      </div>
    </div>
  );
};

export default MainLayout;
