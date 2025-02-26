import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import API from "../utils/api"; // Nếu bạn đã tạo file api.js để gọi API
import useAuthStore from "../store/authStore"; // Nếu sử dụng Zustand cho quản lý state

function Register() {
  const navigate = useNavigate();
  const { login } = useAuthStore(); // Lấy hàm login từ authStore để lưu token
  const [formData, setFormData] = useState({
    username: "",
    email: "",
    password: "",
    user_height: "",
    user_weight: "",
    user_age: "",
    sex: "female",
  });

  const [error, setError] = useState(null);

  // Hàm thay đổi giá trị của form
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  // Hàm xử lý khi người dùng submit form
  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      // Gửi yêu cầu đăng ký đến backend
      const response = await API.post("/register", formData);
      
      const { access_token, user } = response.data;

      // Lưu token vào state và sessionStorage
      login(access_token, user);
      
      // Chuyển hướng đến Dashboard sau khi đăng ký thành công
      navigate("/login");
    } catch (error) {
      setError("Đăng ký không thành công. Vui lòng thử lại.");
    }
  };

  return (
    <div className="flex justify-center items-center min-h-screen bg-gray-100">
      <div className="w-full max-w-md bg-white p-8 rounded-lg shadow-lg">
        <h2 className="text-2xl font-semibold text-center mb-6">Đăng Ký</h2>

        {error && <p className="text-red-500 text-center mb-4">{error}</p>}

        <form onSubmit={handleSubmit}>
          <div className="mb-4">
            <label htmlFor="username" className="block text-sm font-medium">Tên người dùng</label>
            <input
              type="text"
              id="username"
              name="username"
              value={formData.username}
              onChange={handleChange}
              required
              className="w-full p-2 mt-1 border rounded-lg"
            />
          </div>

          <div className="mb-4">
            <label htmlFor="email" className="block text-sm font-medium">Email</label>
            <input
              type="email"
              id="email"
              name="email"
              value={formData.email}
              onChange={handleChange}
              required
              className="w-full p-2 mt-1 border rounded-lg"
            />
          </div>

          <div className="mb-4">
            <label htmlFor="password" className="block text-sm font-medium">Mật khẩu</label>
            <input
              type="password"
              id="password"
              name="password"
              value={formData.password}
              onChange={handleChange}
              required
              className="w-full p-2 mt-1 border rounded-lg"
            />
          </div>

          <div className="mb-4">
            <label htmlFor="user_height" className="block text-sm font-medium">Chiều cao (cm)</label>
            <input
              type="number"
              id="user_height"
              name="user_height"
              value={formData.user_height}
              onChange={handleChange}
              required
              className="w-full p-2 mt-1 border rounded-lg"
            />
          </div>

          <div className="mb-4">
            <label htmlFor="user_weight" className="block text-sm font-medium">Cân nặng (kg)</label>
            <input
              type="number"
              id="user_weight"
              name="user_weight"
              value={formData.user_weight}
              onChange={handleChange}
              required
              className="w-full p-2 mt-1 border rounded-lg"
            />
          </div>

          <div className="mb-4">
            <label htmlFor="user_age" className="block text-sm font-medium">Tuổi</label>
            <input
              type="number"
              id="user_age"
              name="user_age"
              value={formData.user_age}
              onChange={handleChange}
              required
              className="w-full p-2 mt-1 border rounded-lg"
            />
          </div>

          <div className="mb-4">
            <label htmlFor="sex" className="block text-sm font-medium">Giới tính</label>
            <select
              id="sex"
              name="sex"
              value={formData.sex}
              onChange={handleChange}
              required
              className="w-full p-2 mt-1 border rounded-lg"
            >
              <option value="female">Nữ</option>
              <option value="male">Nam</option>
            </select>
          </div>

          <button
            type="submit"
            className="w-full py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600"
          >
            Đăng ký
          </button>
        </form>
      </div>
    </div>
  );
}

export default Register;
