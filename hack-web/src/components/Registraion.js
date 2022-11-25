import React, {useState} from 'react';

const Registration = function() {

    const[firstName, setFirstName] = useState(null);
    const[secondName, setSecondName] = useState(null);
    const[lastName, setLastName] = useState(null);
    const[email, setEmail] = useState(null);
    const[password, setPassword] = useState(null);
    const[confrimPassword, setConfrimPassword] = useState(null);

    const handleInputChange = (e) => {
        const{id, value} = e.target;
        if(id === "firstName") setFirstName(value);
        else if(id === "secondName") setSecondName(value);
        else if(id === "lastName") setLastName(value);
        else if(id === "email") setEmail(value);
        else if(id === "password") setPassword(value);
        else if(id === "confrimPassword") setConfrimPassword(value);
    }

    return (
        <div className='form'>
            <div className='form-body'>
                <div className='username'>
                    <label className='form_label' for='firstName'>Имя:</label>
                    <input className='form_input' value={firstName} onChange = {(e) => handleInputChange(e)} type="text" id='firstName' placeholder='Ваше имя'></input>
                </div>
                <div className='secondname'>
                    <label className='form_label' for='secondName'>Фамилия:</label>
                    <input className='form_input' value={secondName} onChange = {(e) => handleInputChange(e)} type="text" id='secondName' placeholder='Ваша фамилия'></input>
                </div>
                <div className='lastname'>
                    <label className='form_label' for='lastName'>Отчество:</label>
                    <input className='form_input' value={lastName} onChange = {(e) => handleInputChange(e)} type='text' id='lastName' placeholder='Ваше отчество'></input>
                </div>
                <div className='email'>
                    <label className='form_label' for='email'>Почта:</label>
                    <input className='form_input' value={email} onChange ={(e) => handleInputChange(e)} type='email' id='email' placeholder='Ваша почта'></input>
                </div>
                <div className='password'>
                    <label className='form_label' for='password'>Пароль:</label>
                    <input className='form_input' value={password} onChange = {(e) => handleInputChange(e)} type='password' id='passwrod'></input>
                </div>
                <div className='confrim-password'>
                    <label className='form_label' for='password'>Подтверждение пароля:</label>
                    <input className='form_input' value={confrimPassword} onChange = {(e) => handleInputChange(e)} type='password' id='password'></input>
                </div>
            </div>
            <div class="footer">
                <button class='btn' type='submit'>Зарегистрироваться</button>
            </div>
        </div>
    )
}

export default Registration;