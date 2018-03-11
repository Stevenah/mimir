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

export const requestImageVisualization = action$ => {
    return action$.ofType(types.REQUEST_IMAGE_VISUALIZATION)
        .concatMap(({payload: { imageId, layerId, classId }}) =>
            api.getImageVisualization(imageId, classId, layerId)
                .then(response => actions.receiveImageVisualization(response, imageId, classId, layerId))
                .catch(error => actions.rejectImageVisualization(error)));
};

export default [
    requestImages,
    requestImageVisualization,
    requestCnnClasses,
    requestCnnLayers,
    requestCnnClassification,
];