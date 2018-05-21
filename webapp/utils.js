
export const isEmpty = element => {
    return typeof element === 'undefined' ||
        typeof element === 'object' && Object.keys(element).length <= 0 ||   
        typeof element === 'string' && element.length <= 0 ||  
        Array.isArray(element) && element.length <= 0;
};

export const guid = () => {
    function s4() {
      return Math.floor((1 + Math.random()) * 0x10000)
        .toString(16)
        .substring(1);
    }
    return s4() + s4() + '-' + s4() + '-' + s4() + '-' + s4() + '-' + s4() + s4() + s4();
  }

export const prettyProbability = prob => {
  return `${(Number(prob) * 100).toFixed(3).replace(/\.0+$/,'')}%`
}