import React from 'react';
import Aux from '../../hoc/Aux';
import NavigationBar from './Navbar/NavigationBar';

const layout = (props) => (
    <Aux>
        <NavigationBar/>
        <main  style={{"marginTop":"20px"}}>
            {props.children}
        </main>
    </Aux>
);


export default layout;