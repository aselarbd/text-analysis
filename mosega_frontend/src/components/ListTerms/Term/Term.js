import React,{ useState }  from 'react';
import styles from './Term.css'
import { Divider, Icon, Modal, Statistic, Button, Header } from 'semantic-ui-react'
import ReactJson from 'react-json-view'


const Term = (props) => {

    const [modalState, setModalState] = useState({
        modalOpen: false
    });

    const handleOpen = () => setModalState({ modalOpen: true })

    const handleClose = () => setModalState({ modalOpen: false })


    return (
        <div>
            <Statistic.Group  widths='four' className={styles.container}>

                <Statistic>
                    <Statistic.Label>Terms & Conditions</Statistic.Label>
                    <Statistic.Value><Icon name='clipboard' /></Statistic.Value>
                </Statistic>

                <Statistic size='mini'>
                    <Statistic.Label>Topic</Statistic.Label>
                    <Statistic.Value>
                        <p className={styles.custom_statics}>{props.termTopic}</p>
                    </Statistic.Value>
                </Statistic>

                <Statistic size='mini'>
                    <Statistic.Label>URL</Statistic.Label>
                    <Statistic.Value >
                        <Button >
                            <a href={props.termURL}> To Web Page</a>
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
                        <Header icon='browser' content='Terms & Conditions' />
                        <Modal.Content>
                            <ReactJson src={props.term} theme="monokai"/>
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
        </div>
    );
};

export default Term;