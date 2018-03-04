import React from 'react'

import ContentGrid from 'layout/ContentGrid';
import ContentColumn from 'layout/ContentColumn';
import HeaderGrid from 'layout/HeaderGrid';
import HeaderColumn from 'layout/HeaderColumn';
import ContentRow from 'layout/ContentRow';

import ButtonMediaUpload from 'components/button/ButtonMediaUpload';
import ButtonAction from 'components/button/ButtonAction';

import FileSelector from 'components/ui/FileSelector';

import Panel from 'layout/Panel'
import PanelHeader from 'layout/PanelHeader';

import PanelFileSelector from 'components/panels/PanelFileSelector';
import PanelVideoShowcase from 'components/panels/PanelVideoShowcase'
import PanelImagePicker from 'components/panels/PanelImagePicker';

import 'style/AnalysisPage.scss';

const VideoAnalysisPage = () => 
    <div className="full">
        <HeaderGrid>
            <HeaderColumn>
                <PanelHeader>
                </PanelHeader>
            </HeaderColumn>
            <HeaderColumn>
                <PanelHeader>
                    <ButtonMediaUpload>
                        Upload file
                    </ButtonMediaUpload>
                </PanelHeader>
            </HeaderColumn>
        </HeaderGrid>
        <ContentGrid>
            <ContentColumn>
                <PanelVideoShowcase />
                <Panel />
            </ContentColumn>
            <ContentColumn>
                <PanelFileSelector />
            </ContentColumn>
        </ContentGrid>
    </div>

export default VideoAnalysisPage;