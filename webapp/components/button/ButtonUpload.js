import React, { Component } from 'react';
import { connect } from 'react-redux';

import { requestFileUpload, requestImages } from 'actions';

import FineUploaderTraditional from 'fine-uploader-wrappers';
import FileInput from 'react-fine-uploader/file-input';

import ButtonAction from 'components/button/ButtonAction';

class ButtonUpload extends Component {

    static state = []

    componentWillMount() {
        this.uploader = new FineUploaderTraditional({
            options: {
               request: {
                  endpoint: 'api/files/upload',
               },
               chunking: {
                   enabled: true,
               },
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

    render() {
        return (
            <ButtonAction className={['analysis-header-button']}>
                <FileInput className='analysis-header-button' multiple uploader={ this.uploader }>
                    Upload Files
                </FileInput>
            </ButtonAction>
        );
    }
}

export default connect(
    null,
    dispatch => ({
        requestFileUpload(){
            dispatch(requestFileUpload())
        },
        requestImages(){
            dispatch(requestImages())
        }
    })
)(ButtonUpload);