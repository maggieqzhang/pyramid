import React from 'react';
import './styles.css';
import UserNav from '../../components/nav/UserNav';
import SideNav from '../../components/sidenav/SideNav';
// import { Link } from 'react-router-dom';
import discovery from './../../assets/discovery.png';
import users from './../../assets/users.png';
import profile from './../../assets/profile2.png';

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
              <img src={discovery} alt='Discovery Icon'/>
              <div className='vertical-divide'></div>
              <img src={users} alt='Users Icon'/>
              <div className='vertical-divide'></div>
              <img src={profile} alt='Profile Icon'/>
            </div>
          </div>
          <div className='purchases-list'>
            <div className='single-purchase'>
              <div>
                <p><span>You</span> paid <span>Chipotle</span> <br/> with <span>Joshua O</span> and <span>5 others</span></p>
                <p className='location-name'>Harmony Trails Park, CA US <span className='purchase-time'>Sept 1, 2020; 11:00 AM</span></p>
              </div>
              <div className='purchase-price'>$12.84</div>
            </div>
            <div className='single-purchase'>
              <div>
                <p><span>You</span> paid <span>Chipotle</span> <br/> with <span>Joshua O</span> and <span>5 others</span></p>
                <p className='location-name'>Harmony Trails Park, CA US <span className='purchase-time'>Sept 1, 2020; 11:00 AM</span></p>
              </div>
              <div className='purchase-price'>$12.84</div>
            </div>
            <div className='single-purchase'>
              <div>
                <p><span>You</span> paid <span>Chipotle</span> <br/> with <span>Joshua O</span> and <span>5 others</span></p>
                <p className='location-name'>Harmony Trails Park, CA US <span className='purchase-time'>Sept 1, 2020; 11:00 AM</span></p>
              </div>
              <div className='purchase-price'>$12.84</div>
            </div>
            <div className='single-purchase'>
              <div>
                <p><span>You</span> paid <span>Chipotle</span> <br/> with <span>Joshua O</span> and <span>5 others</span></p>
                <p className='location-name'>Harmony Trails Park, CA US <span className='purchase-time'>Sept 1, 2020; 11:00 AM</span></p>
              </div>
              <div className='purchase-price'>$12.84</div>
            </div>
            <div className='single-purchase'>
              <div>
                <p><span>You</span> paid <span>Chipotle</span> <br/> with <span>Joshua O</span> and <span>5 others</span></p>
                <p className='location-name'>Harmony Trails Park, CA US <span className='purchase-time'>Sept 1, 2020; 11:00 AM</span></p>
              </div>
              <div className='purchase-price'>$12.84</div>
            </div>
            <div className='single-purchase'>
              <div>
                <p><span>You</span> paid <span>Chipotle</span> <br/> with <span>Joshua O</span> and <span>5 others</span></p>
                <p className='location-name'>Harmony Trails Park, CA US <span className='purchase-time'>Sept 1, 2020; 11:00 AM</span></p>
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