import * as actionType from '../action';

const initialState = {
    selectedPolicyID: null
};

const reducer = (state= initialState, action) => {
    if (action.type === actionType.SELECT_POLICY) {
        return {
            ...state,
            selectedPolicyID : action.selectedPolicyID
        };
    } else {
        return state
    }
};

export default reducer;