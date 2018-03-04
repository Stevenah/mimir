import { createStore, compose, applyMiddleware, combineReducers } from 'redux';
import { createEpicMiddleware, combineEpics } from 'redux-observable';

import logger from 'redux-logger';

import fileReducer from 'reducers/file';
import loadingReducer from 'reducers/loading';
import reportReducer from 'reducers/report';
import modalReducer from 'reducers/modal';
import cnnReducer from 'reducers/cnn';
import apiSettingsReducer from 'reducers/api';

import analysisEpics from 'epics';

const epics = combineEpics(
    ...analysisEpics
);

const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;

const middlewares = [
    createEpicMiddleware(epics),
];

if (process.env.NODE_ENV === `development`) {
    middlewares.push(logger);
    console.log('You are running the develpment version of the app...')
}

const reducers = combineReducers({
    settings: combineReducers({
        api: apiSettingsReducer,
    }),
    file: fileReducer,
    loading: loadingReducer,
    report: reportReducer,
    modal: modalReducer,
    cnn: cnnReducer,
});

export default createStore(
    reducers,
    composeEnhancers(
        applyMiddleware(...middlewares)
    )
);