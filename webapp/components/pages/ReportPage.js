import React, { Component } from 'react';

import Panel from 'layout/Panel';
import PanelHeader from 'layout/PanelHeader';
import ContentGrid from 'layout/ContentGrid';
import ContentColumn from 'layout/ContentColumn';
import HeaderGrid from 'layout/HeaderGrid';
import HeaderColumn from 'layout/HeaderColumn';
import ContentRow from 'layout/ContentRow';

import PanelReport from 'components/panels/PanelReport';


const ReportPage = () =>
    <div>
        <HeaderGrid>
            <HeaderColumn>
                <PanelHeader>
                </PanelHeader>
            </HeaderColumn>
        </HeaderGrid>
        <ContentGrid>
            <ContentColumn>
                <PanelReport />
            </ContentColumn>
        </ContentGrid>
    </div>

export default ReportPage;