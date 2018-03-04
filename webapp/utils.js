
export const isEmpty = element =>
    typeof element === 'undefined' ||
    typeof element === 'object' && Object.keys(element).length <= 0 ||   
    typeof element === 'string' && element.length <= 0 ||  
    Array.isArray(element) && element.length <= 0

export const prepareBase64Image = image => 
    image ? `data:image/jpeg;base64,${image}` : '';

export const getFile = (fileId, state) =>
    state.file.files[fileId] ? 
        state.file.files[fileId] : {};

export const getLayerVisualization = (fileId, target, layerId, state) =>
    fileId && target && layerId && state ? 
        state.file.files[fileId].visualization[0][target][layerId].gradcam : {};

export const guid = () => {
    const s4 = () => {
        return Math.floor((1 + Math.random()) * 0x10000)
            .toString(16)
            .substring(1);
    }

    return s4() + s4() + '-' + s4() + '-' + s4() + '-' +
        s4() + '-' + s4() + s4() + s4();
};

export function dataURLtoFile(dataurl, filename) {
    var arr = dataurl.split(','), mime = arr[0].match(/:(.*?);/)[1],
        bstr = atob(arr[1]), n = bstr.length, u8arr = new Uint8Array(n);
    while (n--) {
        u8arr[n] = bstr.charCodeAt(n);
    }
    return new File([u8arr], filename, {type:mime});
};

export const getSelectedFileFromState = state => {
    return state.file.files[state.file.selected] ? 
        state.file.files[state.file.selected] : {}
};

const createMarkers = markerData => {
    return markerData.filter(marker => marker.prediction['dog'] * 1000 < marker.prediction['cat']  * 1000)
        .map(marker => ({
            time: (marker.time / 1000),
            text: "cat",
        }));
};

const prepareFiles = files => {
    return files.map(file => ({
        name: file.name,
        type: file.type,
        thumbnail: file.thumbnail,
    }))
}