import React from 'react';
import { NavLink, Link } from 'react-router-dom';
import './styles.css';

const HomeNav = () => {
    // const { currentUser } = useContext(AuthContext);
    return (
        <header id='home-header'>
            <Link to='/'>
                <div className='logo'>
                <h1>Rumen</h1>
                <p>Group food ordering made simple</p>
                </div>
            </Link>
            <nav>
                <ul className='menu'>
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