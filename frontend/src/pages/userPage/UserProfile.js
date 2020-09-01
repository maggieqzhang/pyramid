import React from 'react';
import './styles.css';
import UserNav from '../../components/nav/UserNav';
import SideNav from '../../components/sidenav/SideNav';
import { Link } from 'react-router-dom';

const UserProfile = () => {
  return (
    <React.Fragment>
      <UserNav/>
      <div className='userpage-wrapper'>
        <SideNav/>
        <div className='user-main'>
          <div className='purchases-header'>
            <h1>Purchases</h1>
            <div className='user-icons-wrapper'>
              <ul>
                <li>Global icon</li>
                <li><Link to='/account/friends'>Friends icon</Link></li>
                <li>You only icon</li>
              </ul>
            </div>
          </div>
          <div className='purchases-list'>
            <div className='single-purchase'>
              <div>
                <p><span>You</span> paid <span>Chipotle</span> <br/> with <span>Joshua O</span> and <span>5 others</span></p>
                <p className='location-name'>Local Location Name</p>
              </div>
              <div className='purchase-price'>$12.84</div>
            </div>
            <div className='single-purchase'>
              <div>
                <p><span>You</span> paid <span>Chipotle</span> <br/> with <span>Joshua O</span> and <span>5 others</span></p>
                <p className='location-name'>Local Location Name</p>
              </div>
              <div className='purchase-price'>$12.84</div>
            </div>
            <div className='single-purchase'>
              <div>
                <p><span>You</span> paid <span>Chipotle</span> <br/> with <span>Joshua O</span> and <span>5 others</span></p>
                <p className='location-name'>Local Location Name</p>
              </div>
              <div className='purchase-price'>$12.84</div>
            </div>
            <div className='single-purchase'>
              <div>
                <p><span>You</span> paid <span>Chipotle</span> <br/> with <span>Joshua O</span> and <span>5 others</span></p>
                <p className='location-name'>Local Location Name</p>
              </div>
              <div className='purchase-price'>$12.84</div>
            </div>
            <div className='single-purchase'>
              <div>
                <p><span>You</span> paid <span>Chipotle</span> <br/> with <span>Joshua O</span> and <span>5 others</span></p>
                <p className='location-name'>Local Location Name</p>
              </div>
              <div className='purchase-price'>$12.84</div>
            </div>
          </div>
        </div>
      </div>
    </React.Fragment>
  );
}

export default UserProfile;