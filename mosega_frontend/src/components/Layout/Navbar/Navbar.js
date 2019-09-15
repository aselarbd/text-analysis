import React from 'react';
import { Menu } from 'semantic-ui-react'
import {Link} from "react-router-dom";

const navbar = () => {
    return (
        <div>
            <Menu inverted size='huge'>
                <Menu.Item name='Home'>
                    <Link to="/">Home</Link>
                </Menu.Item>
                <Menu.Item name='Add Privacy Policy'>
                    <Link to="/add+policy">Add Privacy Policy</Link>
                </Menu.Item>
                <Menu.Item name='List Privacy Policy'>
                    <Link to="/list+policy">List Privacy Policy</Link>
                </Menu.Item>
            </Menu>
        </div>
    );
};

export default navbar;