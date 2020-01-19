import * as types from 'actionTypes';
import * as actions from 'actions';

import { of } from 'rxjs';
import { concatMap, map, catchError, mergeMap } from 'rxjs/operators';
import { ofType } from 'redux-observable';
import { ajax } from 'rxjs/ajax';

const baseApi = 'http://0.0.0.0:5000'

export const requestNetworkLayers = action$ => action$.pipe(
    ofType(types.REQUEST_NETWORK_LAYERS),
    concatMap(action =>
        ajax.getJSON(`${ baseApi }/api/networks/${ action.payload }/layers/`).pipe(
            map(response => actions.receiveNetworkLayers(response)),
            catchError(error => of(actions.rejectNetworkLayers(error)))
        )
    )
);

export const requestNetworkClasses = action$ => action$.pipe(
    ofType(types.REQUEST_NETWORK_CLASSES),
    concatMap(action =>
        ajax.getJSON(`${ baseApi }/api/networks/${ action.payload }/classes/`).pipe(
            map(response => actions.receiveNetworkClasses(response)),
            catchError(error => of(actions.rejectNetworkClasses(error)))
        ),
    )
);

export const requestImages = action$ => action$.pipe(
    ofType(types.REQUEST_IMAGES),
    concatMap(action =>
        ajax.getJSON(`${ baseApi }/api/images`).pipe(
            map(response => actions.receiveImages(response.payload)),
            catchError(error => of(actions.rejectImages(error)))
        )
    )
);


export const requestImageUpload = action$ => action$.pipe(
    ofType(types.REQUEST_IMAGE_UPLOAD),
    concatMap(action =>
        ajax.post(`${ baseApi }/api/images/`, action.payload ).pipe(
            mergeMap(response => of(
                actions.receiveImageUpload(response),
                actions.requestImages()
            )),
            catchError(error => of(actions.rejectImageUpload(error)))
        )
    )
);

export const requestImageClassification = action$ => action$.pipe(
    ofType(types.REQUEST_IMAGE_CLASSIFICATION),
    concatMap(action =>
        ajax.getJSON(`${ baseApi }/api/images/`).pipe(
            map(response => actions.receiveImageClassification(response)),
            catchError(error => of(actions.rejectImageClassification(error)))
        )
    )
)

export const requestGradCam = (action$, store) => action$.pipe(
    ofType(types.REQUEST_GRADCAM),
    concatMap(action =>
        ajax.getJSON(`${ baseApi }/api/images/${ store.value.root.imageId }/gradcam?class=${ store.value.root.class }&layer=${ store.value.root.layer }`).pipe(
            map(response => actions.receiveGradCam(response)),
            catchError(error => of(actions.rejectGradCam(error)))
        )
    )
)
export const requestGuidedGradCam = (action$, store) => action$.pipe(
    ofType(types.REQUEST_GUIDED_GRADCAM),
    concatMap(action =>
        ajax.getJSON(`${ baseApi }/api/images/${ store.value.root.imageId }/guidedgradcam?class=${ store.value.root.class }&layer=${ store.value.root.layer }`).pipe(
            map(response => actions.receiveGuidedGradCam(response)),
            catchError(error => of(actions.rejectGuidedGradCam(error)))
        )
    )
)

export default [
    requestImageClassification,
    requestGradCam,
    requestGuidedGradCam,
    requestNetworkLayers,
    requestNetworkClasses,
    requestImages,
    requestImageUpload,
];