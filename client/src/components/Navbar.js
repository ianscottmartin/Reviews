// Navbar.js
import React from 'react';
import { Link } from 'react-router-dom'; // If you're using React Router

function Navbar() {
    return (
        <nav>
            <ul>
                <li>
                    <Link to="/">Home</Link>
                </li>
                <li>
                    <Link to="/artists">Artists</Link>
                </li>
                <li>
                    <Link to="/museums">Museums</Link>
                </li>
                <li>
                    <Link to="/login">Login</Link>
                </li>
                <li>
                    <Link to="/signup">Signup</Link>
                </li>
            </ul>
        </nav>
    );
}

export default Navbar;
