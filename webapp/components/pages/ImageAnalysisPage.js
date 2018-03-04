import React from 'react'

import ContentGrid from 'layout/ContentGrid';
import ContentColumn from 'layout/ContentColumn';
import HeaderGrid from 'layout/HeaderGrid';
import HeaderColumn from 'layout/HeaderColumn';
import ContentRow from 'layout/ContentRow';

import ButtonMediaUpload from 'components/button/ButtonMediaUpload';
import ButtonAction from 'components/button/ButtonAction';
import ButtonImageAnalysis from 'components/button/ButtonImageAnalysis';
import ButtonAnalyseAll from 'components/button/ButtonAnalyseAll';
import ButtonToggleAttachFile from 'components/button/ButtonToggleAttachFile';

import Panel from 'layout/Panel'
import PanelHeader from 'layout/PanelHeader';

import PanelShowcaseSelectedFile from 'components/panels/PanelShowcaseSelectedFile';
import PanelGradcamVisualization from 'components/panels/PanelGradcamVisualization'
import PanelHeatmapVisualization from 'components/panels/PanelHeatmapVisualization'
import PanelLayerSelection from 'components/panels/PanelLayerSelection'
import PanelTargetSelection from 'components/panels/PanelTargetSelection'
import PanelImageDescription from 'components/panels/PanelImageDescription';
import PanelFileSelector from 'components/panels/PanelFileSelector';

const ImageAnalysisPage = () => 
    <div className="full">
        <HeaderGrid>
            <HeaderColumn>
                <PanelHeader>
                    <ButtonToggleAttachFile />
                    {/* <ButtonImageAnalysis label='Analyze'/> */}
                </PanelHeader>
            </HeaderColumn>
            <HeaderColumn>
                <PanelHeader>
                    <ButtonMediaUpload />
                    {/* <ButtonAnalyseAll label='Analyze All'/> */}
                </PanelHeader>
            </HeaderColumn>
        </HeaderGrid>
        <ContentGrid>
            <ContentColumn>
                <ContentRow>
                    <ContentColumn>
                        <PanelShowcaseSelectedFile />
                    </ContentColumn>
                    <ContentColumn>
                        <PanelImageDescription />
                    </ContentColumn>
                </ContentRow>
                <ContentRow>
                    <ContentColumn>
                        <PanelGradcamVisualization />
                    </ContentColumn>
                    <ContentColumn>
                        <PanelHeatmapVisualization />
                    </ContentColumn>
                </ContentRow>
                <ContentRow>
                    <ContentColumn>
                        <PanelLayerSelection />
                    </ContentColumn>
                    <ContentColumn>
                        <PanelTargetSelection />
                    </ContentColumn>
                </ContentRow>
            </ContentColumn>
            <ContentColumn>
                <PanelFileSelector />
            </ContentColumn>
        </ContentGrid>
    </div>

export default ImageAnalysisPage;