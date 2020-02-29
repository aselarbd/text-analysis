import React, {Component} from 'react';
import {Button, Dimmer, Form, Input, Loader, Message, Segment, Divider} from 'semantic-ui-react';
import classes from './Similarity.css';
import Aux from '../../../hoc/Aux';
import Deck from '../../Shared/CardDeck/CardDeck';
import {validateNumberField} from '../../Shared/Utils/Utils';
import * as URL from '../../../constants/URL';
import axios from 'axios';

const options = [
    { key: 'p', text: 'Privacy Policy', value: 'policy' },
    { key: 't', text: 'Terms of Conditions', value: 'term' }

];

class Similarity extends Component {
    state = {
        clauses:'',
        query:'',
        dataType: '',
        makeRequest: null,
        similarResult: null,
        disableButton: true
    };

    similarityQueryHandler =(event) => {
        this.setState({query: event.target.value});
        this.buttonDisableChecker();
    };

    noClausesHandler = (event) => {
        this.setState({clauses: event.target.value});
        this.buttonDisableChecker();
    };

    dataTypeHandler = (event,val) => {
        this.setState({dataType: val.value});
        this.buttonDisableChecker();
    };

    findSimilarityHandler = () => {
        if (this.state.clauses !=='' && this.state.query !== '' && this.state.dataType !==''){
            if (validateNumberField(this.state.clauses)){
                this.setState({similarResult: null});
                this.setState({makeRequest:true});
            }
        }else{
            this.buttonDisableChecker();
        }
    };

    buttonDisableChecker = () => {
        if (this.state.clauses !== '' && this.state.dataType !== '' && this.state.query !== ''){
            this.setState({disableButton:false});
        }
        else {
            this.setState({disableButton:true});
        }
    };

    componentDidMount() {
        this.setState({makeRequest: null, similarResult: null});
    }

    componentDidUpdate() {
        if (this.state.makeRequest){

            const data = {
                "processType":"similar",
                "dataType":this.state.dataType,
                "query": this.state.query,
                "clauses": +this.state.clauses
            };

            axios.post(URL.PROCESSING,data)
                .then(resp => {
                    this.setState({similarResult:resp.data, makeRequest: null});
                });
        }
    }

    render() {

        let similarityResult = <Message style={
            {textAlign:"center", marginLeft: "10px", marginRight: "10px", marginTop: "30px"}}
                                        floating>
            Please select above parameters to get similarity clauses  !
        </Message>;

        if (this.state.makeRequest === true && this.state.similarResult === null){
            similarityResult = (
                <Segment style={{marginLeft: "10px", marginRight: "10px", marginTop: "30px", height:"400px"}}>
                    <Dimmer active inverted>
                        <Loader size='large'>Loading Similarity Results ...</Loader>
                    </Dimmer>
                </Segment>
            );
        }

        if (this.state.similarResult){
            const resultDeck = this.state.similarResult.map((item,index) => (
                <div key={'similar_part_'+index}>
                    <Divider horizontal style={{marginLeft:"10px", marginRight:"10px"}}> {index + 1}</Divider>
                    <br/>
                    <Deck
                        heading={item.heading}
                        text={item.text}
                        meta={'Accuracy : '+item.accuracy.toFixed(4)}
                    />
                    <br/>
                </div>

                ));
            similarityResult = (
                <div className={classes.SimilarityResult}>
                    <h2 style={{ textAlign: "center"}}>Similarity Results</h2>
                    <br/>
                    {resultDeck}
                </div>
            );
        }

        return (
            <Aux>
                <div className={classes.Similarity}>
                    <Form size='large'>
                        <Form.Select required
                            fluid
                            label='Type'
                            options={options}
                            onChange={this.dataTypeHandler}
                            placeholder='Is it from Privacy Policy or Terms of Conditions ?'
                        />
                        <Form.Field required>
                            <label>Similarity Query</label>
                            <Input
                                placeholder='Enter Similarity query'
                                value={this.state.query}
                                onChange={this.similarityQueryHandler}
                            />
                        </Form.Field>
                        <Form.Field required>
                            <label>How many similar clauses  you need ? </label>
                            <Input
                                placeholder='Enter No of clauses'
                                value={this.state.clauses}
                                onChange={this.noClausesHandler}
                            />
                        </Form.Field>
                        <div className={classes.ButtonRight}>
                            <Form.Field >
                                <Button
                                    color='green'
                                    size='large'
                                    onClick={this.findSimilarityHandler}
                                    disabled ={this.state.disableButton}
                                >
                                    Find Similar clauses
                                </Button>
                            </Form.Field>
                        </div>
                    </Form>
                </div>
                <div>
                    {similarityResult}
                </div>
            </Aux>
        );
    }
}

export default Similarity;