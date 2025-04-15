import { useEffect, useState } from "react";
import { apiClient } from "../../utils/api";

interface UserData {
  id: number;
  full_name: string;
  role: string;
  can_edit: boolean;
  can_delete: boolean;
  user: {
    id: number;
    username: string;
    email: string;
    is_active: boolean;
    is_staff: boolean;
  };
}

const AdminPanel = () => {
  const [users, setUsers] = useState<UserData[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    fetchUsers();
  }, []);

  const fetchUsers = async () => {
    try {
      const res = await apiClient.get("/employees/");
      setUsers(res.data);
    } catch (err) {
      setError("Failed to load users.");
    } finally {
      setLoading(false);
    }
  };

  const updateUser = async (id: number, updated: Partial<UserData>) => {
    try {
      await apiClient.patch(`/employees/${id}/`, updated);
      fetchUsers();
    } catch (err) {
      alert("Update failed");
    }
  };

  const handleChange = (id: number, key: keyof UserData, value: any) => {
    const updatedUsers = users.map((u) =>
      u.id === id ? { ...u, [key]: value } : u
    );
    setUsers(updatedUsers);
  };

  if (loading) return <p className="p-4">Loading...</p>;
  if (error) return <p className="p-4 text-red-600">{error}</p>;

  return (
    <div className="p-6">
      <h2 className="text-2xl font-bold mb-4">Admin User Management</h2>
      <table className="w-full border-collapse border border-gray-300">
        <thead className="bg-gray-100 dark:bg-gray-700">
          <tr>
            <th className="p-2 border">Full Name</th>
            <th className="p-2 border">Username</th>
            <th className="p-2 border">Email</th>
            <th className="p-2 border">Role</th>
            <th className="p-2 border">Can Edit</th>
            <th className="p-2 border">Can Delete</th>
            <th className="p-2 border">Actions</th>
          </tr>
        </thead>
        <tbody>
          {users.map((user) => (
            <tr key={user.id}>
              <td className="p-2 border">{user.full_name}</td>
              <td className="p-2 border">{user.user.username}</td>
              <td className="p-2 border">{user.user.email}</td>
              <td className="p-2 border">
                <select
                  value={user.role}
                  onChange={(e) => handleChange(user.id, "role", e.target.value)}
                  className="p-1 border rounded"
                >
                  <option value="admin">Admin</option>
                  <option value="operations">Operations</option>
                  <option value="sales">Sales</option>
                  <option value="account">Account</option>
                </select>
              </td>
              <td className="p-2 border text-center">
                <input
                  type="checkbox"
                  checked={user.can_edit}
                  onChange={(e) => handleChange(user.id, "can_edit", e.target.checked)}
                />
              </td>
              <td className="p-2 border text-center">
                <input
                  type="checkbox"
                  checked={user.can_delete}
                  onChange={(e) => handleChange(user.id, "can_delete", e.target.checked)}
                />
              </td>
              <td className="p-2 border">
                <button
                  onClick={() => updateUser(user.id, {
                    role: user.role,
                    can_edit: user.can_edit,
                    can_delete: user.can_delete,
                  })}
                  className="bg-yellow-600 text-white px-3 py-1 rounded hover:bg-yellow-700"
                >
                  Save
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default AdminPanel;
