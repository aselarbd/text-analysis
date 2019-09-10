import React from 'react';
import { Menu } from 'semantic-ui-react'

const navbar = () => {
    return (
        <div>
            <Menu inverted size='huge'>
                <Menu.Item
                    name='Home'
                />
                <Menu.Item
                    name='Add Privacy Policy'
                />
                <Menu.Item
                    name='List Privacy Policy'
                />
            </Menu>
        </div>
    );
};

export default navbar;