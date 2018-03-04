import * as api from 'api/analysis';
import * as types from 'constants';
import * as actions from 'actions'; 
import * as utils from 'utils';
import 'rxjs/add/operator/concatMap';
import 'rxjs/add/operator/mergeMap';
import 'rxjs/add/operator/switchMap';
import { ajax } from 'rxjs/observable/dom/ajax';
import { Observable } from 'rxjs';

export const requestFileRefresh = (action$, store) => 
    action$.ofType(types.REQUEST_FILE_REFRESH)
        .concatMap(action =>
            api.refreshFiles(store.getState().settings.api.url)
                .then(files => actions.receiveFileRefresh(files))
                .catch(error => actions.rejectFileRefresh(error)));

export const requestCnnLayers = (action$, store) => 
    action$.ofType(types.REQUEST_CNN_LAYERS)
        .concatMap(action =>
            api.getCnnLayers(store.getState().settings.api.url)
                .then(layers => actions.receiveCnnLayers(layers))
                .catch(error => actions.rejectFileRefresh(error)));

export const requestCnnClasses = (action$, store) => 
    action$.ofType(types.REQUEST_CNN_CLASSES)
        .concatMap(action =>
            api.getCnnClasses(store.getState().settings.api.url)
                .then(classes => actions.receiveCnnClasses(classes))
                .catch(error => actions.rejectFileRefresh(error)));

export const requestCnnClassification = (action$, store) => 
    action$.ofType(types.REQUEST_CNN_CLASSIFICATION)
        .switchMap(({ payload: { imageId } }) =>
            ajax.getJSON(`${store.getState().settings.api.url}/api/model/classify/${imageId}`)
                .concatMap(response => [actions.receiveCnnClassification(imageId, response.classes)])
        .catch(error => console.log(error)));

export const requestImageAnalysis = (action$, store) =>
    action$.ofType(types.REQUEST_IMAGE_ANALYSIS)
        .concatMap(({payload: { imageId }}) => 
            api.analyzeImage(imageId, store.getState().settings.api.url)
            .then(response => actions.receiveImageAnalysis(imageId))
            .catch(error => console.log(error)));


export const requestSelectedVisualization = (action$, store) =>
    action$.ofType(types.REQUEST_SELECTED_VISUALIZATIONS).switchMap(() => {
        
        const state = store.getState(); 
        
        let apiUrl = state.settings.api.url,
            imageId = state.cnn.selectedImageId,
            layerId = state.cnn.selectedLayer,
            classId = state.cnn.selectedClass;

        return ajax.getJSON(
            `${apiUrl}/api/file/visualize/${imageId}?layerId=${layerId}&classId=${classId}`,
        ).concatMap(visualizations => [
            actions.receiveVisualizations(visualizations, imageId, classId, layerId),
            actions.updateVisualizations()
        ]);
    })
    .catch(error => actions.rejectFileRefresh(error));

export default [
    requestImageAnalysis,
    requestFileRefresh,
    requestCnnClasses,
    requestCnnLayers,
    requestSelectedVisualization,
    requestCnnClassification
];

