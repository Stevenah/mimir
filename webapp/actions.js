import * as action from 'actionConstants';

export const actionCreator = type =>
    (payload={}, meta={}, error={}) => ({
            type,
            payload,
            meta,
            error,
    });

//

export const requestImageVisualization = (imageId, layerId, classId) => {
    return actionCreator(action.REQUEST_IMAGE_VISUALIZATION)({
        imageId,
        layerId,
        classId
    });
};

export const receiveImageVisualization = (response, imageId, layerId, classId) => {
    return actionCreator(action.RECEIVE_IMAGE_VISUALIZATION)({
        'gradCam': response.gradCam,
        'guidedGradCam': response.guidedGradCam,
        imageId: `${imageId}-${classId}-${layerId}`,
        layerId,
        classId,
    });
};

export const rejectImageVisualization = error => {
    return actionCreator(action.REJECT_IMAGE_VISUALIZATION)({
        error,
    });
};

//

export const requestImages = () => ({
    type: action.REQUEST_IMAGES,
});

export const receiveImages = response => {
    const images = response.images.reduce((images, image) => {
        images[image.id] = {
            id: image.id,
            label: image.label,
            prediction: image.prediction,
            classIndex: image.classIndex,
            source: 'data:image/jpeg;base64,' + image.source,
            selected: false,
            loading: false,
            attached: false,
            type: 'image',
        }
        return images
    }, {})

    return actionCreator(action.RECEIVE_IMAGES)({
        images,
    });
};

export const rejectImages = error => {
    return actionCreator(action.REJECT_IMAGES)({
        error,
    });
};

//

export const requestCnnClasses = () => ({
    type: action.REQUEST_CNN_CLASSES,
});

export const receiveCnnClasses = response => {
    return actionCreator(action.RECEIVE_CNN_CLASSES)({
        'classes': response.classes,
     });
};

export const rejectCnnClasses = error => {
    return actionCreator(action.REJECT_CNN_CLASSES)({
        error,
     });
};

export const selectCnnClass = classId => {
    return actionCreator(action.SELECT_CNN_CLASS)({
        classId,
    });
};

//

export const requestCnnLayers = () => ({
    type: action.REQUEST_CNN_LAYERS,
});

export const receiveCnnLayers = response => {
    return actionCreator(action.RECEIVE_CNN_LAYERS)({
        'layers': response.layers,
    });
};

export const rejectCnnLayers = error => {
    return actionCreator(action.REJECT_CNN_LAYERS)({
        error,
    });
};

export const selectCnnLayer = layerId => {
    return actionCreator(action.SELECT_CNN_LAYER)({
        layerId,
    });
};

//

export const requestCnnClassification = (imageId) => {
    return actionCreator(action.REQUEST_CNN_CLASSIFICATION)({
        imageId,
    });
};

export const receiveCnnClassification = (response, imageId) => {
    return actionCreator(action.RECEIVE_CNN_CLASSIFICATION)({
        'classification': response.classification,
        imageId,
    });
};

export const rejectCnnClassification = error => {
    return actionCreator(action.REJECT_CNN_CLASSIFICATION)({
        error,
    });
};

//

export const attachFile = imageId => {
    return actionCreator(action.ATTACH_FILE)({
        imageId,
    });
};

export const detachFile = imageId => {
    return actionCreator(action.DETACH_FILE)({
        imageId,
    });
};

//

export const selectFile = fileId => {
    return actionCreator(action.SELECT_FILE)({
        fileId,
    });
};
    
export const setTextField = (field, value) => {
    return actionCreator(action.SET_TEXT_FIELD)({
        field, value,
    });
};

export const setApiUrl = apiUrl => {
    return actionCreator(action.SET_API_URL)({
        apiUrl,
    });
};

export const requestFileUpload = () => ({
    type: action.REQUEST_FILE_UPLOAD,
});

export const requestSelectedImage = imageId => {
    return actionCreator(action.REQUEST_SELECTED_IMAGE)({
        imageId,
    })
}

export const receiveSelectedImage = response => {
    return actionCreator(action.RECEIVE_SELECTED_IMAGE)({
        source: 'data:image/jpeg;base64,' + response.image,
    })
}

export const requestAvailableModels = () => ({
    type: action.REQUEST_AVAILABLE_MODELS,
});

export const receiveAvailableModels = response => {
    return actionCreator(action.RECEIVE_AVAILABLE_MODELS)({
        models: response.models,
    })
}

export const requestModelActivation = modelId => {
    return actionCreator(action.REQUEST_MODEL_ACTIVATION)({
        modelId, 
    });
}

export const receiveModelActivation = response => {
    return actionCreator(action.RECEIVE_MODEL_ACTIVATION)({
        model: response.model, 
    });
}

export const requestActiveModel = () => ({
    type: action.REQUEST_ACTIVE_MODEL,
});

export const receiveActiveModel = response => {
    return actionCreator(action.RECEIVE_ACTIVE_MODEL)({
        model: response.model,
    });
}


// export const requestUploadModel = () => ({
//     type: action.REQUEST_UPLOAD_MODEL,
// });

// export const receiveUploadModel = response => {
//     return actionCreator(action.RECEIVE_UPLOAD_MODEL)({
//         modelId: response.modelId,
//     });
// }

/** 
 * START - DELETE MODEL ACTIONS
 */

export const requestDeleteModel = modelId => {
    return actionCreator(action.REQUEST_DELETE_MODEL)({
        modelId
    });
}

export const receiveDeleteModel = response => {
    return actionCreator(action.RECEIVE_DELETE_MODEL)({
        response
    });
}

/**
 * END - DELETE MODEL ACTIONS
 */


/** 
 * START - UPLOAD MODEL ACTIONS
 */

export const requestUploadModel = () => ({
    type: action.REQUEST_UPLOAD_MODEL
});

export const receiveUploadModel = () => ({
    type: action.RECEIVE_UPLOAD_MODEL
});

/**
 * END - UPLOAD MODEL ACTIONS
 */

export const openModal = modalId => {
    return actionCreator(action.OPEN_MODAL)({
        modalId,
    });
}

export const closeModal = () => ({
    type: action.CLOSE_MODAL,
})  

export const selectCLassFilter = classFilterId => {
    return actionCreator(action.SELECT_CLASS_FILTER)({
        classFilter: classFilterId,
    });
}