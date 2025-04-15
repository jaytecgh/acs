import { useEffect, useState } from "react";
import axios from "axios";

interface DashboardStats {
  total_sales: number;
  total_purchases: number;
  total_expenses: number;
  inventory_count: number;
}

const Dashboard = () => {
  const [stats, setStats] = useState<DashboardStats | null>(null);

  useEffect(() => {
    const fetchStats = async () => {
      const token = localStorage.getItem("access_token");
      try {
        const res = await axios.get("http://127.0.0.1:8000/dashboard/", {
          headers: {
            Authorization: `Bearer ${token}`
          }
        });
        setStats(res.data);
      } catch (err) {
        console.error("Failed to load dashboard stats", err);
      }
    };

    fetchStats();
  }, []);

  return (
    <div className="bg-[#F8F8F8] dark:bg-[#0f172a] min-h-screen p-6">
      <h1 className="text-3xl font-bold text-[#1D1D1D] dark:text-white">Dashboard</h1>

      {/* Stats Cards */}
      <div className="grid grid-cols-4 gap-6 mt-6">
        <div className="bg-white dark:bg-[#1F2937] p-6 rounded-lg shadow-md">
          <h2 className="text-xl font-semibold text-gray-800 dark:text-white">₵{stats?.total_purchases ?? 0}</h2>
          <p className="text-gray-500 dark:text-gray-300">Total Purchases</p>
        </div>
        <div className="bg-white dark:bg-[#1F2937] p-6 rounded-lg shadow-md">
          <h2 className="text-xl font-semibold text-gray-800 dark:text-white">₵{stats?.total_expenses ?? 0}</h2>
          <p className="text-gray-500 dark:text-gray-300">Total Expenses</p>
        </div>
        <div className="bg-white dark:bg-[#1F2937] p-6 rounded-lg shadow-md">
          <h2 className="text-xl font-semibold text-gray-800 dark:text-white">₵{stats?.total_sales ?? 0}</h2>
          <p className="text-gray-500 dark:text-gray-300">Total Sales</p>
        </div>
        <div className="bg-white dark:bg-[#1F2937] p-6 rounded-lg shadow-md">
          <h2 className="text-xl font-semibold text-gray-800 dark:text-white">{stats?.inventory_count ?? 0}</h2>
          <p className="text-gray-500 dark:text-gray-300">Inventory Items</p>
        </div>
      </div>

      {/* Revenue & Customer Satisfaction */}
      <div className="grid grid-cols-2 gap-6 mt-6">
        <div className="bg-white dark:bg-[#1F2937] p-6 rounded-lg shadow-md">
          <h2 className="text-lg font-semibold text-gray-800 dark:text-white">Total Revenue</h2>
          <div className="h-40 bg-gray-200 dark:bg-gray-700 rounded mt-4 flex items-center justify-center">
            <span className="text-gray-500 dark:text-gray-300">Chart Placeholder</span>
          </div>
        </div>
        <div className="bg-white dark:bg-[#1F2937] p-6 rounded-lg shadow-md">
          <h2 className="text-lg font-semibold text-gray-800 dark:text-white">Customer Satisfaction</h2>
          <div className="h-40 bg-gray-200 dark:bg-gray-700 rounded mt-4 flex items-center justify-center">
            <span className="text-gray-500 dark:text-gray-300">Chart Placeholder</span>
          </div>
        </div>
      </div>

      {/* Purchase & Sales History */}
      <div className="grid grid-cols-2 gap-6 mt-6">
        <div className="bg-white dark:bg-[#1F2937] p-6 rounded-lg shadow-md">
          <h2 className="text-lg font-semibold text-gray-800 dark:text-white">Purchase History</h2>
          <p className="text-gray-500 dark:text-gray-300">Table data will go here...</p>
        </div>
        <div className="bg-white dark:bg-[#1F2937] p-6 rounded-lg shadow-md">
          <h2 className="text-lg font-semibold text-gray-800 dark:text-white">Sales History</h2>
          <p className="text-gray-500 dark:text-gray-300">Table data will go here...</p>
        </div>
      </div>

      {/* Product Summary */}
      <div className="mt-4 w-full bg-white dark:bg-[#1F2937] shadow rounded-lg p-4">
        <h2 className="text-lg font-semibold mb-4 text-gray-800 dark:text-white">Product Summary</h2>
        <div className="overflow-x-auto">
          <table className="min-w-full table-auto">
            <thead>
              <tr className="bg-gray-100 dark:bg-gray-700 text-left text-sm font-medium text-gray-700 dark:text-gray-200">
                <th className="px-4 py-2">Product</th>
                <th className="px-4 py-2">Total Purchased</th>
                <th className="px-4 py-2">Total Sold</th>
                <th className="px-4 py-2">Balance</th>
              </tr>
            </thead>
            <tbody className="text-sm divide-y divide-gray-200 dark:divide-gray-600">
              <tr className="text-gray-800 dark:text-gray-100">
                <td className="px-4 py-2">Sikaceram 80 - 20KG</td>
                <td className="px-4 py-2">100</td>
                <td className="px-4 py-2">60</td>
                <td className="px-4 py-2">40</td>
              </tr>
              <tr className="text-gray-800 dark:text-gray-100">
                <td className="px-4 py-2">Sikaceram 103 - 20KG</td>
                <td className="px-4 py-2">500</td>
                <td className="px-4 py-2">300</td>
                <td className="px-4 py-2">200</td>
              </tr>
              <tr className="text-gray-800 dark:text-gray-100">
                <td className="px-4 py-2">Sikaceram 203 - 20KG</td>
                <td className="px-4 py-2">500</td>
                <td className="px-4 py-2">300</td>
                <td className="px-4 py-2">200</td>
              </tr>
              <tr className="text-gray-800 dark:text-gray-100">
                <td className="px-4 py-2">Super Sikalite - 1KG</td>
                <td className="px-4 py-2">500</td>
                <td className="px-4 py-2">300</td>
                <td className="px-4 py-2">200</td>
              </tr>
              <tr className="text-gray-800 dark:text-gray-100">
                <td className="px-4 py-2">Sikalatex - 20KG</td>
                <td className="px-4 py-2">500</td>
                <td className="px-4 py-2">300</td>
                <td className="px-4 py-2">200</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
