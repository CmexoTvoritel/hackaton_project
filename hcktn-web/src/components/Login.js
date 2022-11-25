import React, {useState} from 'react';
import Admin_pan from './Admin_pan';

import {
    BrowserRouter as Router,
    Routes,
    Route,
    Link,
  } from 'react-router-dom';

const Login = function() {

    const[email, setEmail] = useState(null);
    const[password, setPassword] = useState(null);

    return (
        <div className='form'>
            <div className='form-body'>
                <div className='email'>
                    <label className='for_label' for='email'>E-mail:</label>
                    <input className='form_input' type="email" id="email" placeholder='Ваша почта'></input>
                </div>
                <div className='form-body'>
                    <label className='for_label' type="password" id="password" for='password'>Password:</label>
                    <input></input>
                </div>
            </div>
            
            <Link to="/Admin_pan">
                <button>Login</button>
            </Link>

            

        </div>
    )
}

// function admn_pn () {
//     <Link to="/admin_panel">Admin_pan</Link>
// }

export default Login;