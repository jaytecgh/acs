import { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import { login, register } from "../utils/auth";

const AuthPage = () => {
  const [mode, setMode] = useState<"login" | "register">("login");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [fullName, setFullName] = useState("");
  const [rememberMe, setRememberMe] = useState(false);
  const [error, setError] = useState("");
  const navigate = useNavigate();

  const clearForm = () => {
    setEmail("");
    setPassword("");
    setConfirmPassword("");
    setError("");
  };

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await login(email, password);
      const userData = JSON.parse(localStorage.getItem("user") || "{}");

      if (!userData.role) {
        navigate("/pending-approval");
      } else {
        navigate("/dashboard");
      }
    } catch (err) {
      setError("Invalid credentials! Please try again.");
    }
  };

  const handleRegister = async (e: React.FormEvent) => {
    e.preventDefault();
    if (password !== confirmPassword) {
      setError("Passwords do not match.");
      return;
    }

    try {
      await register(email, password, fullName);
      alert("Account created! Awaiting admin approval.");
      setMode("login");
      clearForm();
    } catch (err) {
      setError("Registration failed. Try a different email.");
    }
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100 px-4">
      <h1 className="text-3xl font-bold mb-2 text-center">Avenue Construction Supply</h1>
      <p className="mb-6 text-gray-600 text-center">Supplying Trust, Building Our Future!</p>

      <div className="bg-white shadow-md rounded-lg p-6 w-full max-w-md">
        {error && <p className="text-red-500 text-center text-sm mb-2">{error}</p>}

        {mode === "login" && (
          <form onSubmit={handleLogin} className="space-y-4">
            <input
              type="email"
              placeholder="Email"
              className="w-full p-2 border border-gray-300 rounded"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />
            <input
              type="password"
              placeholder="Password"
              className="w-full p-2 border border-gray-300 rounded"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
            <div className="flex items-center justify-between">
              <div className="flex items-center">
                <input
                  type="checkbox"
                  checked={rememberMe}
                  onChange={(e) => setRememberMe(e.target.checked)}
                  className="mr-2"
                />
                <label className="text-sm text-gray-600">Remember Me</label>
              </div>
              <Link to="/forgot-password" className="text-sm text-blue-600 hover:underline">
                Forgot Password?
              </Link>
            </div>
            <button type="submit" className="w-full bg-blue-600 text-white p-2 rounded hover:bg-blue-700">
              Login
            </button>
            <p className="text-sm text-center text-gray-600 mt-2">
              Do not have an account?{" "}
              <button
                onClick={() => {
                  setMode("register");
                  clearForm();
                }}
                className="text-blue-600 hover:underline"
              >
                Sign Up
              </button>
            </p>
          </form>
        )}

        {mode === "register" && (
          <form className="space-y-4" onSubmit={handleRegister}>
            <input
              type="text"
              placeholder="Full Name"
              className="w-full p-2 border border-gray-300 rounded"
              value={fullName}
              onChange={(e) => setFullName(e.target.value)}
              required
            />
            <input
              type="email"
              placeholder="Email"
              className="w-full p-2 border border-gray-300 rounded"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />
            <input
              type="password"
              placeholder="Password"
              className="w-full p-2 border border-gray-300 rounded"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
            <input
              type="password"
              placeholder="Confirm Password"
              className="w-full p-2 border border-gray-300 rounded"
              value={confirmPassword}
              onChange={(e) => setConfirmPassword(e.target.value)}
              required
            />
            <button type="submit" className="w-full bg-green-600 text-white p-2 rounded hover:bg-green-700">
              Register
            </button>
            <p className="text-sm text-center text-gray-600 mt-2">
              Already have an account?{" "}
              <button
                onClick={() => {
                  setMode("login");
                  clearForm();
                }}
                className="text-blue-600 hover:underline"
              >
                Login
              </button>
            </p>
          </form>
        )}
      </div>
    </div>
  );
};

export default AuthPage;
