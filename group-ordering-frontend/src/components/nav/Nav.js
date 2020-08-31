import React from 'react';
import { NavLink, Link } from 'react-router-dom';
import './styles.css';

const Nav = () => {
    // const { currentUser } = useContext(AuthContext);
    return (
        <header>
            <Link to='/'>
                <div className='logo'>Group Food Ordering</div>
            </Link>
            <nav>
                <ul className='menu'>
                    <li><NavLink to='/login'>Login</NavLink></li>
                    <li><NavLink to='/signup'>Signup</NavLink></li>
                    {/* {currentUser && <li><button className='logout-btn main-blue' onClick={()=>app.auth().signOut()}>Logout</button></li>} */}
                </ul>
            </nav>         
        </header>
    )
};

export default Nav;