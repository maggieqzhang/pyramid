import React, {useState} from "react";
import { AuthContext } from "./../Auth.js";

const Login = () => {

  const [initialData, setInitialData] = useState([{}])

  useEffect(() => {
    fetch('/login').then(
      response => response.json())
      .then(data => setInitialData(data))
  });

  const { currentUser } = useContext(AuthContext);

  return (
    <div className='login'>
      <h1 className='main-blue'>Login</h1>
      <form className='login-form'>
            <label>Email</label>
            <input name="email" type="email" placeholder="Email" />
            <label>Password</label>
            <input name="password" type="password" placeholder="Password" />
        <button type="submit">Login</button>
        <p>Don't have an account? <NavLink className='main-blue' to='/signup'>Signup</NavLink></p>
      </form>
    </div>
  );
};

export default Login;