import { Outlet } from "react-router-dom";

const SettingsLayout = () => {
  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4 text-gray-800 dark:text-white">Settings</h1>
      <Outlet />
    </div>
  );
};

export default SettingsLayout;
