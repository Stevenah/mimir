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

const postJsonOptions = () => ({
    'method': 'POST',
    'dataType': 'json',
    'Content-Type': 'application/json',
})

const deleteOptions = () => ({
    'method': 'DELETE',
})

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

export const getRefreshCnnClassification = imageId => {
    return fetch(`/api/cnn/reclassify`, postJsonOptions())
        .then(handleStatus)
        .then(response => response.json())
        .then(response => response)
        .catch(handleErrors)
};



export const getSelectedImage = imageId => {
    return fetch(`/api/files/images/${imageId}`, getJsonOptions())
        .then(handleStatus)
        .then(response => response.json())
        .then(response => response)
        .catch(handleErrors)
};

export const getAvailableModels = () => {
    return fetch(`/api/cnn/models`, getJsonOptions())
        .then(handleStatus)
        .then(response => response.json())
        .then(response => response)
        .catch(handleErrors)
};

export const getActiveModel = () => {
    return fetch(`/api/cnn/active`, getJsonOptions())
        .then(handleStatus)
        .then(response => response.json())
        .then(response => response)
        .catch(handleErrors)
};

export const activateModel = modelId => {
    return fetch(`/api/cnn/activate/${modelId}`, postJsonOptions())
        .then(handleStatus)
        .then(response => response.json())
        .then(response => response)
        .catch(handleErrors)
};

export const deleteModel = modelId => {
    return fetch(`/api/cnn/delete/${modelId}`, deleteOptions())
        .then(handleStatus)
        .then(response => response.json())
        .then(response => response)
        .catch(handleErrors)
};