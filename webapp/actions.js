import * as action from 'actionTypes';

export const actionCreator = type => {
    return (payload={}, meta={}, error={}) => ({
        type, payload, meta, error,
    });
}

export const openModal = modalId => { return actionCreator(action.OPEN_MODAL)(modalId); }
export const closeModal = () => { return actionCreator(action.CLOSE_MODAL)(); }

export const selectLayer = layerId => { return actionCreator(action.SELECT_LAYER)(layerId); }
export const selectClass = classId => { return actionCreator(action.SELECT_CLASS)(classId); }
export const selectImage = imageId => { 
    return actionCreator(action.SELECT_IMAGE)(imageId); 
}

export const requestNetworkLayers = modelId => { return actionCreator(action.REQUEST_NETWORK_LAYERS)(modelId); };
export const receiveNetworkLayers = response => { return actionCreator(action.RECEIVE_NETWORK_LAYERS)(response); };
export const rejectNetworkLayers = () => { return actionCreator(action.REJECT_NETWORK_LAYERS)(); };

export const requestNetworkClasses = modelId => { return actionCreator(action.REQUEST_NETWORK_CLASSES)(modelId); };
export const receiveNetworkClasses = response => { return actionCreator(action.RECEIVE_NETWORK_CLASSES)(response); };
export const rejectNetworkClasses = () => { return actionCreator(action.REJECT_NETWORK_CLASSES)(); };

export const requestImages = () => { return actionCreator(action.REQUEST_IMAGES)(); };
export const rejectImages = response => { return actionCreator(action.REJECT_IMAGES)(response); };
export const receiveImages = response => {
    return actionCreator(action.RECEIVE_IMAGES)(response.reduce((obj, item) => {
        obj[item.id] = item
        return obj
    }, {}));
};

export const requestImageUpload = formData => { return actionCreator(action.REQUEST_IMAGE_UPLOAD)(formData); };
export const receiveImageUpload = () => { return actionCreator(action.RECEIVE_IMAGE_UPLOAD)(); };
export const rejectImageUpload = () => { return actionCreator(action.REJECT_IMAGE_UPLOAD)(); };

export const requestImageClassification = () => { return actionCreator(action.REQUEST_IMAGE_CLASSIFICATION)(); };
export const receiveImageClassification = () => { return actionCreator(action.RECEIVE_IMAGE_CLASSIFICATION)(); };
export const rejectImageClassification = () => { return actionCreator(action.REJECT_IMAGE_CLASSIFICATION)(); };

export const rejectGradCam = () => { return actionCreator(action.REJECT_GRADCAM)(); };

export const requestGradCam = (imageId, layerId, classId) => {
    return actionCreator(action.REQUEST_GRADCAM)({
        imageId: imageId, class: classId, layer: layerId,
    }); 
};

export const receiveGradCam = response => {  
    return actionCreator(action.RECEIVE_GRADCAM)(response) 
};


export const requestGuidedGradCam = (imageId, layerId, classId) => {
    return actionCreator(action.REQUEST_GUIDED_GRADCAM)({
        imageId: imageId, class: classId, layer: layerId,
    });
};

export const receiveGuidedGradCam = response => {
    return actionCreator(action.RECEIVE_GUIDED_GRADCAM)(response);
};

export const rejectGuidedGradCam = () => { return actionCreator(action.REJECT_GUIDED_GRADCAM)(); };