import React, { useState, useEffect, useContext } from "react";
import { NavLink } from 'react-router-dom';
import { AuthContext } from "./../Auth.js";
import logo from './../assets/logo-slogan.png';
import pear from './../assets/pear.svg';
import apple from './../assets/apple.png';
import orange from './../assets/orange.png';
import coconut from './../assets/coconut.png';

const Login = () => {

  const [initialData, setInitialData] = useState([{}])

  useEffect(() => {
    fetch('/login').then(
      response => response.json())
      .then(data => setInitialData(data))
  });

  const { currentUser } = useContext(AuthContext);

  return (
    <React.Fragment>
      <div className='login-wrapper'>
        <div className='intro'>
          <img src={logo} alt='Project logo' />
          <img src={pear} alt='Pear' id='pear'/>
          <p>Discover food and friends in your neighborhood. Pick a restaurant and set a comfortable time to have your food delivered at your local public area.</p>
        </div>
          <div className='login'>
            <form className='login-form'>
                  <input name="email" type="email" placeholder="Email or Phone number" />
                  <input name="password" type="password" placeholder="Password" />
                  <NavLink to='/home'><button type="submit">LOG IN</button></NavLink>
              <p>Forgot account?</p>
              <hr id='login-divider'/>
              <NavLink to='/signup'><button id='create-new-btn' type="submit">CREATE NEW ACCOUNT</button></NavLink>
            <p>Restaurant owner? Sign in</p>
            </form>
          </div>
      </div>
      <footer>
        <div className='left-fruits'>
          <img src={apple} alt='apple'/>
          <img id='orange' src={orange} alt='orange'/>
        </div>
        <div className='footer-menu'>
          <p>Help</p>
          <p>About</p>
          <p>Contact Us</p>
        </div>
        <div className='right-fruit'>
          <img src={coconut} alt='coconut'/>
        </div>
      </footer>
    </React.Fragment>
  );
};

export default Login;