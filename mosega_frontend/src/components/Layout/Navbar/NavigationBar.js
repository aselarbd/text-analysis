import React, {Component} from 'react';
import { Menu } from 'semantic-ui-react'
import {withRouter} from "react-router-dom";

class NavigationBar extends Component {

    state= {};


    handleItemClick = (e, { name }) => {
        this.setState({ activeItem: name });
        this.props.history.push({pathname:"/"+name});
    };

    render() {

        const { activeItem } = this.state;

        return(
            <div>
                <Menu inverted color='black' size='massive'>
                    <Menu.Item
                        name='policy'
                        active={activeItem === 'policy'}
                        onClick={this.handleItemClick}
                    >
                        Privacy Policy
                    </Menu.Item>

                    <Menu.Item
                        name='term'
                        active={activeItem === 'term'}
                        onClick={this.handleItemClick}
                    >
                        Terms and Conditions
                    </Menu.Item>

                    <Menu.Item
                        name='process'
                        active={activeItem === 'process'}
                        onClick={this.handleItemClick}
                    >
                        Processing
                    </Menu.Item>

                    <Menu.Menu position='right'>

                        <Menu.Item
                            name='login'
                            active={activeItem === 'login'}
                            onClick={this.handleItemClick}
                        >
                            Log In
                        </Menu.Item>
                    </Menu.Menu>
                </Menu>
            </div>
        );
    }
}

export default withRouter(NavigationBar);