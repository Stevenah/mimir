import React, { Component } from 'react';

import Panel from 'layout/Panel';
import PanelHeader from 'layout/PanelHeader';
import ContentGrid from 'layout/ContentGrid';
import ContentColumn from 'layout/ContentColumn';
import HeaderGrid from 'layout/HeaderGrid';
import HeaderColumn from 'layout/HeaderColumn';
import ContentRow from 'layout/ContentRow';

import ButtonToggleAttachFile from 'components/button/ButtonToggleAttachFile';
import ButtonClassFilter from 'components/button/ButtonClassFilter';
import ButtonPrint from 'components/button/ButtonPrint';

import PanelFileSelector from 'components/panels/PanelFileSelector';

import PanelReport from 'components/panels/PanelReport';


const ReportPage = () =>
    <div>
        <HeaderGrid>

            <HeaderColumn>
                <PanelHeader>
                    <ButtonPrint />
                </PanelHeader>
            </HeaderColumn>
            
            <HeaderColumn>
                <PanelHeader>

                    <HeaderColumn>
                        <PanelHeader>
                            <ButtonToggleAttachFile />
                        </PanelHeader>
                    </HeaderColumn>

                    <HeaderColumn>
                        <PanelHeader>
                            <ButtonClassFilter />
                        </PanelHeader>
                    </HeaderColumn>

                </PanelHeader>
            </HeaderColumn>

        </HeaderGrid>

        <ContentGrid>

            <ContentColumn>
                <PanelReport />
            </ContentColumn>

            <ContentColumn>
                <PanelFileSelector />
            </ContentColumn>

        </ContentGrid>
    </div>

export default ReportPage;