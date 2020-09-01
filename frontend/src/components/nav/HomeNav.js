import React from 'react';
import { NavLink, Link } from 'react-router-dom';
import './styles.css';

const HomeNav = () => {
    // const { currentUser } = useContext(AuthContext);
    const currentTime= new Date().toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit' });

    return (
        <header id='home-header'>
                <div className='logo'>
                <h1>Rumen</h1>
                <p>Group food ordering made simple</p>
                </div>
            <nav>
                <ul className='menu'>
                    <li id='current-time'>{currentTime}</li>
                    <li id='home-nav-menu'><NavLink to='/location'>Harmony Trails Park</NavLink></li>
                    <li><NavLink to='/account'>Account</NavLink></li>
                    <li><NavLink to='/login'>Login</NavLink></li>
                    <li><NavLink to='/signup'>Signup</NavLink></li>
                    {/* {currentUser && <li><button className='logout-btn main-blue' onClick={()=>app.auth().signOut()}>Logout</button></li>} */}
                </ul>
            </nav>         
        </header>
    )
};

export default HomeNav;