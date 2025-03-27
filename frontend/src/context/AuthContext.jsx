import { createContext, useState, useEffect } from "react";
import { jwtDecode } from "jwt-decode";
import { useNavigate } from "react-router-dom";
import api from "../services/api";

const AuthContext = createContext(null); // Ensure default value is null

const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const navigate = useNavigate();
  console.log("AuthProvider is rendering...");
  
  useEffect(() => {
    const token = localStorage.getItem("token");
    if (token) {
        try {
            const decodedUser = jwtDecode(token);
            console.log("Decoded User:", decodedUser); // Add this line
            if (decodedUser.exp * 1000 < Date.now()) {
                logout();
            } else {
                setUser(decodedUser);
                redirectToDashboard(decodedUser.role);
            }
        } catch (error) {
            console.error("Invalid token", error);
            logout();
        }
    }
}, []);
  

  const login = async (email, password) => {
    try {
      const response = await api.post("/auth/login", { email, password });
      const token = response.data.access_token;
      localStorage.setItem("token", token);

      const decodedUser = jwtDecode(token);
      console.log("Decoded User:", decodedUser);
      setUser(decodedUser);

      redirectToDashboard(decodedUser.role);
    } catch (error) {
      console.error("Login failed:", error.response?.data || error.message);
    }
  };

  const logout = () => {
    localStorage.removeItem("token");
    setUser(null);
    navigate("/login");
  };

  const redirectToDashboard = (role) => {
    console.log("Role:", role); // Add this line
    if (role === "landlord") {
        console.log("Redirecting to landlord dashboard");
        navigate("/landlord/dashboard");
    } else if (role === "tenant") {
        console.log("Redirecting to tenant dashboard");
        navigate("/tenant/dashboard");
    } else if (role === "admin") {
        console.log("Redirecting to admin dashboard");
        navigate("/admin/dashboard");
    } else {
        console.log("Redirecting to home, role not found");
        navigate("/"); // Default to home if role is not found
    }
};
  

  return (
    <AuthContext.Provider value={{ user, login, logout }}> {/* Ensure value is provided */}
      {children}
    </AuthContext.Provider>
  );
};

export { AuthContext, AuthProvider };

