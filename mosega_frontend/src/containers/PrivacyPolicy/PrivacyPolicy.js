import React, {Component} from 'react';

import NewPolicy from '../../components/NewPolicy/NewPolicy'


import {connect} from 'react-redux';
import * as actionType from '../../store/action';

class PrivacyPolicy extends Component{

    render() {
        return(
            <div>
                <div>

                </div>
                <div>
                    <NewPolicy />
                </div>
                <div>

                </div>
            </div>
        );
    }
}

const mapStateToProps = state => {
  return {
      policies: state.policies.policies
  }
};

const mapDispatchToProps = dispath => {
    return{
        selectPolicy: () => dispath({type:actionType.ADD, payload: {}})
    }
};

export default connect(mapStateToProps,mapDispatchToProps) (PrivacyPolicy);