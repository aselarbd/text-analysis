import * as actionType from '../action';

const initialState = {
    terms: []
};

const reducer = (state= initialState, action) => {
    if (action.type === actionType.LOAD_TERMS) {
        return {
            ...state,
            terms: [...action.payload]
        };
    } else {
        return state;
    }
};

export default reducer;