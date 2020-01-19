import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';

import AnalysisPage from 'pages/AnalysisPage';
import store from 'store';

class App extends Component {
    render() {
        return (
            <Provider store={ store }>
                <AnalysisPage />
            </Provider>
        )
    }
}

const render = () => {
    ReactDOM.render(<App />,
        document.getElementById('root') || document.createElement('div'));
};

render();
