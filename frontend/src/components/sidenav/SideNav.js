import React from 'react';
// import { Link } from 'react-router-dom';
import './styles.css';
import userImg from './../../assets/paul.png';
import lemon from './../../assets/lemon.png';

const SideNav = () => {
    // const { currentUser } = useContext(AuthContext);
    return (
        <div className='sidenav'>
            <div className='user-details'>
                <img src={userImg} alt='User'/>
                <h1>Paul Kim</h1>
                <h2>@usernametag</h2>
            </div>
            <div className='side-menu'>
                <ul>
                    <li>Profile</li>
                    <li>Refer A Friend</li>
                    <li>Purchases</li>
                </ul>
            </div>
            <div className='help'>
                <p>Need help? <br/> <span>Contact us</span></p>
                <img src={lemon} alt='lemon'/>
            </div>
            
        </div>
    )
};

export default SideNav;