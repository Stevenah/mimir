import React, { Component } from 'react';
import { connect } from 'react-redux';

import { requestFileUpload, requestFileRefresh } from 'actions';

import FineUploaderTraditional from 'fine-uploader-wrappers';
import FileInput from 'react-fine-uploader/file-input';

import ButtonAction from 'components/button/ButtonAction';

class ButtonUpload extends Component {

    static state = []

    componentWillMount() {
        this.uploader = new FineUploaderTraditional({
            options: {
               request: {
                  endpoint: 'api/file/upload'
               },
            }
         });
    }

    componentDidMount() {
        this.uploader.on('onSubmit', (id, name) => {
            this.props.requestFileUpload();
        });

        this.uploader.on('onAllComplete', (succeeded, failed) => {
            this.props.requestFileRefresh();
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
        requestFileRefresh(){
            dispatch(requestFileRefresh())
        }
    })
)(ButtonUpload);