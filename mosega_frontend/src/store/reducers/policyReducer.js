import * as actionType from '../action';

const initialState = {
    policies: []
};

const reducer = (state= initialState, action) => {
    switch (action.type){
        case actionType.LOAD_POLICIES:
            return {
                policies: [...action.payload]
            };
        default:
            return state
    }
};

export default reducer