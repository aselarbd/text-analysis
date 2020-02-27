import * as actionType from '../action';

const initialState = {
    policies: []
};

//TODO: manage state
const reducer = (state= initialState, action) => {
    switch (action.type){
        case actionType.ADD:
            return {
                ...state
            };
        default:
            return state
    }
};

export default reducer