import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import { BrowserRouter, browserHistory  } from 'react-router-dom';

import { Button } from 'mimir-ui';

import store from 'store';
import App from 'components/app/App';

const AppContainer = () =>
    <Provider store={store}>
        <BrowserRouter>
            <App />
        </BrowserRouter>
    </Provider>

const render = () => {
    ReactDOM.render(<AppContainer />,
        document.getElementById('app') || document.createElement('div'));
};

render();
