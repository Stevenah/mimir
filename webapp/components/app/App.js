import React, { Component } from 'react';
import { Route, Switch } from 'react-router-dom';

import PageRoot from 'pages/PageRoot';
import ReportPage from 'pages/ReportPage';
import ImageAnalysisPage from 'pages/ImageAnalysisPage';

import Sidebar from 'components/sidebar/Sidebar';

import 'style/app/App.scss';

const App = () =>
    <div className="app" >
        <Sidebar />
        <PageRoot>
            <Switch>
                <Route exact path="/" component={ImageAnalysisPage} />
                <Route path="/image" component={ImageAnalysisPage} />
                <Route path="/report" component={ReportPage} />
            </Switch>
        </PageRoot>
    </div>

export default App;