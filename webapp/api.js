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
    return fetch(`/api/cnn/visualize/${imageId}?classId=${classId}&layerId=${layerId}`, getJsonOptions())
        .then(handleStatus)
        .then(response => response.json())
        .then(response => response)
        .catch(handleErrors);
};

export const getImage = imageId => {
    return fetch(`/api/files/images/${imageId}`, getJsonOptions())
        .then(handleStatus)
        .then(response => response.json())
        .then(response => response)
        .catch(handleErrors);
};

export const getImages = () => {
    return fetch(`/api/files/images`, getJsonOptions())
        .then(handleStatus)
        .then(response => response.json())
        .then(response => response)
        .catch(handleErrors);
};

export const getCnnLayers = () => {
    return fetch(`/api/cnn/layers`, getJsonOptions())
        .then(handleStatus)
        .then(response => response.json())
        .then(response => response)
        .catch(handleErrors)
};

export const getCnnClasses = () => {
    return fetch(`/api/cnn/classes`, getJsonOptions())
        .then(handleStatus)
        .then(response => response.json())
        .then(response => response)
        .catch(handleErrors)
};

export const getCnnClassification = imageId => {
    return fetch(`/api/cnn/classify/${imageId}`, getJsonOptions())
        .then(handleStatus)
        .then(response => response.json())
        .then(response => response)
        .catch(handleErrors)
};