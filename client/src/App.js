import React from 'react';
import {
  BrowserRouter as Router,
  Route
} from 'react-router-dom';
import { withAuthentication, AuthUserContext } from './components/session';

import HomePage from './pages/HomePage/home-page.component';
import LoginPage from './pages/LoginPage/login-page.component';

import './App.css';

import 'semantic-ui-css/semantic.min.css'

const App = () => {
  return (
    <div className="App">
      <Router>
        <AuthUserContext.Consumer>
        { 
          authUser =>
            authUser ?
            <Route exact path='/' component={HomePage} /> :
            <Route exact path='/' component={LoginPage} />
        }
        </AuthUserContext.Consumer>
      </Router>
    </div>
  )
}

export default withAuthentication(App);
