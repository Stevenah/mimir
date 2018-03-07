
export const isEmpty = element => {
    return typeof element === 'undefined' ||
        typeof element === 'object' && Object.keys(element).length <= 0 ||   
        typeof element === 'string' && element.length <= 0 ||  
        Array.isArray(element) && element.length <= 0;
};
