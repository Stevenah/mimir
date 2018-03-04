import * as action from 'constants';

export const actionCreator = type => 
    (payload={}, meta={}, error={}) => ({
            type,
            payload,
            meta,
            error,
    });

export const requestImageAnalysis = imageId => {
    return actionCreator(action.REQUEST_IMAGE_ANALYSIS)({
        imageId
    });
}

export const receiveImageAnalysis = imageId =>
    actionCreator(action.RECEIVE_IMAGE_ANALYSIS)({
        imageId
    });

export const rejectImageAnalysis = error =>
    actionCreator(action.REJECT_IMAGE_ANALYSIS)({
        error,
    });

export const selectVisualizationTarget = targetId => 
    actionCreator(action.SELECT_VISUALIZATION_TARGET)({
        targetId,
    });

export const selectVisualizationLayer = layerId => 
    actionCreator(action.SELECT_VISUALIZATION_LAYER)({
        layerId,
    });

export const selectFile = fileId =>
    actionCreator(action.SELECT_FILE)({
        fileId,
    });

export const attachFile = file =>
    actionCreator(action.ATTACH_FILE)({
        file,
    });

export const detachFile = file =>
    actionCreator(action.DETACH_FILE)({
        file,
    });
    
export const updateField = (field, value) =>
    actionCreator(action.EDIT_FIELD)({
        field, value,
    });

export const openModal = active =>
    actionCreator(action.OPEN_MODAL)({
        active,
    });

export const closeModal = error =>
    actionCreator(action.CLOSE_MODAL)({

    });

export const setApiUrl = apiUrl =>
    actionCreator(action.SET_API_URL)({
        apiUrl,
    })

export const requestFileUpload = () => ({
    type: action.REQUEST_FILE_UPLOAD
})

export const requestFileRefresh = () => ({
    type: action.REQUEST_FILE_REFRESH,
})

export const receiveFileRefresh = files =>
    actionCreator(action.RECEIVE_FILE_REFRESH)({
        files,
    });

export const rejectFileRefresh = error =>
    actionCreator(action.REJECT_FILE_REFRESH)({
        error,
    });

export const selectCnnClass = classId => {
    return actionCreator(action.SELECT_CNN_CLASS)({
        classId,
    });
}

export const selectCnnLayer = layerId => {
    return actionCreator(action.SELECT_CNN_LAYER)({
        layerId,
    });
}

export const requestCnnClasses = () => {
    return actionCreator(action.REQUEST_CNN_CLASSES)({ });
}
    
export const requestCnnLayers = () => {
    return actionCreator(action.REQUEST_CNN_LAYERS)({ });
}

export const receiveCnnClasses = classes => {
    return actionCreator(action.RECEIVE_CNN_CLASSES)({
        classes,
     });
}
    
export const receiveCnnLayers = layers => {
    return actionCreator(action.RECEIVE_CNN_LAYERS)({
        layers,
    });
}

export const requestImageVisualizations = (imageId, classId, layerId) => {
    return actionCreator(action.RECEIVE_IMAGE_VISUALIZATIONS)({
        imageId, classId, layerId
    });
}

export const requestCnnClassification = (imageId) => {
    return actionCreator(action.REQUEST_CNN_CLASSIFICATION)({
        imageId,
    });
}

export const receiveCnnClassification = (imageId, classification) => {
    return actionCreator(action.RECEIVE_CNN_CLASSIFICATION)({
        classification, imageId
    });
}

export const updateFileSelection = () => {
    return actionCreator(action.UPDATE_FILE_SELECTION)({ });
}

export const requestSelectedVisualization = () => {
    return actionCreator(action.REQUEST_SELECTED_VISUALIZATIONS)({ });
}

export const receiveVisualizations = (visualizations, imageId, classId, layerId) => {
    return actionCreator(action.RECEIVE_SELECTED_VISUALIZATIONS)({
        imageId: `${imageId}-${classId}-${layerId}`,
        ...visualizations, classId, layerId
    });
}

export const updateVisualizations = () => {
    return actionCreator(action.UPDATE_SELECTED_VISUALIZATIONS)({ });
}