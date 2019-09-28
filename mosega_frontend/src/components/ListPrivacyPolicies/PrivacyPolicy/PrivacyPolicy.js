import React,{ useState }  from 'react';
import styles from './PrivacyPolicy.css'
import { Divider, Icon, Modal, Statistic, Button, Header } from 'semantic-ui-react'
import ReactJson from 'react-json-view'


const PrivacyPolicy = (props) => {

    const [modalState, setModalState] = useState({
        modalOpen: false
    });

    const handleOpen = () => setModalState({ modalOpen: true })

    const handleClose = () => setModalState({ modalOpen: false })


        return (
        <div>
            <Statistic.Group  widths='four' className={styles.container}>

                <Statistic>
                    <Statistic.Label>Privacy Policy</Statistic.Label>
                    <Statistic.Value><Icon name='file alternate' /></Statistic.Value>
                </Statistic>

                <Statistic size='mini'>
                    <Statistic.Label>Topic</Statistic.Label>
                    <Statistic.Value>
                        <p className={styles.custom_statics}>{props.policyTopic}</p>
                    </Statistic.Value>
                </Statistic>

                <Statistic size='mini'>
                    <Statistic.Label>URL</Statistic.Label>
                    <Statistic.Value >
                        <Button >
                            <a href={props.policyURL}> To Web Page</a>
                        </Button>
                    </Statistic.Value>
                </Statistic>

                <Statistic >
                    <Statistic.Label>More Details</Statistic.Label>

                    <Modal
                        trigger={
                            <Statistic.Value text>
                            <Button secondary onClick={handleOpen}>More</Button>
                            </Statistic.Value>
                        }
                        open={modalState.modalOpen}
                        onClose={handleClose}
                        basic
                        size='small'
                    >
                        <Header icon='browser' content='Privacy Policy' />
                        <Modal.Content>

                            <ReactJson src={props.policy} theme="monokai"/>

                            {/*<textarea className={styles.custom_textarea}*/}
                            {/*          disabled={true}*/}
                            {/*          value={JSON.stringify(props.policy, undefined, 4) }>*/}
                            {/*</textarea>*/}

                        </Modal.Content>
                        <Modal.Actions>
                            <Button color='green' onClick={handleClose} inverted>
                                <Icon name='checkmark' /> Okay
                            </Button>
                        </Modal.Actions>
                    </Modal>
                </Statistic>

            </Statistic.Group>
            <Divider/>



            {/*<Item>*/}
            {/*    <Item.Image size='huge'  >*/}
            {/*        <Icon name="file alternate" size="huge"/>*/}
            {/*    </Item.Image>*/}

            {/*    <Item.Content verticalAlign='top' >*/}
            {/*        <Item.Header >Header</Item.Header>*/}
            {/*        <Item.Description>*/}
            {/*            Description*/}
            {/*        </Item.Description>*/}
            {/*    </Item.Content>*/}
            {/*</Item>*/}




            {/*<Icon name="file alternate" size="huge"/>*/}
            {/*<span>Heading : </span>*/}
            {/*{props.policyTopic}*/}
            {/*<Divider />*/}



            {/*<textarea className={styles.custom_textarea}*/}
            {/*          disabled={true}*/}
            {/*          value={JSON.stringify(props.policy, undefined, 4) }>*/}
            {/*</textarea>*/}
        </div>
    );
};

export default PrivacyPolicy;