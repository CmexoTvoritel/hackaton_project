import React, {useState} from 'react';
import { login } from '../http/userAPI';
import Admin_pan from './Admin_pan';
import '../styles/styles.css'

import {
    BrowserRouter as Router,
    Routes,
    Route,
    Link,
  } from 'react-router-dom';

const Login = function() {

    const[email, setEmail] = useState(null);
    const[password, setPassword] = useState(null);

    const signIn = async() => {
        const response = await login(email, password);
    }

    return (
        <div className='form'>
            <Link to="/">
                <h1>Registration</h1>
            </Link>
            <Link to="/login">
                <h1>Login</h1>
            </Link>
            <div className='form-body'>
                <div className='email'>
                    <label className='for_label' for='email'>E-mail:</label>
                    <div></div>
                    <input className='form_input' type="email" id="email" placeholder='Ваша почта'></input>
                </div>
                <div className='form-body'>
                    <label className='for_label' for='password'>Password:</label>
                    <div></div>
                    <input className='form_input' type="password" id="password" placeholder="Ваш пароль"></input>
                </div>
            </div>
            
            <Link to="/Admin_pan">
                <button onClick={signIn}>Login</button>
            </Link>

            

        </div>
    )
}

export default Login;