import React, {Component} from 'react';
import {Message, Dimmer, Loader, Segment, Divider, Header, Button} from 'semantic-ui-react';
import CardDeck from '../../Shared/CardDeck/CardDeck';
import {connect} from 'react-redux';
import {withRouter} from 'react-router-dom';
import axios from 'axios';
import * as URL from '../../../constants/URL';
import classes from './FullPolicy.css';
import * as actionType from "../../../store/action";
import Aux from '../../../hoc/Aux';

class FullPolicy extends Component{

    state={
        loadedPolicy: null
    };

    goToURLHandler = (url) => {
        window.location.replace(url);
    };

    findSimilarSetHandler = () => {
        this.props.similarSetHandler({"ID": this.props.loadedPolicyID, "queryType":"policy"});
        this.props.history.push({
            pathname:"/similarity-set",
        });
    };

    componentDidMount() {
        this.setState({loadedPolicy: null});
        this.props.select_policy_handler(null);
    }

    componentDidUpdate() {
        if (this.props.loadedPolicyID){
            if (!this.state.loadedPolicy ||
                (this.state.loadedPolicy && this.state.loadedPolicy.id !== this.props.loadedPolicyID)){
                    const endPoint = URL.GET_ONE_POLICY + this.props.loadedPolicyID;
                    axios.get(endPoint)
                        .then(resp => {
                            this.setState({loadedPolicy: resp.data});
                        });
            }
        }
    }

    render() {
        let policy = <Message style={{textAlign:"center", marginLeft: "10px", marginRight: "10px"}} floating>
            Please select a Privacy Policy  !
        </Message>;

        if (this.props.loadedPolicyID){
            policy = (
                <Segment style={{marginLeft: "10px", marginRight: "10px", height:"400px"}}>
                    <Dimmer active inverted>
                        <Loader size='large'>Loading Policy</Loader>
                    </Dimmer>
                </Segment>
            );
        }

        if(this.state.loadedPolicy){
            const policyRes = this.state.loadedPolicy.data.map((item,index) => (
               <CardDeck key={'subPart_'+index} heading={item.heading} text={item.text} displayType="policy"/>
            ));

            policy =(
                <Aux>
                    <Segment clearing style={{marginLeft:"10px", marginRight:"10px"}}>
                        <Header as='h2' floated='left'>
                            {this.state.loadedPolicy.title}
                        </Header>
                        <Header as='h2' floated='right'>
                            <Button
                                size='big'
                                color='teal'
                                onClick={()=>this.goToURLHandler(this.state.loadedPolicy.url)}
                            >
                                Visit web site
                            </Button>
                            <Button
                                size='big'
                                color='teal'
                                onClick={this.findSimilarSetHandler}
                            >
                                Find Similar items to individual headings
                            </Button>
                        </Header>
                    </Segment>
                    <br/>
                    <Divider horizontal style={{marginLeft:"10px", marginRight:"10px", marginTop:"20px"}}>
                        Details
                    </Divider>
                    <br/>
                    {policyRes}
                </Aux>
            );
        }
        return (
            <div className={classes.FullPolicy}>
                {policy}
            </div>
        );
    }
}

const mapStateToProps = state => {
    return {
        loadedPolicyID: state.selectedPolicy.selectedPolicyID
    }
};

const mapDispatchToProps = dispatch => {
    return{
        select_policy_handler: (ID) => dispatch({type:actionType.SELECT_POLICY, selectedPolicyID:ID}),
        similarSetHandler: (queryItem) => dispatch({type:actionType.SIMILAR_SET_QUERY, payload:queryItem})
    }
};

export default withRouter(connect(mapStateToProps, mapDispatchToProps) (FullPolicy));