import React from 'react';
import { NavLink, Link } from 'react-router-dom';

const Header = () => {
    return (
        <nav className="flex justify-between relative items-center font-mono h-16 text-white">
            <Link to="/" className="pl-8 text-xl font-bold ">
                {' '}
                Cars FARM
            </Link>
            <div className="pr-8 font-semibold ">
                <NavLink
                    className={({ isActive }) =>
                        isActive ? 'active-link' : 'inactive-link'
                    }
                    to="/"
                >
                    Home
                </NavLink>
                <NavLink
                    className={({ isActive }) =>
                        isActive ? 'active-link' : 'inactive-link'
                    }
                    to="/cars"
                >
                    Cars
                </NavLink>
                <NavLink
                    className={({ isActive }) =>
                        isActive ? 'active-link' : 'inactive-link'
                    }
                    to="/new"
                >
                    New Car
                </NavLink>
                <NavLink
                    className={({ isActive }) =>
                        isActive ? 'active-link' : 'inactive-link'
                    }
                    to="/about"
                >
                    About
                </NavLink>
            </div>
        </nav>
    );
};

export default Header;
