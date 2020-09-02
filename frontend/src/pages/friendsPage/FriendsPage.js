import React, { useState, useEffect } from 'react';
import './styles.css';
import UserNav from '../../components/nav/UserNav';
import SideNav from '../../components/sidenav/SideNav';
import OrderForm from '../../components/orderForm/OrderForm';
import useModal from '../../useModal';

const FriendsPage = () => {
  const [friends, setFriends] = useState([]);
  const {isShowing, toggle} = useModal();

  const url = `http://127.0.0.1:5000/friends`;
    const fetchFriends = async () => {
        const res = await fetch(url);
        const loginJSON = await res.json();
        setFriends(loginJSON);
        console.log(res)
    };

    useEffect(() => {
        fetchFriends()
    }, []);

  return (
    <React.Fragment>
      <UserNav/>
      <div className='userpage-wrapper'>
        <SideNav/>
        <div className='user-main'>
          <div className='purchases-header'>
            <h1>Friends</h1>
            <h1 id='what-to-eat-header'>What Everyone Wants to Eat<br/> In Your Area</h1>
          </div>
          <div className='friends-wrapper'>
            <div className='friends-list'>
              <div className='single-friend'>
                <div className='friends-photo'></div>
                <p>Joshua Ocampo</p>
              </div>
              <div className='single-friend'>
                <div className='friends-photo'></div>
                <p>Joshua Ocampo</p>
              </div>
              <div className='single-friend'>
                <div className='friends-photo'></div>
                <p>Joshua Ocampo</p>
              </div>
              <div className='single-friend'>
                <div className='friends-photo'></div>
                <p>Joshua Ocampo</p>
              </div>
              <div className='single-friend'>
                <div className='friends-photo'></div>
                <p>Joshua Ocampo</p>
              </div>
              <div className='single-friend'>
                <div className='friends-photo'></div>
                <p>Joshua Ocampo</p>
              </div>
            </div>
            <div className='what-friends-eat'>
              <div className='single-eating-wish' onClick={toggle}>
                <p>1</p>
                <p>Joshua O and 9 others want Chipotle</p>
                <p>Location Time</p>
              </div>
              <div className='single-eating-wish'>
                <p>1</p>
                <p>Joshua O and 9 others want Chipotle</p>
                <p>Location Time</p>
              </div>
              <div className='single-eating-wish'>
                <p>1</p>
                <p>Joshua O and 9 others want Chipotle</p>
                <p>Location Time</p>
              </div>
              <div className='single-eating-wish'>
                <p>1</p>
                <p>Joshua O and 9 others want Chipotle</p>
                <p>Location Time</p>
              </div>
              <div className='single-eating-wish'>
                <p>1</p>
                <p>Joshua O and 9 others want Chipotle</p>
                <p>Location Time</p>
              </div>
              <div className='single-eating-wish'>
                <p>1</p>
                <p>Joshua O and 9 others want Chipotle</p>
                <p>Location Time</p>
              </div>
            </div>
          </div>
        </div>
        <OrderForm isShowing={isShowing} hide={toggle}/>
      </div>
    </React.Fragment>
  );
}

export default FriendsPage;