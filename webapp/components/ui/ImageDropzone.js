import React, { Component } from 'react';
import { connect } from 'react-redux';

import { requestFileUpload, requestImages, requestFiles } from 'actions';

import FineUploaderTraditional from 'fine-uploader-wrappers';
import Dropzone from 'react-fine-uploader/dropzone';

import { compose, withProps } from 'recompose';

import { Icon } from 'semantic-ui-react';


const defaultStyle = {
    width: '100%',
    height: '100%',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center'
}

class ImageUploadDropzone extends Component {

    static state = []

    componentWillMount() {
        this.uploader = new FineUploaderTraditional({
            options: {
               request: {
                  endpoint: 'api/files/upload',
               }
            }
         });
    }

    componentDidMount() {
        this.uploader.on('onSubmit', (id, name) => {
            this.props.requestFileUpload();
        });

        this.uploader.on('onAllComplete', (succeeded, failed) => {
            this.props.requestImages();
        });
    }

    onProcessingDroppedFilesComplete = (files, dropTarget) => {
        
    }

    render() {
        return (
            <Dropzone
                multiple
                onProcessingDroppedFilesComplete={this.onProcessingDroppedFilesComplete}
                style={ defaultStyle } uploader={ this.uploader 
            }>
                <Icon size='huge' name='image' />
            </Dropzone>
        );
    }
}

export default ImageUploadDropzone;