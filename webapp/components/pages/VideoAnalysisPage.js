import React from 'react'


import Panel from 'layout/Panel'
import PanelHeader from 'layout/PanelHeader';
import ContentGrid from 'layout/ContentGrid';
import ContentColumn from 'layout/ContentColumn';
import HeaderGrid from 'layout/HeaderGrid';
import HeaderColumn from 'layout/HeaderColumn';
import ContentRow from 'layout/ContentRow';

import ButtonMediaUpload from 'components/button/ButtonMediaUpload';
import ButtonAction from 'components/button/ButtonAction';

import PanelVideoStatistics from 'components/panels/PanelVideoStatistics';
import PanelShowcaseSelectedFile from 'components/panels/PanelShowcaseSelectedFile';
import PanelImagePicker from 'components/panels/PanelImagePicker';
import PanelGradcamVisualization from 'components/panels/PanelGradcamVisualization'
import PanelHeatmapVisualization from 'components/panels/PanelHeatmapVisualization'
import PanelLayerSelection from 'components/panels/PanelLayerSelection'
import PanelTargetSelection from 'components/panels/PanelTargetSelection'

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
                <PanelShowcaseSelectedFile />
                <PanelVideoStatistics />
            </ContentColumn>
            <ContentColumn>
                <PanelImagePicker />
            </ContentColumn>
        </ContentGrid>
    </div>

export default VideoAnalysisPage;