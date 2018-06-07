import * as api from 'api';
import * as types from 'actionConstants';
import * as actions from 'actions'; 
import { ajax } from 'rxjs/observable/dom/ajax';
import { Observable } from 'rxjs';

import 'rxjs/add/operator/concatMap';

export const requestImages = action$ => {
    return action$.ofType(types.REQUEST_IMAGES)
        .concatMap(action => api.getImages()
            .then(response => actions.receiveImages(response))
            .catch(error => actions.rejectImages(error)));
};

export const requestCnnLayers = action$ => {
    return action$.ofType(types.REQUEST_CNN_LAYERS)
        .concatMap(action => api.getCnnLayers()
            .then(response => actions.receiveCnnLayers(response))
            .catch(error => actions.rejectCnnLayers(error)));
};

export const requestCnnClasses = action$ => {
    return action$.ofType(types.REQUEST_CNN_CLASSES)
        .concatMap(action => api.getCnnClasses()
            .then(response => actions.receiveCnnClasses(response))
            .catch(error => actions.rejectCnnClasses(error)));
};

export const requestCnnClassification = action$ => {
    return action$.ofType(types.REQUEST_CNN_CLASSIFICATION)
        .concatMap(({payload: { imageId }}) => api.getCnnClassification(imageId)
            .then(response => actions.receiveCnnClassification(response, imageId))
            .catch(error => actions.rejectCnnClassification(error)));
};

export const requestCnnClassificationRefresh = action$ => {
    return action$.ofType(types.REQUEST_MODEL_ACTIVATION)
        .concatMap(() => 
            api.getRefreshCnnClassification()
                .then(response => actions.requestImages())
                .catch(error => actions.rejectRefreshCnnClassification(error)));
};

export const requestImageVisualization = (action$, store) => {
    return action$.ofType(types.REQUEST_IMAGE_VISUALIZATION)
        .concatMap(({payload: { imageId, layerId, classId }}) =>
            api.getImageVisualization(imageId, classId, store.getState().cnn.layers[layerId])
                .then(response => actions.receiveImageVisualization(response, imageId, classId, layerId))
                .catch(error => actions.rejectImageVisualization(error)));
};

export const requestSelectedImage = action$ => {
    return action$.ofType(types.REQUEST_SELECTED_IMAGE)
        .concatMap(({payload: { imageId }}) =>
            api.getSelectedImage(imageId)
                .then(response => actions.receiveSelectedImage(response, imageId))
                .catch(error => actions.rejectSelectedImage(error)));
};

export const requestAvailableModels = action$ => {
    return action$.ofType(types.REQUEST_AVAILABLE_MODELS)
        .concatMap(() =>
            api.getAvailableModels()
                .then(response => actions.receiveAvailableModels(response))
                .catch(error => actions.rejectAvailableModels(error)));
};

export const requestActiveModel = action$ => {
    return action$.ofType(types.REQUEST_ACTIVE_MODEL)
        .concatMap(() =>
            api.getActiveModel()
                .then(response => actions.receiveActiveModel(response))
                .catch(error => actions.rejectActiveModel(error)));
};

export const requestModelActivation = action$ => {
    return action$.ofType(types.REQUEST_MODEL_ACTIVATION)
        .concatMap( ( { payload: { modelId } } ) =>
            api.activateModel(modelId)
                .then(response => actions.receiveModelActivation(response))
                .catch(error => actions.rejectModelActivation(error)));
};

export const requestDeleteModel = action$ => {
    return action$.ofType(types.REQUEST_DELETE_MODEL)
        .concatMap( ( { payload: { modelId } } ) =>
            api.deleteModel(modelId)
                .then(response => actions.receiveDeleteModel(response))
                .catch(error => actions.rejectDeleteModel(error)));
};

export default [
    requestImages,
    requestImageVisualization,
    requestCnnClasses,
    requestCnnLayers,
    requestCnnClassification,
    requestSelectedImage,
    requestAvailableModels,
    requestActiveModel,
    requestModelActivation,
    requestDeleteModel,
    requestCnnClassificationRefresh,
];