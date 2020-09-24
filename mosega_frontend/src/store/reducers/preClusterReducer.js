import * as actionType from '../action';

const initialState = {
    query: null,
    queryType: null,
    noOfClusters:null
};

const reducer =(state= initialState, action) => {
    if (action.type === actionType.PRE_CLUSTER_QUERY){
        return {
            query: action.payload.query,
            queryType: action.payload.queryType,
            noOfClusters: action.payload.noOfClusters
        }

    } else {
        return state
    }

};

export default reducer;