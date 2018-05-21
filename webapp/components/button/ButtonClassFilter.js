import React from 'react';
import { connect } from 'react-redux';
import { compose, withProps, withHandlers } from 'recompose';
import { selectCLassFilter } from 'actions';

import { isEmpty } from 'utils';

import ButtonDropDown from 'components/button/ButtonDropDown'

const enhance = compose(
    connect(
        state => ({
            classes: state.cnn.classes,
            selected: state.app.classFilter,
        }),
        dispatch => ({
            selectCLassFilter(classId) {
                dispatch(selectCLassFilter(classId))
            },
        }),
    ),
    withProps(props => ({
        options: {'default': 'All', ...props.classes},
    })),
    withHandlers({
        onClick: props => classId => {
            props.selectCLassFilter(classId);
        }
    })
);

export default enhance(ButtonDropDown);