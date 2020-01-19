import React, { Component } from 'react';
import { connect } from 'react-redux';

import { MimirUI, Grid, Image, NavBar } from 'mimir-ui';

import NetworkClassSelection from 'components/NetworkClassSelection';
import NetworkLayerSelection from 'components/NetworkLayerSelection';
import ImageSelectionGrid from 'components/ImageSelectionGrid';

import { requestImageUpload } from 'actions';

class AnalysisPage extends Component {
        
    fileUpload = React.createRef();

    requestUpload = () => {
        let formData = new FormData();
        formData.append('imagefile', this.fileUpload.current.files[0]);
        this.props.upload(formData);
    }

    render() {

        return (
            <MimirUI
                header={[
                    <NavBar.MenuItem key={1} onClick={ () => this.fileUpload.current.click() }>
                        Upload Images
                    </NavBar.MenuItem>
                ]}
            >
                <input 
                    type='file'
                    ref={ this.fileUpload }
                    style={ { 'display': 'none' } }
                    onChange={ this.requestUpload }
                />
                <Grid>
                    <Grid.Column borderRight>
                        <Grid.Row borderBottom>
                            <Grid.Column borderRight>
                                <Image src={ this.props.selected } />
                            </Grid.Column>
                            <Grid.Column>
                            </Grid.Column>
                        </Grid.Row>
                        <Grid.Row borderBottom>
                            <Grid.Column borderRight loading={ this.props.loading.gradcam }>
                                <Image src={ this.props.gradcam }/>
                            </Grid.Column>
                            <Grid.Column loading={ this.props.loading.guidedGradcam }>
                                <Image src={ this.props.guided } />
                            </Grid.Column>
                        </Grid.Row>
                        <Grid.Row>
                            <Grid.Column borderRight>
                                <NetworkLayerSelection />
                            </Grid.Column>
                            <Grid.Column>
                                <NetworkClassSelection />
                            </Grid.Column>
                        </Grid.Row>
                    </Grid.Column>
                    <Grid.Column>
                        <ImageSelectionGrid />
                    </Grid.Column>
                </Grid>
            </MimirUI>
        );
    }
}

export default connect(
    state => ({
        selected: state.root.image,
        gradcam: state.root.gradCam,
        guided: state.root.guidedGradCam,
        loading: state.loading,
    }),
    dispatch => ({
        upload: fileData =>  {
            dispatch(requestImageUpload(fileData));
        }
    })
)(AnalysisPage)
