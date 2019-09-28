import React from 'react';
import { Menu,Dropdown, Button } from 'semantic-ui-react'
import {Link} from "react-router-dom";
import styles from "./Navbar.css"

const navbar = () => {
    return (
        <div >
            <Menu  size='huge'  color='teal'>
                <Menu.Item  name='Home' >
                    <Button color='teal' >
                        <Link className={styles.textColor} to="/">Home</Link>
                    </Button>
                </Menu.Item>


                {/*Dropdown for Privacy Policy*/}

                <Menu.Item>
                    <Dropdown
                        text='Privacy Policy'
                        className='button teal'
                    >
                        <Dropdown.Menu className='button '>
                            <Dropdown.Header content='Privacy Policy Operations' />
                            <Dropdown.Divider />
                            <Dropdown.Item >
                                <Link to="/add+policy">Add Privacy Policy</Link>
                            </Dropdown.Item>
                            <Dropdown.Divider />
                            <Dropdown.Item>
                                <Link to="/list+policy">List Privacy Policy</Link>
                            </Dropdown.Item>
                            <Dropdown.Divider />
                        </Dropdown.Menu>
                    </Dropdown>
                </Menu.Item>

                {/*Dropdown for Terms & Conditions*/}

                <Menu.Item>
                    <Dropdown
                        text='Terms & Conditions'
                        className='button teal'
                    >
                        <Dropdown.Menu className='button '>
                            <Dropdown.Header content='Terms & Conditions Operations' />
                            <Dropdown.Divider />
                            <Dropdown.Item >
                                <Link to="/add+terms">Add Terms & Conditions</Link>
                            </Dropdown.Item>
                            <Dropdown.Divider />
                            <Dropdown.Item>
                                <Link to="/list+terms">List Terms & Conditions</Link>
                            </Dropdown.Item>
                            <Dropdown.Divider />
                        </Dropdown.Menu>
                    </Dropdown>
                </Menu.Item>


            </Menu>
        </div>
    );
};

export default navbar;