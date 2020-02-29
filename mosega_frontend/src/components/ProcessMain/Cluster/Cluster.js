import React, {Component} from 'react';
import { Form, Input, Button, Message,  Dimmer, Loader, Segment, Divider } from 'semantic-ui-react';
import classes from './Cluster.css';
import Aux from '../../../hoc/Aux';
import {validateNumberField} from '../../Shared/Utils/Utils';
import * as URL from '../../../constants/URL';
import Deck from '../../Shared/CardDeck/CardDeck';
import axios from 'axios';

const options = [
    { key: 'p', text: 'Privacy Policy', value: 'policy' },
    { key: 't', text: 'Terms of Conditions', value: 'term' }

];

class Cluster extends Component {

    state = {
        clusterCount:'',
        dataType: '',
        makeRequest: null,
        clusterResult: null,
        disableButton: true
    };

    clusterCountHandler = (event) => {
        this.setState({clusterCount: event.target.value});
        console.log(this.state.clusterCount);
        this.buttonDisableChecker();
    };

    dataTypeHandler = (event, val) => {
        this.setState({dataType: val.value});
        this.buttonDisableChecker();
    };

    findClusterHandler = () => {
        if (validateNumberField(this.state.clusterCount)){
            this.setState({clusterResult: null});
            this.setState({makeRequest:true});
        }
    };

    buttonDisableChecker = () => {
      if (this.state.clusterCount !== '' && this.state.dataType !== ''){
          this.setState({disableButton:false});
      }
    };

    componentDidMount() {
        this.setState({makeRequest: null, clusterResult: null});
    }

    componentDidUpdate() {
        if (this.state.makeRequest){
            const data = {
                'processType':'cluster',
                'dataType':this.state.dataType,
                "noOfClusters":+this.state.clusterCount
            };
            axios.post(URL.PROCESSING,data)
                .then(resp => {
                    this.setState({clusterResult:resp.data, makeRequest:null});
                });
        }
    }

    render() {

        let clusterResult = <Message style={
            {textAlign:"center", marginLeft: "10px", marginRight: "10px", marginTop: "30px"}}
                                        floating>
            Please select above parameters to cluster clauses  !
        </Message>;

        if (this.state.makeRequest === true && this.state.clusterResult === null){
            clusterResult = (
                <Segment style={{marginLeft: "10px", marginRight: "10px", marginTop: "30px", height:"400px"}}>
                    <Dimmer active inverted>
                        <Loader size='large'>Loading Clustering Results ...</Loader>
                    </Dimmer>
                </Segment>
            );
        }

        if (this.state.clusterResult){
            let resultDeck = [];
            for (let i=0; i< this.state.clusterCount; i++){
                let innerCluster = this.state.clusterResult[i].map((item,index)=> (
                    <Deck
                        key={'inner_cluster_'+i+'_'+index}
                        heading={item.heading}
                        text={item.text}
                    />
                ));

                const outerCluster = (
                    <div key={'outer_cluster_'+i}>
                        <Divider horizontal style={{marginLeft:"10px", marginRight:"10px"}} > Cluster {i+1}</Divider>
                        <br/>
                        <div className={classes.ClusterResult}>
                            {innerCluster}
                        </div>
                        <br/>
                    </div>

                );
                resultDeck.push(outerCluster);
            }
            clusterResult =(
                <div style={{marginTop:"30px"}}>
                    <h2 style={{ textAlign: "center"}}>Cluster Results</h2>
                    <br/>
                    {resultDeck}
                </div>
            );
        }

        return (
            <Aux>
                <div className={classes.Cluster}>
                    <Form size='large'>
                        <Form.Select required
                                     fluid
                                     label='Type'
                                     options={options}
                                     onChange={this.dataTypeHandler}
                                     placeholder='Is it from Privacy Policy or Terms of Conditions ?'
                        />
                        <Form.Field required>
                            <label>How many clusters ? </label>
                            <Input
                                placeholder='Enter No of clusters'
                                onChange={this.clusterCountHandler}
                            />
                        </Form.Field>
                        <div className={classes.ButtonRight}>
                            <Form.Field >
                                <Button
                                    color='green'
                                    size='large'
                                    onClick={this.findClusterHandler}
                                    disabled ={this.state.disableButton}
                                >
                                    Cluster clauses
                                </Button>
                            </Form.Field>
                        </div>
                    </Form>
                </div>
                <div>
                    {clusterResult}
                </div>
            </Aux>
        );
    }
}

export default Cluster;