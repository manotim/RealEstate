import { Routes, Route } from "react-router-dom";
import HomePage from "./pages/HomePage";
import TenantDashboard from "./pages/TenantDashboard";
import LandlordDashboard from "./pages/LandlordDashboard";
import AdminDashboard from "./pages/AdminDashboard";
import Login from "./pages/Login";
import Register from "./pages/Register";

function App() {
  return (
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/tenant/dashboard" element={<TenantDashboard />} />
        <Route path="/landlord/dashboard" element={<LandlordDashboard />} />
        <Route path="/admin/dashboard" element={<AdminDashboard />} />
      </Routes>
  );
}

export default App;
