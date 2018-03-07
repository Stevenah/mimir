import store from 'store';

const handleStatus = response => {
    if (!response.ok) {
        throw Error(response.statusText);
    }

    return response;
};

const handleErrors = errors => {
    console.log(errors);
};

const getJsonOptions = () => ({
    'method': 'GET',
    'dataType': 'json',
    'Content-Type': 'application/json',
});

export const getImageVisualization = (imageId, classId, layerId) => {

    const baseUrl = store.getState().settings.api.url;

    return fetch(`${baseUrl}/api/cnn/visualize/${imageId}?classId=${classId}&layerId=${layerId}`, getJsonOptions())
        .then(handleStatus)
        .then(response => response.json())
        .then(response => response)
        .catch(handleErrors);
};

export const getImage = imageId => {

    const baseUrl = store.getState().settings.api.url;

    return fetch(`${baseUrl}/api/files/images/${imageId}`, getJsonOptions())
        .then(handleStatus)
        .then(response => response.json())
        .then(response => response)
        .catch(handleErrors);
};

export const getImages = () => {
    
    const baseUrl = store.getState().settings.api.url;
    
    return fetch(`${baseUrl}/api/files/images`, getJsonOptions())
        .then(handleStatus)
        .then(response => response.json())
        .then(response => response)
        .catch(handleErrors);
};

export const getCnnLayers = () => {

    const baseUrl = store.getState().settings.api.url;
    
    return fetch(`${baseUrl}/api/cnn/layers`, getJsonOptions())
        .then(handleStatus)
        .then(response => response.json())
        .then(response => response)
        .catch(handleErrors)
};

export const getCnnClasses = () => {

    const baseUrl = store.getState().settings.api.url;

    return fetch(`${baseUrl}/api/cnn/classes`, getJsonOptions())
        .then(handleStatus)
        .then(response => response.json())
        .then(response => response)
        .catch(handleErrors)
};

export const getCnnClassification = imageId => {

    const baseUrl = store.getState().settings.api.url;
    
    return fetch(`${baseUrl}/api/cnn/classify/${imageId}`, getJsonOptions())
        .then(handleStatus)
        .then(response => response.json())
        .then(response => response)
        .catch(handleErrors)
};