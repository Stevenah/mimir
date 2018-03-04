import React, { Component } from 'react';
import { Route, Switch } from 'react-router-dom';

import PageRoot from 'pages/PageRoot';
import ReportPage from 'pages/ReportPage';
import SettingsPage from 'pages/SettingsPage';
import ImageAnalysisPage from 'pages/ImageAnalysisPage';

import ModalRouter from 'components/modal/ModalRouter';
import ModalRoute from 'components/modal/ModalRoute';
import AttachImageModal from 'components/modal/AttachImageModal';

import Sidebar from 'components/sidebar/Sidebar';

import 'style/app/App.scss';

const App = () =>
    <div className="app" >
        <Sidebar />
        <ModalRouter>
            <ModalRoute name='attachImage' component={AttachImageModal}/>
        </ModalRouter>
        <PageRoot>
            <Switch>
                <Route exact path="/" component={ImageAnalysisPage} />
                <Route path="/image" component={ImageAnalysisPage} />
                <Route path="/report" component={ReportPage} />
                {/* <Route path="/settings" component={SettingsPage} /> */}
            </Switch>
        </PageRoot>
    </div>

export default App;