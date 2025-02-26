import React, { useState, useEffect, useRef } from "react";
import { useNavigate } from "react-router-dom"; // Import useNavigate
import API from "../utils/api";
import { FaPaperPlane } from "react-icons/fa";

function ChatAI() {
  const [userMessage, setUserMessage] = useState("");
  const [chatHistory, setChatHistory] = useState([]);
  const [loading, setLoading] = useState(false);
  const chatContainerRef = useRef(null);
  const navigate = useNavigate(); // Khởi tạo hook điều hướng

  useEffect(() => {
    const fetchChatHistory = async () => {
      try {
        const token = sessionStorage.getItem("access_token");
        const res = await API.get("/chatHistories/10/1", {
          headers: { Authorization: `Bearer ${token}` },
        });
        setChatHistory(res.data.reverse()); // Hiển thị tin nhắn mới nhất ở dưới
      } catch (error) {
        console.error("Lỗi khi lấy lịch sử trò chuyện:", error);
      }
    };

    fetchChatHistory();
  }, []);

  useEffect(() => {
    if (chatContainerRef.current) {
      chatContainerRef.current.scrollTop = chatContainerRef.current.scrollHeight;
    }
  }, [chatHistory]);

  const handleSendMessage = async () => {
    if (!userMessage.trim()) return;

    const newMessage = { user_message: userMessage, ai_response: "Đang trả lời..." };
    setChatHistory((prev) => [...prev, newMessage]);
    setUserMessage("");
    setLoading(true);

    try {
      const token = sessionStorage.getItem("access_token");
      const res = await API.post(
        "/alResponse",
        { user_message: userMessage },
        { headers: { Authorization: `Bearer ${token}` } }
      );

      setChatHistory((prev) =>
        prev.map((msg, index) =>
          index === prev.length - 1 ? { ...msg, ai_response: res.data.response } : msg
        )
      );
    } catch (error) {
      console.error("Lỗi khi gửi tin nhắn:", error);
      setChatHistory((prev) =>
        prev.map((msg, index) =>
          index === prev.length - 1 ? { ...msg, ai_response: "Lỗi khi gửi tin nhắn." } : msg
        )
      );
    } finally {
      setLoading(false);
    }
  };

  const handleLogout = () => {
    sessionStorage.removeItem("access_token"); // Xóa token
    navigate("/login"); // Điều hướng về trang đăng nhập
  };

  return (
    <div className="flex justify-center items-center min-h-screen bg-gradient-to-r from-blue-500 to-purple-600 p-4">
      <div className="w-full max-w-lg bg-gradient-to-r from-indigo-500 to-blue-500 p-4 rounded-xl shadow-lg">
        {/* Header */}
        <div className="flex items-center justify-between p-3 border-b border-gray-400">
          <div className="flex items-center">
            <img
              src="/avatar.png"
              alt="AI Avatar"
              className="w-10 h-10 rounded-full border-2 border-white"
            />
            <div className="ml-3 text-white">
              <h2 className="text-lg font-semibold">Chat with AI</h2>
              <p className="text-sm">Active now</p>
            </div>
          </div>
          {/* Buttons điều hướng */}
          <div className="flex space-x-2">
            <button
              onClick={() => navigate("/dashboard")}
              className="bg-yellow-400 text-black px-3 py-1 rounded-lg hover:bg-yellow-500"
            >
              Dashboard
            </button>
            <button
              onClick={handleLogout}
              className="bg-red-500 text-white px-3 py-1 rounded-lg hover:bg-red-600"
            >
              Logout
            </button>
          </div>
        </div>

        {/* Chat container */}
        <div
          ref={chatContainerRef}
          className="h-80 overflow-y-auto p-4 flex flex-col space-y-2 bg-blue-300 rounded-lg"
        >
          {chatHistory.map((chat, index) => (
            <div key={index} className="flex flex-col space-y-1">
              <div className="self-end bg-green-400 text-white px-4 py-2 rounded-lg max-w-xs">
                {chat.user_message}
              </div>
              <div className="self-start bg-white text-black px-4 py-2 rounded-lg max-w-xs">
                {chat.ai_response}
              </div>
            </div>
          ))}
        </div>

        {/* Input chat */}
        <div className="flex items-center mt-3 bg-gray-800 rounded-lg p-2">
          <input
            type="text"
            value={userMessage}
            onChange={(e) => setUserMessage(e.target.value)}
            placeholder={loading ? "Đang chờ AI phản hồi..." : "Nhập tin nhắn..."}
            className="flex-1 bg-transparent text-white outline-none p-2"
            onKeyPress={(e) => e.key === "Enter" && handleSendMessage()}
            disabled={loading}
          />
          <button
            onClick={handleSendMessage}
            className="bg-green-500 p-2 rounded-lg text-white hover:bg-green-600"
            disabled={loading}
          >
            <FaPaperPlane />
          </button>
        </div>
      </div>
    </div>
  );
}

export default ChatAI;
