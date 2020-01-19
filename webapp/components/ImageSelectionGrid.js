import React, { Component } from 'react';
import { connect } from 'react-redux';

import { ImageGrid, Image } from 'mimir-ui';
import { requestImages, selectImage, requestImageClassification, requestGradCam, requestGuidedGradCam } from 'actions';

class ImageSelectionGrid extends Component {
    
    componentDidMount() {
        this.props.requestImages();
    }
    
    getImageList = () => {
        
        console.log(this.props)
        
        if (!this.props.images) {
            return [];
        }

        return Object.keys(this.props.images).map(imageId => (
            <Image 
                key={ `selectable_image_${this.props.images[imageId].id}` }
                onClick={() => this.props.selectImage(this.props.images[imageId].id) }
                src={ this.props.images[imageId].imagefile }
            />
        ));
    }

    render() {
        return (
            <ImageGrid>
                <input 
                    type='file'
                    ref={ this.fileUpload }
                    style={ { 'display': 'none' } }
                    onChange={ this.requestUpload }
                />
                { this.getImageList() }
            </ImageGrid>
        );
    }
}

export default connect(
    state => ({
        selectedImageId: state.root.selectedImageId,
        images: state.root.images,
    }),
    dispatch => ({
        selectImage: (imageId) => {
            dispatch(selectImage(imageId));
            dispatch(requestImageClassification(imageId));
            dispatch(requestGradCam());
            dispatch(requestGuidedGradCam());
        },
        requestImages: () => {
            dispatch(requestImages());
        }
    })
)(ImageSelectionGrid);