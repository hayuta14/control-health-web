import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import API from "../utils/api";

function Dashboard() {
  const [userData, setUserData] = useState(null);
  const [isEditing, setIsEditing] = useState(false);
  const [editData, setEditData] = useState({});
  const [newPassword, setNewPassword] = useState("");
  const [message, setMessage] = useState("");
  const navigate = useNavigate();

  useEffect(() => {
    const fetchUserData = async () => {
      try {
        const token = sessionStorage.getItem("access_token");
        if (!token) {
          navigate("/login");
          return;
        }

        const response = await API.get("/userProfile", {
          headers: { Authorization: `Bearer ${token}` },
        });

        const formattedData = {
          username: response.data.username,
          email: response.data.email,
          user_height: response.data.user_height,
          user_weight: response.data.user_weight,
          user_age: response.data.user_age,
          sex: response.data.sex,
          BMI: response.data.BMI,
          BMR: response.data.BMR,
          body_fat: response.data.body_fat,
        };

        setUserData(formattedData);
        setEditData(formattedData);
      } catch (error) {
        console.error("Lỗi khi lấy dữ liệu người dùng:", error);
        navigate("/login");
      }
    };

    fetchUserData();
  }, [navigate]);
  const fetchUserData = async () => {
    try {
      const token = sessionStorage.getItem("access_token");
      if (!token) {
        navigate("/login");
        return;
      }
  
      const response = await API.get("/userProfile", {
        headers: { Authorization: `Bearer ${token}` },
      });
  
      const formattedData = {
        username: response.data.username,
        email: response.data.email,
        user_height: response.data.user_height,
        user_weight: response.data.user_weight,
        user_age: response.data.user_age,
        sex: response.data.sex,
        BMI: response.data.BMI,
        BMR: response.data.BMR,
        body_fat: response.data.body_fat,
      };
  
      setUserData(formattedData);
      setEditData(formattedData);
    } catch (error) {
      console.error("Lỗi khi lấy dữ liệu người dùng:", error);
      navigate("/login");
    }
  };

  const handleEditChange = (e) => {
    setEditData({ ...editData, [e.target.name]: e.target.value });
  };

  const handleSave = async () => {
    try {
      const token = sessionStorage.getItem("access_token");

      const updatedData = {
        username: editData.username,
        password: newPassword || undefined,
        user_height: editData.user_height,
        user_weight: editData.user_weight,
        user_age: editData.user_age,
        sex: editData.sex,
      };

      await API.put("/alterUser", updatedData, {
        headers: { Authorization: `Bearer ${token}` },
      });

      setUserData(editData);
      setIsEditing(false);
      setNewPassword("");
      setMessage("Cập nhật thành công!");
      fetchUserData();
    } catch (error) {
      console.error("Lỗi khi cập nhật:", error);
      setMessage("Có lỗi xảy ra. Vui lòng thử lại!");
    }
  };

  const handleLogout = () => {
    sessionStorage.removeItem("access_token");
    navigate("/login");
  };

  if (!userData) return <div className="text-center mt-10">Loading...</div>;

  return (
    <div className="min-h-screen bg-gray-100 flex justify-center items-center p-6">
      <div className="bg-white w-full max-w-4xl rounded-lg shadow-lg p-6">
        {/* Profile Header */}
        <div className="flex flex-col items-center mb-6">
          <img
            src="https://bootdey.com/img/Content/avatar/avatar7.png"
            alt="Profile"
            className="w-24 h-24 rounded-full border-2 border-blue-400"
          />
          {isEditing ? (
            <input
              type="text"
              name="username"
              value={editData.username}
              onChange={handleEditChange}
              className="mt-2 p-2 border rounded-md"
            />
          ) : (
            <h2 className="text-xl font-semibold mt-4">{userData.username}</h2>
          )}
        </div>

        {/* Success/Error Message */}
        {message && <p className="text-center mb-4 text-green-500">{message}</p>}

        {/* User Info */}
        <div className="grid grid-cols-2 gap-6">
          {[
            { key: "email", label: "Email" },
            { key: "user_height", label: "Chiều cao (cm)" },
            { key: "user_weight", label: "Cân nặng (kg)" },
            { key: "user_age", label: "Tuổi" },
            { key: "sex", label: "Giới tính" },
          ].map((field) => (
            <div key={field.key} className="flex flex-col">
              <label className="text-gray-600 font-medium">{field.label}</label>
              {isEditing ? (
                <input
                  type="text"
                  name={field.key}
                  value={editData[field.key]}
                  onChange={handleEditChange}
                  className="p-2 border rounded-md"
                />
              ) : (
                <p className="p-2 bg-gray-100 rounded-md">{userData[field.key]}</p>
              )}
            </div>
          ))}

          {/* BMI, BMR, Body Fat */}
          {[
            { key: "BMI", label: "Chỉ số BMI" },
            { key: "BMR", label: "Tỷ lệ trao đổi chất (BMR)" },
            { key: "body_fat", label: "Tỷ lệ mỡ cơ thể (%)" },
          ].map((metric) => (
            <div key={metric.key} className="flex flex-col">
              <label className="text-gray-600 font-medium">{metric.label}</label>
              <p className="p-2 bg-gray-100 rounded-md">{userData[metric.key]}</p>
            </div>
          ))}

          {/* Password Input */}
          {isEditing && (
            <div className="flex flex-col">
              <label className="text-gray-600 font-medium">Mật khẩu mới</label>
              <input
                type="password"
                value={newPassword}
                onChange={(e) => setNewPassword(e.target.value)}
                className="p-2 border rounded-md"
              />
            </div>
          )}
        </div>

        {/* Action Buttons */}
        <div className="mt-6 flex justify-between">
          {isEditing ? (
            <button
              onClick={handleSave}
              className="bg-green-500 text-white py-2 px-4 rounded-md hover:bg-green-600"
            >
              Lưu
            </button>
          ) : (
            <button
              onClick={() => setIsEditing(true)}
              className="bg-blue-500 text-white py-2 px-4 rounded-md hover:bg-blue-600"
            >
              Chỉnh sửa
            </button>
          )}

          <button
            onClick={handleLogout}
            className="bg-red-500 text-white py-2 px-4 rounded-md hover:bg-red-600"
          >
            Đăng xuất
          </button>

          <button
            onClick={() => navigate("/analyze")}
            className="bg-purple-500 text-white py-2 px-4 rounded-md hover:bg-purple-600"
          >
            Chat AI
          </button>
        </div>
      </div>
    </div>
  );
}

export default Dashboard;
