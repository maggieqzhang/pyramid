import React from "react";
// import { withRouter, Redirect } from "react-router";
// import { AuthContext } from "./../Auth.js";
import { NavLink } from 'react-router-dom';

const Login = () => {

  return (
    <div className='login-page'>
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
    </div>
  );
};

export default Login;