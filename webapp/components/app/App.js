import React, { Component } from 'react';
import { Route, Switch } from 'react-router-dom';

import PageRoot from 'pages/PageRoot';
import ReportPage from 'pages/ReportPage';
import ImageAnalysisPage from 'pages/ImageAnalysisPage';

import ModalRouter from 'components/modal/ModalRouter';
import ModalRoute from 'components/modal/ModalRoute';

import ModalModelManager from 'components/modal/ModalModelManager';
import ModalUploadModel from 'components/modal/ModalUploadModel';

import Sidebar from 'components/sidebar/Sidebar';

import 'style/app/App.scss';

const App = () =>
    <div className="app" >
        <Sidebar />
        <ModalRouter>
            <ModalRoute name='manageModels' component={ ModalModelManager } />
            <ModalRoute name='uploadModel' component={ ModalUploadModel } />
        </ModalRouter>
        <PageRoot>
            <Switch>
                <Route exact path="/" component={ImageAnalysisPage} />
                <Route path="/image" component={ImageAnalysisPage} />
                <Route path="/report" component={ReportPage} />
            </Switch>
        </PageRoot>
    </div>

export default App;