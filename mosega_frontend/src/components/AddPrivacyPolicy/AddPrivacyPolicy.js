import React, {Component} from 'react';
import { Input, Button } from 'semantic-ui-react'
import styles from './AddPrivacyPolicy.css'
import axios from 'axios'

class addPrivacyPolicy extends Component  {

    state = {
        policyAddable:false,
        url:""
    }

    backend_URL = 'http://127.0.0.1:8000/PrivacyPolicyAPI/api/v1/PrivacyPolicy/'

    enablePrivacyPolicy = (url) => {
        this.setState({policyAddable:true})

        console.log(url)
        this.setState({url:url})

        if (url === ""){
            this.setState({policyAddable:false})
        }
    }

    addNewPrivacyPolicy = () => {
        const url = this.state.url
        const data = {"url":url}
        //TODO : make the POST call to backend
        axios.post(this.backend_URL, data)
            .then(
                response => {
                    console.log(response)
                }
            );


    }



    render() {
        return (
            <div>
                <Input className={styles.input}
                       size='huge'
                       placeholder='Add URL of a Privacy Policy'
                       onChange={(event)=> this.enablePrivacyPolicy(event.target.value)}
                />
                <br/><br/>
                <div className={styles.custom_button_content} >
                    <Button  className={styles.custom_button}
                             color='black'
                             disabled={!this.state.policyAddable}
                             onClick={this.addNewPrivacyPolicy}
                        >Add Policy</Button></div>
            </div>
        );
    }
}

export default addPrivacyPolicy;