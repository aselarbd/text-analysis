import React from 'react';
import {Accordion, Icon} from "semantic-ui-react";
import Aux from "../../hoc/Aux";

const PolicyItem = (props) => {
    return (
        <div>
            <Accordion fluid styled>

                <Accordion.Title active index={props.index}>
                    <Icon name='dropdown'/>
                    {props.heading}
                </Accordion.Title>
                <Accordion.Content active>
                    <p>
                        test content <br/>
                        {props.text}
                    </p>
                </Accordion.Content>

            </Accordion>


        </div>
    );
};

export default PolicyItem;