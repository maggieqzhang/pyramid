import React from 'react';
import { NavLink, Link } from 'react-router-dom';
import './styles.css';
import logo from './../../assets/logo-slogan.png';
import time from './../../assets/clock.png';
import profile from './../../assets/profile.png';
import social from './../../assets/social.png';
import location from './../../assets/place.png';

const UserNav = () => {
    // const { currentUser } = useContext(AuthContext);
    const currentTime= new Date().toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit' });

    return (
        <header id='home-header'>
                <div className='logo'>
                    <img src={logo} alt='Project logo'/>
                </div>
                <div className='current-time'>
                    <p>CURRENT TIME</p>
                    <img src={time} alt='Time'/>
                    {currentTime}
                </div>
                <div className='current-location'>
                    <p>LOCATION</p>
                    <img src={location} alt='Location'/>
                    <Link to='/home'><span>Harmony Trails Park</span></Link>
                </div>
                <nav>
                    <ul className='menu'>
                        {/* <li id='home-nav-menu'><NavLink to='/location'>Harmony Trails Park</NavLink></li> */}
                        <li>Help</li>
                        <li>Settings</li>
                        <li>Logout</li>
                        {/* {currentUser && <li><button className='logout-btn main-blue' onClick={()=>app.auth().signOut()}>Logout</button></li>} */}
                    </ul>
                    <div className='main-menu'>
                        <div className='profile-link'>
                        <NavLink to='/account'>
                            <img src={profile} alt='Profile'/>
                            <p>Profile</p>
                        </NavLink>
                        </div>
                        <div className='social-link'>
                        <NavLink to='/account/friends'>
                            <img src={social} alt='Social'/>
                            <p>Social</p>
                        </NavLink>
                        </div>
                    </div>
                </nav> 
        </header>
    )
};

export default UserNav;