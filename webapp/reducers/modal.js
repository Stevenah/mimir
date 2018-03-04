import * as actions from 'constants';
import update from 'immutability-helper';

const initialState = {
    active: null,
};

const modal = (state = initialState, action) => {
    switch (action.type) {
        case actions.OPEN_MODAL:
            return update(state, {
                active: {$set: action.payload.active}
            });
            
        case actions.CLOSE_MODAL:
            return update(state, {
                active: {$set: null}
            });
        
        default:
            return state;
    }
};

export default modal;
