const PendingApproval = () => (
  <div className="min-h-screen flex items-center justify-center bg-gray-100">
    <div className="bg-white p-6 rounded shadow-md text-center max-w-md">
      <h2 className="text-xl font-semibold text-yellow-600 mb-4">Account Pending Approval</h2>
      <p className="text-gray-700">Your registration was successful. Please wait for an administrator to assign a role before you can access the system.</p>
    </div>
  </div>
);

export default PendingApproval;
