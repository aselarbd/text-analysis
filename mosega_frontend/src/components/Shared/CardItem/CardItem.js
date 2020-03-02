import React from 'react';
import { Button, Card } from 'semantic-ui-react';

const cardItem = (props) => {
    return (
        <Card style={{margin: "20px"}}>
            <Card.Content>
                <Card.Header>{props.title}</Card.Header>
                <Card.Meta>{props.dataType}</Card.Meta>
                <Card.Description>
                    {props.dataType} statement of <strong>{props.title}</strong>
                </Card.Description>
            </Card.Content>
            <Card.Content extra>
                <div className='ui two buttons'>
                    <Button
                        basic
                        color='green'
                        onClick={props.goToURL}
                    >
                        Go To Site
                    </Button>
                    <Button
                        basic
                        color='blue'
                        onClick={props.viewItem}
                    >
                        {props.buttonText}
                    </Button>
                </div>
            </Card.Content>
        </Card>
    );
};

export default cardItem;