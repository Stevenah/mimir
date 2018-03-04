import * as actions from 'constants';
import update from 'immutability-helper';

const initialState = {
    url: 'http://0.0.0.0:80',
};

const apiSettings = (state = initialState, action) => {
    switch (action.type) {

        case actions.SET_API_URL:
            return update(state, {
                url: {$set: action.payload.apiUrl}
            });
            
        default:
            return state;
    }
};

export default apiSettings;