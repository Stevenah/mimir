import { createStore, compose, applyMiddleware, combineReducers } from 'redux';
import { createEpicMiddleware, combineEpics } from 'redux-observable';

import rootReducer from 'reducers/root';
import networkReducer from 'reducers/network';
import loadingReducer from 'reducers/loading';

import appEpics from 'epics';
import logger from 'redux-logger';

let composeEnhancers = compose;

const middlewares = []

const epics = combineEpics(
    ...appEpics
);

const reducers = combineReducers({
    root: rootReducer,
    network: networkReducer,
    loading: loadingReducer,
});

const epicMiddleware = createEpicMiddleware();

middlewares.push(epicMiddleware);

// if (process.env.NODE_ENV === `development`) {
console.log('You are running the develpment version of the app...')
composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;
middlewares.push(logger);
// }

export default createStore(
    reducers,
    composeEnhancers(
        applyMiddleware(...middlewares)
    )
);

epicMiddleware.run(epics)