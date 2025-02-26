import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import API from "../utils/api"; // Your API handler

function Login() {
  const [formData, setFormData] = useState({ email: "", password: "" });
  const [error, setError] = useState(null);
  const navigate = useNavigate();

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await API.post("/login", formData);
      sessionStorage.setItem("access_token", response.data.access_token);
      navigate("/dashboard"); // Redirect after login
    } catch {
      setError("Đăng nhập không thành công. Vui lòng thử lại.");
    }
  };

  return (
    <div className="flex justify-center items-center min-h-screen bg-blue-200">
      <div className="w-full max-w-4xl flex bg-white rounded-lg shadow-lg overflow-hidden">
        
        {/* Left Side - Welcome Message */}
        <div className="w-1/2 bg-gradient-to-r from-blue-500 to-blue-600 text-white flex flex-col justify-center items-center p-10">
          <h2 className="text-3xl font-bold">WELCOME BACK</h2>
          <p className="text-sm text-center mt-3">
            Hãy đăng nhập để tiếp tục trải nghiệm các dịch vụ sức khỏe tuyệt vời!
          </p>
        </div>

        {/* Right Side - Login Form */}
        <div className="w-1/2 p-10">
          <h2 className="text-2xl font-bold text-center mb-6">Đăng Nhập</h2>

          {error && <p className="text-red-500 text-center mb-4">{error}</p>}

          <form onSubmit={handleSubmit} className="space-y-4">
            <div>
              <label className="block text-sm font-medium">Email</label>
              <input
                type="email"
                name="email"
                value={formData.email}
                onChange={handleChange}
                required
                className="w-full p-2 mt-1 border rounded-lg"
              />
            </div>

            <div>
              <label className="block text-sm font-medium">Mật khẩu</label>
              <input
                type="password"
                name="password"
                value={formData.password}
                onChange={handleChange}
                required
                className="w-full p-2 mt-1 border rounded-lg"
              />
            </div>

            <div className="flex items-center justify-between">
              <label className="flex items-center">
                <input type="checkbox" className="mr-2" />
                Ghi nhớ đăng nhập
              </label>
              <a href="#" className="text-blue-500 text-sm">Quên mật khẩu?</a>
            </div>

            <button
              type="submit"
              className="w-full py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600"
            >
              Đăng nhập
            </button>
          </form>

          <p className="text-center text-sm mt-4">
            Chưa có tài khoản?{" "}
            <button onClick={() => navigate("/register")} className="text-blue-500">
              Đăng ký ngay!
            </button>
          </p>
        </div>
      </div>
    </div>
  );
}

export default Login;
