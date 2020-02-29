import React from 'react';
import { Card } from 'semantic-ui-react';

const cardDeck = (props) => {
    return <Card
        header={props.heading}
        meta={props.meta}
        description={props.text}
        fluid
        style ={{"margin":"10px", "width":"98%"}}
    />;
};

export default cardDeck;