import axios from 'axios';
import * as URL from '../../../constants/URL';

export const validateNumberField = (num) => {
    if (!isNaN(num)){
        return true;
    }
    alert("Please enter a valid number !");
    return false;
};

export const  deleteItems = (item_type, item_id) => {
    if (item_type ==="policy"){
        const END_POINT = URL.DELETE_ONE_POLICY +item_id;
        axios.delete(END_POINT)
            .then( () => window.location.reload()
            );
    }
    if (item_type ==="term"){
        const END_POINT = URL.DELETE_ONE_TERM +item_id;
        axios.delete(END_POINT)
            .then( () => window.location.reload()
            );
    }
}

