// src/components/SignupForm.jsx
import React, { useState } from 'react';
import API from '../api';

const SignupForm = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      // ตรวจสอบว่าข้อมูลที่ส่งไปเป็น JSON
      console.log("Sending Data:", { email, password });
      
      const res = await API.post('/auth/signup', {
        email, 
        password
      }, {
        headers: {
          'Content-Type': 'application/json'  // กำหนด Content-Type
        }
      });

      console.log("Response Data:", res.data);
      alert('Signup successful!');
    } catch (err) {
      console.error("Error Response:", err.response?.data || err);
      alert('Signup failed. See console for details.');
    }
  };

  return (
    <div className="min-h-screen bg-white flex items-center justify-center px-4">
      <div
        className="w-full max-w-4xl h-auto md:h-[550px] bg-white rounded-[35px] shadow-lg flex flex-col md:flex-row overflow-hidden"
        style={{
          boxShadow: '2px 2px 15px -5px #00000040', // เพิ่มเงาให้การ์ด
        }}
      >
        {/* ฝั่งซ้าย */}
        <div
          className="relative w-full md:w-1/2 h-72 md:h-full bg-gradient-to-br from-[#2BADCF] to-[#05AE9A] flex items-center justify-center overflow-hidden"
          style={{
            boxShadow: '1px 7px 15px -5px #00000040',
            background: 'linear-gradient(180deg, #2BADCF 0%, #05AE9A 100%)',
          }}
        >
          {/* ใส่ภาพพื้นหลังเบา ๆ */}
          <img
            src="/images/Group295.png"
            alt="Background"
            className="absolute top-0 left-0 w-full h-full object-cover opacity-20"
          />
          {/* ใส่ภาพหลักให้อยู่ด้านหน้า */}
          <img
            src="/images/Group295.png"
            alt="Foreground"
            className="absolute top-0 left-0 w-full h-full"
          />
          {/* ข้อความ */}
          <div className="relative text-white text-center px-8">
            <h1 className="text-3xl md:text-5xl font-bold mb-4">Welcome</h1>
            <p className="text-lg md:text-2xl font-light mb-4">To Parking Dashboard</p>
            <hr className="border-white mx-auto my-4" />
            <p className="mt-2 text-xs md:text-sm font-medium">
              ระบบบริหารจัดการที่จอดรถอัจฉริยะ
            </p>
          </div>
        </div>
        {/* ด้านขวา */}
        <div className="w-full md:w-1/2 p-8 flex flex-col justify-start items-center">
          {/* ปรับขนาดและตำแหน่งของโลโก้ */}
          <img
            src="/images/All-logo.png" // ใส่ URL โลโก้ของคุณ
            alt="Logo"
            style={{
              width: '300px', // ลดขนาดโลโก้เมื่อเป็นมือถือ
              height: 'auto', // ความสูงอัตโนมัติรักษาสัดส่วน
              marginBottom: '60px', // ระยะห่างด้านล่าง 20px
              marginTop: '30px',
            }}
          />
          <form onSubmit={handleSubmit} className="w-full px-4">
            <input
              type="text"
              placeholder="Admin 001"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
              className="block w-full mb-4 px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-400"
              style={{
                border: '1px solid #1AB6C1', // กำหนดกรอบเป็นสี #1AB6C1
              }}
            />
            <input
              type="password"
              placeholder="Password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
              className="block w-full mb-4 px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-400"
              style={{
                border: '1px solid #1AB6C1',
                marginBottom: '40px',
              }}
            />
            <button
              type="submit"
              className="w-full text-white py-2 rounded font-semibold"
              style={{
                background: 'linear-gradient(180deg, #30ABD3 0%, #13CAA9 100%)',
              }}
            >
              เข้าสู่ระบบ
            </button>
          </form>
        </div>
      </div>
    </div>
  );  
};

export default SignupForm;
