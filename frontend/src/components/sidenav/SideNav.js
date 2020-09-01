import React from 'react';
// import { Link } from 'react-router-dom';
import './styles.css';
import userImg from './../../assets/paul.png';

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
                    <li>Search</li>
                    <li>Refer A Friend</li>
                    <li>Purchases</li>
                    <li>Settings</li>
                    <li>Get Help</li>
                </ul>
            </div>
        </div>
    )
};

export default SideNav;