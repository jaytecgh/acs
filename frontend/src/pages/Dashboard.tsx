
const Dashboard = () => {
  return (
    <div className="bg-[#F8F8F8] min-h-screen p-6">
      <h1 className="text-3xl font-bold text-[#1D1D1D]">Dashboard</h1>

      {/* Stats Cards */}
      <div className="grid grid-cols-4 gap-6 mt-6">
        <div className="bg-white p-6 rounded-lg shadow-md">
          <h2 className="text-xl font-semibold">$1k</h2>
          <p className="text-gray-500">Total Purchases</p>
        </div>
        <div className="bg-white p-6 rounded-lg shadow-md">
          <h2 className="text-xl font-semibold">300</h2>
          <p className="text-gray-500">Payables</p>
        </div>
        <div className="bg-white p-6 rounded-lg shadow-md">
          <h2 className="text-xl font-semibold">5</h2>
          <p className="text-gray-500">Total Sales</p>
        </div>
        <div className="bg-white p-6 rounded-lg shadow-md">
          <h2 className="text-xl font-semibold">8</h2>
          <p className="text-gray-500">Receivables</p>
        </div>
      </div>

      {/* Revenue & Customer Satisfaction */}
      <div className="grid grid-cols-2 gap-6 mt-6">
        <div className="bg-white p-6 rounded-lg shadow-md">
          <h2 className="text-lg font-semibold">Total Revenue</h2>
          {/* Placeholder Chart */}
          <div className="h-40 bg-gray-200 rounded mt-4 flex items-center justify-center">
            <span className="text-gray-500">Chart Placeholder</span>
          </div>
        </div>
        <div className="bg-white p-6 rounded-lg shadow-md">
          <h2 className="text-lg font-semibold">Customer Satisfaction</h2>
          {/* Placeholder Chart */}
          <div className="h-40 bg-gray-200 rounded mt-4 flex items-center justify-center">
            <span className="text-gray-500">Chart Placeholder</span>
          </div>
        </div>
      </div>

      {/* Purchase & Sales History */}
      <div className="grid grid-cols-2 gap-6 mt-6">
        <div className="bg-white p-6 rounded-lg shadow-md">
          <h2 className="text-lg font-semibold">Purchase History</h2>
          <p className="text-gray-500">Table data will go here...</p>
        </div>
        <div className="bg-white p-6 rounded-lg shadow-md">
          <h2 className="text-lg font-semibold">Sales History</h2>
          <p className="text-gray-500">Table data will go here...</p>
        </div>
      </div>

      {/* Product Summary */}
      <div className="mt-4 w-full bg-white shadow rounded-lg p-4">
        <h2 className="text-lg font-semibold mb-4">Product Summary</h2>
        <div className="overflow-x-auto">
        <table className="min-w-full table-auto">
      <thead>
        <tr className="bg-gray-100 text-left text-sm font-medium">
          <th className="px-4 py-2">Product</th>
          <th className="px-4 py-2">Total Purchased</th>
          <th className="px-4 py-2">Total Sold</th>
          <th className="px-4 py-2">Balance</th>
        </tr>
      </thead>
      <tbody className="text-sm divide-y">
        {/* Replace with dynamic data */}
        <tr>
          <td className="px-4 py-2">Sikaceram 80 - 20KG</td>
          <td className="px-4 py-2">100</td>
          <td className="px-4 py-2">60</td>
          <td className="px-4 py-2">40</td>
        </tr>
        <tr>
          <td className="px-4 py-2">Sikaceram 103 - 20KG</td>
          <td className="px-4 py-2">500</td>
          <td className="px-4 py-2">300</td>
          <td className="px-4 py-2">200</td>
        </tr>
        <tr>
          <td className="px-4 py-2">Sikaceram 203 - 20KG</td>
          <td className="px-4 py-2">500</td>
          <td className="px-4 py-2">300</td>
          <td className="px-4 py-2">200</td>
        </tr>
        <tr>
          <td className="px-4 py-2">Super Sikalite - 1KG</td>
          <td className="px-4 py-2">500</td>
          <td className="px-4 py-2">300</td>
          <td className="px-4 py-2">200</td>
        </tr>
        <tr>
          <td className="px-4 py-2">Sikalatex - 20KG</td>
          <td className="px-4 py-2">500</td>
          <td className="px-4 py-2">300</td>
          <td className="px-4 py-2">200</td>
        </tr>
        {/* Add more rows dynamically */}
      </tbody>
    </table>

        </div>
      </div>

    </div>
  );
};

export default Dashboard;
