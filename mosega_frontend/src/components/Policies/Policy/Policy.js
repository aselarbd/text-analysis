import React from 'react';
import { Button, Card } from 'semantic-ui-react';

const Policy = (props) => {
    return (
            <Card style={{margin: "20px"}}>
                <Card.Content>
                    <Card.Header>{props.title}</Card.Header>
                    <Card.Meta>Privacy Policy</Card.Meta>
                    <Card.Description>
                        Privacy Policy statement of <strong>{props.title}</strong>
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
                            onClick={props.viewPolicy}
                        >
                            View Policy
                        </Button>
                    </div>
                </Card.Content>
            </Card>
    );
};

export default Policy;