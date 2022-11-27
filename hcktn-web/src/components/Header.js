import React from 'react';
import Registration from './Registration';
import Login from './Login';
import { login, registration } from '../http/userAPI';

import {
    BrowserRouter as Router,
    Routes,
    Route,
    Link,
  } from 'react-router-dom';
import Admin_pan from './Admin_pan';

const Header = function() {
    return(
        <Router>
            <main>
                    <Routes>
                        <Route exact path="/Admin_pan" element={<Admin_pan/>}/>
                        <Route exact path="/login" element={<Login/>}/>
                        <Route exact path="/"element={<Registration/>}/>
                    </Routes>
            </main>

        </Router>
    )
}

export default Header;