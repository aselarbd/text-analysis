import React, {Component} from 'react';
import { Input, Button, Header, Icon, Modal } from 'semantic-ui-react';
import * as URL from '../../../constants/URL';
import axios from 'axios';
import classes from './NewPolicy.css';


class NewPolicy extends Component {

    state = {
        disableButton: false,
        url:'',
        modalOpen: false,
        success: true
    };

    urlChangeHandler = (event) => {
        this.setState({
            url: event.target.value
        });
        this.buttonDisableChecker();
    };

    buttonDisableChecker = () => {
      if (this.state.url !==''){
          this.setState({disableButton:false});
      }else{
          this.setState({disableButton:true});
      }
    };

    addNewPolicy = () => {
        if (this.state.url !== ''){
            const endPoint = URL.ADD_NEW_POLICY;
            const data = {"url": this.state.url};

            axios.post(endPoint,data).then(() => {
                this.setState({success:true});
                this.handleOpen();
            }).catch(err => {
                console.log(err);
                this.setState({success:false});
            });
        }else {
            this.buttonDisableChecker();
        }
    };

    handleOpen = () => this.setState({ modalOpen: true });

    handleClose = () => {
        this.setState({ modalOpen: false });
        window.location.reload();
    };


    render() {

        const addedSuccessfully = (
            <Modal open={this.state.modalOpen} onClose={this.handleClose} basic size='small' >

                <Header icon='browser' content='Privacy Policy Added successfully' />

                <Modal.Content>
                    <h3>Privacy Policy of following URL added to database</h3>
                    <h4>{this.state.url}</h4>
                </Modal.Content>

                <Modal.Actions>
                    <Button color='green' onClick={this.handleClose} inverted>
                        <Icon name='checkmark' /> Got it
                    </Button>
                </Modal.Actions>

            </Modal>
        );

        const errorInAddition = (
            <Modal open={this.state.modalOpen} onClose={this.handleClose} basic size='small' >

                <Header icon='exclamation' content='Error occurred !!! ' />

                <Modal.Content>
                    <h3>Error occurred while adding following Privacy Policy URL to the database</h3>
                    <h4>{this.state.url}</h4>
                </Modal.Content>

                <Modal.Actions>
                    <Button color='red' onClick={this.handleClose} inverted>
                        <Icon name='checkmark' /> Try again
                    </Button>
                </Modal.Actions>

            </Modal>
        );

        return(
            <div className={classes.NewPolicy}>

                {(this.state.success)? addedSuccessfully : errorInAddition}

                <Input
                    placeholder="Enter Privacy Policy URL"
                    type="text"
                    value={this.state.url}
                    onChange={this.urlChangeHandler}
                    style={{padding: "10px 10px", width:"80%", height:"60px"}}
                />
                <Button
                    positive
                    disabled = {!this.state.disableButton}
                    onClick = {this.addNewPolicy}
                    style = {{padding: "10px 10px",marginLeft: "20px", width:"15%", height:"40px"}}
                > Add Policy</Button>
            </div>
        );
    }
}

export default NewPolicy;