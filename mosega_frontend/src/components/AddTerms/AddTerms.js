import React, {Component} from 'react';
import { Input, Button } from 'semantic-ui-react'
import styles from './AddTerms.css'
import axios from 'axios'



class AddTerms extends Component  {

    state = {
        TermAddable:false,
        url:""
    }

    backend_URL = "";

    enableTerms = (url) => {
        this.setState({TermAddable:true})

        console.log(url)
        this.setState({url:url})

        if (url === ""){
            this.setState({TermAddable:false})
        }
    }

    addNewTerms = () => {
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
                       placeholder='Add URL of a Terms & conditions'
                       onChange={(event)=> this.enableTerms(event.target.value)}
                />
                <br/><br/>
                <div className={styles.custom_button_content} >
                    <Button  className={styles.custom_button}
                             color='black'
                             disabled={!this.state.TermAddable}
                             onClick={this.addNewTerms}
                    >Add Terms & Conditions</Button></div>
            </div>
        );
    }
}

export default AddTerms;