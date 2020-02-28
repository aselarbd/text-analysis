import React from 'react';
import { Card } from 'semantic-ui-react';

const segment = (props) => {
    return <Card
        header={props.heading}
        meta={props.meta}
        description={props.text}
        fluid
        style ={{"margin":"10px", "width":"98%"}}
    />;
};

export default segment;