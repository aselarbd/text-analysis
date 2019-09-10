import React from 'react';
import Aux from '../../hoc/Aux'
import styles from './Layout.css'
import Navbar from './Navbar/Navbar'

const layout = (props) => (
    <Aux>
        <Navbar/>
        <main className={styles.content}>
            {props.children}
        </main>
    </Aux>
);


export default layout;