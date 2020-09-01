import React from 'react';
import {BrowserRouter as Router, Route, Switch} from 'react-router-dom';
import Login from './pages/Login';
import Signup from './pages/Signup';
import Home from './pages/Home';
import { AuthProvider } from './Auth';
import UserProfile from './pages/userPage/UserProfile';
import FriendsPage from './pages/friendsPage/FriendsPage';

function App() {
  return (
    <AuthProvider>
      <Router>
        <Switch>
          <Route path='/' exact component={Home} />
          <Route path='/account' exact component={UserProfile} />
          <Route path='/account/friends' exact component={FriendsPage} />
          <Route path='/login' exact component={Login} />
          <Route path='/signup' exact component={Signup} />
        </Switch>
      </Router>
    </AuthProvider>
  );
}

export default App;
