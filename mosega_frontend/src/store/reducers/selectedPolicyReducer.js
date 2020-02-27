import * as actionType from '../action';

const initialState = {
    selectedPolicyID: null
};

const reducer = (state= initialState, action) => {
    switch (action.type){
        case actionType.SELECT_POLICY:
            return {
                ...state,
                selectedPolicyID : action.selectedPolicyID
            };
        default:
            return state
    }
};

export default reducer