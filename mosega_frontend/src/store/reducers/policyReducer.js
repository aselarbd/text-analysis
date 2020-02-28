import * as actionType from '../action';

const initialState = {
    policies: []
};

const reducer = (state= initialState, action) => {
    if (action.type === actionType.LOAD_POLICIES) {
        return {
            policies: [...action.payload]
        };
    } else {
        return state
    }
};

export default reducer;