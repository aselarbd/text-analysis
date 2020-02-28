import React from 'react';
import { Button, Card } from 'semantic-ui-react';

const Term = (props) => {
    return (
        <Card style={{margin: "20px"}}>
            <Card.Content>
                <Card.Header>{props.title}</Card.Header>
                <Card.Meta>Terms of Conditions</Card.Meta>
                <Card.Description>
                    Terms of Conditions statement of <strong>{props.title}</strong>
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
                        onClick={props.viewTerm}
                    >
                        View Term
                    </Button>
                </div>
            </Card.Content>
        </Card>
    );
};

export default Term;