import * as actions from 'constants';
import update from 'immutability-helper';

const initialState = {
    analysis: false,
    file: false,
};

const analysis = (state = initialState, action) => {
    switch (action.type) {
        case actions.REQUEST_SELECTED_VISUALIZATIONS:
            return update(state, {
                analysis: {$set: true}
            });

        case actions.RECEIVE_SELECTED_VISUALIZATIONS:
            return update(state, {
                analysis: {$set: false}
            });

        case actions.REQUEST_FILE_UPLOAD:
        case actions.REQUEST_FILES:
        case actions.REQUEST_FILE_REFRESH:
            return update(state, {
                file: {$set: true}
            });

        case actions.REJECT_FILES:
        case actions.RECEIVE_FILES:
        case actions.RECEIVE_FILE_REFRESH:
            return update(state, {
                file: {$set: false}
            });
            
        default:
            return state;
    }
};

export default analysis;