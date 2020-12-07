import * as actionType from '../action';

const initialState = {
    ID: null,
    queryType: null,
};

const reducer =(state= initialState, action) => {
    if (action.type === actionType.SIMILAR_SET_QUERY){
        return {
            ID: action.payload.ID,
            queryType: action.payload.queryType
        }

    } else {
        return state
    }

};

export default reducer;