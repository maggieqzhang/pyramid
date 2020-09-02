import React from 'react';
import {BrowserRouter as Router, Route, Switch} from 'react-router-dom';
import Login from './pages/Login';
import Signup from './pages/Signup';
import Home from './pages/Home';
import Checkout from './pages/checkout/Checkout';
import { AuthProvider } from './Auth';
import UserProfile from './pages/userPage/UserProfile';
import FriendsPage from './pages/friendsPage/FriendsPage';
import PickTime from './pages/PickTime';

function App() {
  return (
    <AuthProvider>
      <Router>
        <Switch>
          <Route path='/' exact component={Login} />
          <Route path='/account' exact component={UserProfile} />
          <Route path='/account/friends' exact component={FriendsPage} />
          <Route path='/checkout' exact component={Checkout} />
          <Route path='/home' exact component={Home} />
          <Route path='/pick-time' exact component={PickTime} />
          <Route path='/signup' exact component={Signup} />
        </Switch>
      </Router>
    </AuthProvider>
  );
}

export default App;
