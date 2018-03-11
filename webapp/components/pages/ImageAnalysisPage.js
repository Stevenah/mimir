import React from 'react'

import ContentGrid from 'layout/ContentGrid';
import ContentColumn from 'layout/ContentColumn';
import HeaderGrid from 'layout/HeaderGrid';
import HeaderColumn from 'layout/HeaderColumn';
import ContentRow from 'layout/ContentRow';

import ButtonUpload from 'components/button/ButtonUpload';
import ButtonToggleAttachFile from 'components/button/ButtonToggleAttachFile';

import Panel from 'layout/Panel'
import PanelHeader from 'layout/PanelHeader';

import PanelShowcaseSelectedFile from 'components/panels/PanelShowcaseSelectedFile';
import PanelGuidedGradCamVisualization from 'components/panels/PanelGuidedGradCamVisualization'
import PanelGradCamVisualization from 'components/panels/PanelGradCamVisualization'
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
                </PanelHeader>
            </HeaderColumn>
            <HeaderColumn>
                <PanelHeader>
                    <ButtonUpload />
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
                        <PanelGuidedGradCamVisualization />
                    </ContentColumn>
                    <ContentColumn>
                        <PanelGradCamVisualization />
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