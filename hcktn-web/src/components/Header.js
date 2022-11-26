import React from 'react';
import Registration from './Registration';
import Login from './Login';

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
            <header>
            <nav>
                <ul>
                    <li>
                        <Link to="/">Registration</Link>
                    </li>
                    <li>
                        <Link to="/login">Login</Link>
                    </li>
                </ul>
            </nav>
            </header>

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