const AdminPanel = () => {
  return (
    <div className="p-6">
      <h1 className="text-3xl font-bold mb-4">Admin Panel</h1>
      <p>Welcome, Admin! Here you can manage users, inventory, and system settings.</p>
      
      <div className="grid grid-cols-3 gap-4 mt-6">
        <div className="bg-white p-4 shadow rounded-lg">Manage Users</div>
        <div className="bg-white p-4 shadow rounded-lg">View Reports</div>
        <div className="bg-white p-4 shadow rounded-lg">System Settings</div>
      </div>
    </div>
  );
};

export default AdminPanel;
