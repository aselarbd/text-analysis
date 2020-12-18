import * as actionType from '../action';

const initialState = {
    queryCheck:false,
    query: null,
    queryType: null,
    processType: null,
    itemID:null
};

const reducer =(state= initialState, action) => {
    if (action.type === actionType.ADD_SIMILARITY_QUERY){
        return {
            queryCheck:true,
            query: action.payload.query,
            queryType: action.payload.queryType,
            processType: action.payload.processType,
            itemID: action.payload.itemID
        }

    } else if (action.type === actionType.REMOVE_SIMILARITY_QUERY){
        return {
            queryCheck:false,
            query: null,
            queryType: null,
            processType: null,
            itemID:null
        }
    }else {
        return state
    }

};

export default reducer;