// src/pages/Home.jsx
import React, { useState } from "react";
import LoginForm from "../components/LoginForm";
import SignupForm from "../components/SignupForm";

const Home = () => {
  const [showLogin, setShowLogin] = useState(true); // ค่าเริ่มต้นที่ Login Form

  const toggleForm = () => {
    setShowLogin(!showLogin); // สลับระหว่าง Login และ Signup Form
  };

  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
      {showLogin ? (
        <>
          <LoginForm />
          <p>
            ยังไม่มีบัญชี?{" "}
            <button
              onClick={toggleForm}
              style={{
                background: "none",
                border: "none",
                color: "blue",
                textDecoration: "underline",
                cursor: "pointer",
              }}
            >
              สมัครสมาชิก
            </button>
          </p>
        </>
      ) : (
        <>
          <SignupForm />
          <p>
            มีบัญชีแล้ว?{" "}
            <button
              onClick={toggleForm}
              style={{
                background: "none",
                border: "none",
                color: "blue",
                textDecoration: "underline",
                cursor: "pointer",
              }}
            >
              เข้าสู่ระบบ
            </button>
          </p>
        </>
      )}
    </div>
  );
};

export default Home;
