import React from 'react';
import logo from '../assets/logo.png';

export default function Header() {
    return (
        <header className="header">
            <div className="header-container">
                <div className="logo">
                    <img src={logo} alt="Logo" />
                </div>
                <button className="login-btn">Login</button>
            </div>
        </header>
    );
}