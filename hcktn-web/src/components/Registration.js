import React, {useState} from 'react';
import { Link } from 'react-router-dom';
import { registration } from '../http/userAPI';
import Admin_pan from './Admin_pan';
import '../styles/styles.css'

const Registration = function() {

    

    const[firstName, setFirstName] = React.useState(null);
    const[secondName, setSecondName] = React.useState(null);
    const[lastName, setLastName] = React.useState(null);
    const[email, setEmail] = React.useState(null);
    const[password, setPassword] = React.useState(null);
    const[confrimPassword, setConfrimPassword] = React.useState(null);

    const handleInputChange = (e) => {
        const{id, value} = e.target;
        if(id === "firstName") setFirstName(value);
        else if(id === "secondName") setSecondName(value);
        else if(id === "lastName") setLastName(value);
        else if(id === "email") setEmail(value);
        else if(id === "password") setPassword(value);
        else if(id === "confrimPassword") setConfrimPassword(value);
    }

    const signIn = async() => {
        const response = await registration(firstName, secondName, lastName, email, password)
        console.log(response)
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
                <div className='username'>
                    <label className='form_label' for='firstName'>Имя:</label>
                    <div></div>
                    <input className='form_input' value={firstName} onChange = {(e) => handleInputChange(e)} type="text" id='firstName' placeholder='Ваше имя'></input>
                </div>
                <div className='secondname'>
                    <label className='form_label' for='secondName'>Фамилия:</label>
                    <div></div>
                    <input className='form_input' value={secondName} onChange = {(e) => handleInputChange(e)} type="text" id='secondName' placeholder='Ваша фамилия'></input>
                </div>
                <div className='lastname'>
                    <label className='form_label' for='lastName'>Отчество:</label>
                    <div></div>
                    <input className='form_input' value={lastName} onChange = {(e) => handleInputChange(e)} type='text' id='lastName' placeholder='Ваше отчество'></input>
                </div>
                <div className='email'>
                    <label className='form_label' for='email'>Почта:</label>
                    <div></div>
                    <input className='form_input' value={email} onChange ={(e) => handleInputChange(e)} type='email' id='email' placeholder='Ваша почта'></input>
                </div>
                <div className='password'>
                    <label className='form_label' for='password'>Пароль:</label>
                    <div></div>
                    <input className='form_input' value={password} onChange = {(e) => handleInputChange(e)} type='password' id='password'></input>
                </div>
                <div className='confrim-password'>
                    <label className='form_label' for='password'>Подтверждение пароля:</label>
                    <div></div>
                    <input className='form_input' value={confrimPassword} onChange = {(e) => handleInputChange(e)} type='password' id='confrimPassword'></input>
                </div>
            </div>

            <Link to="/Admin_pan">
                <button onClick={signIn}>Registration</button>
            </Link>
            <h1>{firstName}</h1>

        </div>
    )
}

export default Registration;