import React, {Component} from 'react';
import { Message,  Dimmer, Loader, Segment } from 'semantic-ui-react';
import SubPart from '../../Shared/Segment/Segment';
import {connect} from 'react-redux';
import axios from 'axios';
import * as URL from '../../../constants/URL';
import classes from './FullTerm.css';
import * as actionType from "../../../store/action";

class FullTerm extends Component{

    state={
        loadedTerm: null
    };

    componentDidMount() {
        this.setState({loadedTerm: null});
        this.props.selectTermHandler(null);
    }

    componentDidUpdate() {
        if (this.props.loadedTermID){
            if (!this.state.loadedTerm ||
                (this.state.loadedTerm && this.state.loadedTerm.id !== this.props.loadedTermID)){
                const endPoint = URL.GET_ONE_TERM + this.props.loadedTermID;
                axios.get(endPoint)
                    .then(resp => {
                        this.setState({loadedTerm: resp.data});
                    });
            }
        }
    }

    render() {
        let term = <Message style={{textAlign:"center", marginLeft: "10px", marginRight: "10px"}} floating>
            Please select a Term of Condition  !
        </Message>;

        if (this.props.loadedTermID){
            term = (
                <Segment style={{marginLeft: "10px", marginRight: "10px", height:"400px"}}>
                    <Dimmer active inverted>
                        <Loader size='large'>Loading Term</Loader>
                    </Dimmer>
                </Segment>
            );
        }

        if(this.state.loadedTerm){
            term = this.state.loadedTerm.data.map((item, index) => (
                <SubPart key={'subPart_'+index} heading={item.heading} text={item.text}/>
            ));
        }
        return <div className={classes.FullTerm}>{term}</div>;
    }
}

const mapStateToProps = state => {
    return {
        loadedTermID: state.selectedTerm.selectedTermID
    }
};

const mapDispatchToProps = dispath => {
    return{
        selectTermHandler: (ID) => dispath({type:actionType.SELECT_TERM, selectedTermID:ID})
    }
};

export default connect(mapStateToProps, mapDispatchToProps) (FullTerm);