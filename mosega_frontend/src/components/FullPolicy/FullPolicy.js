import React, {Component} from 'react';
import { Message,  Dimmer, Loader, Segment } from 'semantic-ui-react';
import SubPart from './Segment/Segmant';
import {connect} from 'react-redux';
import axios from 'axios';
import * as URL from '../../constants/URL';
import classes from './FullPolicy.css';

class FullPolicy extends Component{

    state={
        loadedPolicy: null
    };

    componentDidUpdate() {
        if (this.props.loadedPolicyID){
            if (!this.state.loadedPolicy ||
                (this.state.loadedPolicy && this.state.loadedPolicy.id !== this.props.loadedPolicyID)){
                    const endPoint = URL.GET_ONE_POLICY + '/' + this.props.loadedPolicyID;
                    const url = "http://www.mocky.io/v2/5e57f199300000e1ccfd3efc";
                    axios.get(url)
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
                        <Loader size='large'>Loading</Loader>
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
        loadedPolicyID: state.selected.selectedPolicyID
    }
};

export default connect(mapStateToProps, null) (FullPolicy);