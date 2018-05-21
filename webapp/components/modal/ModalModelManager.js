import React, { Component } from 'react';
import { connect } from 'react-redux';
import { Icon, Label, Menu, Table } from 'semantic-ui-react'
import classnames from 'classnames';
import Modal from 'components/modal/Modal';
import { Dimmer, Loader } from 'semantic-ui-react';

import { requestAvailableModels, requestActiveModel, requestModelActivation, requestDeleteModel } from 'actions';
import { requestCnnLayers, requestCnnClasses } from '../../actions';

import 'style/modal/ModalModelManager.scss';

const defaultClasses = [

];

class ModalModelManager extends Component {

    static defaultProps = {
        classNames: [],
        availableModels: [],
    }

    componentWillMount() {
        this.props.getModels();
    }

    render() {
        
        let classNames = classnames(
            defaultClasses,
            this.props.classNames,
        );

        return (
            <Modal>
                <Table basic className={ classNames }>
                    <Table.Header className='modal-scroll'>
                        <Table.Row style={{display: 'flex', justifyContent: 'space-between'}}> 
                                <Table.HeaderCell  style={{width: '200px'}} textAlign='center'>
                                    Model Name
                                </Table.HeaderCell>
                                <Table.HeaderCell style={{width: '200px'}} textAlign='center'>
                                    Trained on
                                </Table.HeaderCell>
                                <Table.HeaderCell textAlign='center'>
                                    Action
                                </Table.HeaderCell>
                        </Table.Row>
                    </Table.Header>

                    <Table.Body style={{height: '550px'}} className='modal-scroll'>
                        {this.props.availableModels.map(model => (
                                <Table.Row  style={{display: 'flex', justifyContent: 'space-between'}}>
                                    <Table.Cell style={{width: '200px'}} textAlign='center'>
                                        { model.model }
                                    </Table.Cell>
                                    <Table.Cell style={{width: '300px'}} textAlign='center'>
                                        { model.dataset }
                                    </Table.Cell>
                                    <Table.Cell textAlign='center'>
                                        <Icon className='clickable' size='large' 
                                            name={model.id === this.props.activeModel ? 'checkmark box' : 'square outline'}
                                            onClick={ () => this.props.activateModel(model.id) }
                                        />
                                        <Icon className='clickable' size='large' name='write'
                                            onClick={ () => console.log("Modify model!") }
                                        />
                                        <Icon className='clickable' size='large' name='delete'
                                             onClick={ () => this.props.deleteModel(model.id) }
                                        />
                                    </Table.Cell>
                                </Table.Row>
                        ))}
                    </Table.Body>
                </Table>
                {this.props.loading && [<Dimmer active />, <Loader active />]}
            </Modal>
        );
    }
}

export default connect(
    state => ({
        availableModels: state.cnn.availableModels,
        activeModel: state.cnn.activeModel,
        loading: state.loading.modelActivation,
    }),
    dispatch => ({
        getModels() {
            dispatch(requestActiveModel());
            dispatch(requestAvailableModels());
        },
        activateModel(modelId) {
            dispatch(requestModelActivation(modelId));
            dispatch(requestCnnLayers());
            dispatch(requestCnnClasses());
        },
        deleteModel(modelId) {
            dispatch(requestDeleteModel(modelId));
            dispatch(requestAvailableModels());
        },
    })
)(ModalModelManager);