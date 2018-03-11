import { createStore, compose, applyMiddleware, combineReducers } from 'redux';
import { createEpicMiddleware, combineEpics } from 'redux-observable';

import logger from 'redux-logger';

import appReducer from 'reducers/app';
import loadingReducer from 'reducers/loading';
import reportReducer from 'reducers/report';
import cnnReducer from 'reducers/cnn';

import appEpics from 'epics';

const epics = combineEpics(
    ...appEpics
);

let composeEnhancers = compose;

const middlewares = [
    createEpicMiddleware(epics),
];

if (process.env.NODE_ENV === `development`) {
    console.log('You are running the develpment version of the app...')
    composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;
    middlewares.push(logger);
}

export default createStore(
    combineReducers({
        app: appReducer,
        loading: loadingReducer,
        report: reportReducer,
        cnn: cnnReducer,
    }),
    composeEnhancers(
        applyMiddleware(...middlewares)
    )
);