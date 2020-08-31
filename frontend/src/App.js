import React from 'react';
import {BrowserRouter as Router, Route, Switch} from 'react-router-dom';
import Login from './pages/Login';
import Signup from './pages/Signup';
import Nav from './components/nav/Nav';
import Home from './pages/Home';
import { AuthProvider } from './Auth';
import UserProfile from './pages/UserProfile';

function App() {
  return (
    <AuthProvider>
      <Router>
        <Nav/>
        <Switch>
          <Route path='/' exact component={Home} />
          <Route path='/account' exact component={UserProfile} />
          <Route path='/login' exact component={Login} />
          <Route path='/signup' exact component={Signup} />
        </Switch>
      </Router>
    </AuthProvider>
  );
}

export default App;
