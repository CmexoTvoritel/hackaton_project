import React from 'react';
import Registration from './Registration';
import Login from './Login';

import {
    BrowserRouter as Router,
    Routes,
    Route,
    Link,
  } from 'react-router-dom';

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
                        <Route exact path="/login" element={<Login/>}/>
                        <Route path="/"element={<Registration/>}/>
                    </Routes>
            </main>

        </Router>
    )
}

export default Header;