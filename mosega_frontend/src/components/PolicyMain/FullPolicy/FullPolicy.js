import React, {Component} from 'react';
import { Message,  Dimmer, Loader, Segment } from 'semantic-ui-react';
import SubPart from '../../Shared/Segment/Segment';
import {connect} from 'react-redux';
import axios from 'axios';
import * as URL from '../../../constants/URL';
import classes from './FullPolicy.css';
import * as actionType from "../../../store/action";

class FullPolicy extends Component{

    state={
        loadedPolicy: null
    };

    componentDidMount() {
        this.setState({loadedPolicy: null});
        this.props.selectPolicyHandler(null);
    }

    componentDidUpdate() {
        if (this.props.loadedPolicyID){
            if (!this.state.loadedPolicy ||
                (this.state.loadedPolicy && this.state.loadedPolicy.id !== this.props.loadedPolicyID)){
                    const endPoint = URL.GET_ONE_POLICY + '/' + this.props.loadedPolicyID;
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
            policy = this.state.loadedPolicy.data.map((item,index) => (
               <SubPart key={'subPart_'+index} heading={item.heading} text={item.text}/>
            ));
        }
        return <div className={classes.FullPolicy}>{policy}</div>;
    }
}

const mapStateToProps = state => {
    return {
        loadedPolicyID: state.selectedPolicy.selectedPolicyID
    }
};

const mapDispatchToProps = dispath => {
    return{
        selectPolicyHandler: (ID) => dispath({type:actionType.SELECT_POLICY, selectedPolicyID:ID})
    }
};

export default connect(mapStateToProps, mapDispatchToProps) (FullPolicy);