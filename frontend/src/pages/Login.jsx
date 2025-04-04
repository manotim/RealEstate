import { useState, useContext } from "react";
import { AuthContext } from "../context/AuthContext";


const Login = () => {
  const authContext = useContext(AuthContext); // Get the context first
  if (!authContext) {
    console.error("AuthContext is undefined. Ensure AuthProvider is wrapped correctly.");
    return <p>Error: AuthContext is not available.</p>; // Prevents crash
  }

  const { login } = authContext; // Extract login after checking context
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    await login(email, password); // Call login function
  };

  return (
    <div>
      <h2>Login</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <button type="submit">Login</button>
      </form>
    </div>
  );
};

export default Login;
