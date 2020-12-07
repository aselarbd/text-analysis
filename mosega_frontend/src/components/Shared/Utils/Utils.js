
export const validateNumberField = (num) => {
    if (!isNaN(num)){
        return true;
    }
    alert("Please enter a valid number !");
    return false;
};

