import * as actionType from '../action';

const initialState = {
    selectedTermID: null
};

const reducer = (state= initialState, action) => {
    if (action.type === actionType.SELECT_TERM) {
        return {
            ...state,
            selectedTermID : action.selectedTermID
        };
    } else {
        return state
    }
};

export default reducer;