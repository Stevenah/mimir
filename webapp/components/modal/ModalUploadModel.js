import React, { Component } from 'react';
import { connect } from 'react-redux';
import { Button, Label, TextArea, Checkbox, Form, Radio } from 'semantic-ui-react'
import classnames from 'classnames';
import Modal from 'components/modal/Modal';
import { Dimmer, Loader } from 'semantic-ui-react';

import { guid } from 'utils'

import { requestUploadModel, receiveUploadModel } from 'actions';

import FineUploaderTraditional from 'fine-uploader-wrappers';
import FileInput from 'react-fine-uploader/file-input';

const defaultClasses = [

];

const architectures = [
    { key: '1', text: 'VGG', value: 'vgg' },
    { key: '2', text: 'Inception', value: 'inception' },
    { key: '3', text: 'ResNet', value: 'resnet' },
    { key: '4', text: 'Custom', value: 'custom' },
]  

class ModalUploadModel extends Component {

    static defaultProps = {
        classNames: [],
        uploadedFileName: 'None',
    }

    state = {
        classFile: 'Select a File',
        modelFile: 'Select a File',
    }

    componentWillMount = () => {
        this.sessionId = guid()
    }


    componentDidMount = () => {

        this.uploader = new FineUploaderTraditional({
            options: {
               autoUpload: false,
               interceptSubmit: true,
               extraButtons: [
                   { element: this.classFileInput, },
                   { element: this.modelInputFile, }
               ],
            },
         });

        this.uploader.on('onSubmit', (id, name) => {

            let buttonId = this.uploader.methods.getButton(id).id

            if (buttonId  === 'model_file_input') {
                this.uploader.methods.setParams({buttonId: buttonId}, id);
                this.setState( { modelFile: name } );
            }

            if (buttonId  === 'class_file_input') {
                this.uploader.methods.setParams({buttonId: buttonId}, id);
                this.setState( { classFile: name } )
            }
        });

        this.uploader.on('onUpload', () => {
            this.props.requestUploadModel()
        });
        
        this.uploader.on('onAllComplete', (succeeded, failed) => {
            this.props.receiveUploadModel()
        });
    }


    upload = () => {
        this.uploader.methods.setForm('qq-form')
        this.uploader.methods.uploadStoredFiles()
    }

    render = () =>  {
        
        let classNames = classnames(
            defaultClasses,
            this.props.classNames,
        );

        return (
            <Modal>
                <Form style={ { padding: '20px' } } onSubmit={e => e.preventDefault()} action={'api/cnn/upload'} id='qq-form'>
                    <Form.Group widths='equal'>
                        <Form.Select name='architecture' label='Architecture' options={architectures} placeholder='Architecture' />
                    </Form.Group>

                    <Form.Group widths='equal'>
                        <Form.Input name="model_name" fluid label='Model Name' placeholder='Model Name' />
                        <Form.Field>
                            <label>
                                Model File
                            </label>
                            <div ref={input => this.modelInputFile = input} id="model_file_input">
                                <label htmlFor='model_file' style={ { width: '130px' } } className='ui icon button'>
                                    <i style={{ paddingRight: '5px' }} className='file icon'></i>
                                    Model File
                                </label>
                                <span style={ { maxWidth: '200px', whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis', display: 'inline-block' } }>
                                    { this.state.modelFile }
                                </span>
                            </div>
                        </Form.Field>
                    </Form.Group>

                    <Form.Group widths='equal'>
                        <Form.Input name="dataset_name" fluid label='Dataset Trained on' placeholder='Dataset Name' />
                        <Form.Field>
                            <label>
                                Class File
                            </label>
                            <div ref={input => this.classFileInput = input} id="class_file_input">
                                <label htmlFor='class_file' style={ { width: '130px' } } className='ui icon button'>
                                    <i style={{ paddingRight: '5px' }} className='file icon'></i>
                                    Class File
                                </label>
                                <span style={ { maxWidth: '200px', whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis', display: 'inline-block' } }>
                                    { this.state.classFile }
                                </span>
                            </div>
                        </Form.Field>
                    </Form.Group>
                    
                    <Form.Field name="description" style={ { 'height': '230px', 'resize': 'none' } } control={TextArea} label='Description' placeholder='Give a short description about your model...' />
                    
                    <Button>
                        Cancel
                    </Button>
                    <Button type="submit" onClick={() => this.upload()}>
                        Upload
                    </Button>
                    <input readOnly={true} value={ this.sessionId } type="text" name="submission_id" style={ { display: 'none' } } />
                </Form>
                {this.props.loading && [<Dimmer active />, <Loader active />]}
            </Modal>
        );
    }
}

export default connect(
    state => ({
        loading: state.loading.modelUpload,
    }),
    dispatch => ({
        requestUploadModel() {
            dispatch(requestUploadModel())
        },
        receiveUploadModel() {
            dispatch(receiveUploadModel())
        }
    })
)(ModalUploadModel);
