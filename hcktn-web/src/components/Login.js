import React, {useState} from 'react';

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
            <div class="footer">
                <button class='btn' type='submit'>Войти</button>
            </div>
        </div>
    )
}

export default Login;