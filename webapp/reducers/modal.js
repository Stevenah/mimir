import * as actions from 'actionConstants';
import update from 'immutability-helper';

const initialState = {
    active: null,
};

const modal = (state = initialState, action) => {
    switch (action.type) {

        case actions.OPEN_MODAL: {
            return update(state, {
                active: { $set: action.payload.modalId }
            });
        }

            
        case actions.CLOSE_MODAL: {
            return update(state, {
                active: { $set: null }
            });
        }

        case actions.RECEIVE_UPLOAD_MODEL:
        case actions.REJECT_UPLOAD_MODEL: {
            return update(state, {
                active: { $set: null }
            });
        }

        default: {
            return state;
        }
        
    }
};

export default modal;