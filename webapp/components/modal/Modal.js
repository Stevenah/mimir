import React, { Component } from 'react';
import { connect } from 'react-redux';

import ReactModal from 'react-modal';
import AwesomeModal from 'react-awesome-modal';
import classnames from 'classnames';

import { closeModal } from 'actions';

import 'style/modal/Modal.scss';

const defaultClasses = [
	
];

const defaultStyle = {

}

class Modal extends Component {

	static defaultProps = {
		classNames: [],
		isOpen: true,
		visible: true,
		width:'800',
		height:'600',
		effect:'fadeInUp',
		style: defaultStyle,
	}

	closeModal = () => {
		this.props.closeModal();
	}

	render() {
		
		let classNames = classnames(
            defaultClasses,
            this.props.classNames,
        );

		return (
			<AwesomeModal
				className={ classNames }
				visible={ this.props.visible }
				height={ this.props.height }
				width={ this.props.width }
				effect={ this.props.effect }
				onClickAway={ () => this.closeModal() }
				style={ this.props.style }
			>
				{ this.props.children }
			</AwesomeModal>
		);
	}
}

export default connect(
	null,
	dispatch => ({
		closeModal() {
			dispatch(closeModal())
		},
	})
)(Modal);
