import React from 'react';

const Registration = function() {
    return (
        <div className='form'>
            <div className='form-body'>
                <div className='username'>
                    <label className='form_label' for='firstName'>Имя:</label>
                    <input className='form_input' type="text" id='firstName' placeholder='Ваше имя'></input>
                </div>
                <div className='secondname'>
                    <label className='form_label' for='secondName'>Фамилия:</label>
                    <input className='form_input' type="text" id='secondName' placeholder='Ваша фамилия'></input>
                </div>
                <div className='lastname'>
                    <label className='form_label' for='lastName'>Отчество:</label>
                    <input className='form_input' type='text' id='lastName' placeholder='Ваше отчество'></input>
                </div>
                <div className='email'>
                    <label className='form_label' for='email'>Почта:</label>
                    <input className='form_input' type='email' id='email' placeholder='Ваша почта'></input>
                </div>
                <div className='password'>
                    <label className='form_label' for='password'>Пароль:</label>
                    <input className='form_input' type='password' id='passwrod'></input>
                </div>
                <div className='confrim-password'>
                    <label className='form_label' for='password'>Подтверждение пароля:</label>
                    <input className='form_input' type='password' id='password'></input>
                </div>
            </div>
        </div>
    )
}

export default Registration;