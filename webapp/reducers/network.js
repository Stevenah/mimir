import * as actions from '../actionTypes';
import update from 'immutability-helper';

const initialState = {

};

const network = (state = initialState, action) => {
    switch (action.type) {
         

        case actions.RECEIVE_NETWORK_CLASSES: {
            return update(state, {
                classes: { $set: action.payload },
            })
        }

        case actions.RECEIVE_NETWORK_LAYERS: {
            return update(state, {
                layers: { $set: action.payload },
            })
        }

        default: {
            return state;
        }
    }
};

export default network;