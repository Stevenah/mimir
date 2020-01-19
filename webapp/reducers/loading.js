import * as actions from '../actionTypes';
import update from 'immutability-helper';

const initialState = {
    gradcam: false,
    guidedGradcam: false,
};

const loading = (state = initialState, action) => {
    switch (action.type) {
         
        case actions.RECEIVE_GRADCAM:
        case actions.REJECT_GRADCAM: {
            return update(state, {
                gradcam: { $set: false },
            })
        }

        case actions.RECEIVE_GUIDED_GRADCAM:
        case actions.REJECT_GUIDED_GRADCAM: {
            return update(state, {
                guidedGradcam: { $set: false },
            })
        }


        case actions.REQUEST_GRADCAM: {
            return update(state, {
                gradcam: { $set: true },
            })
        }

        case actions.REQUEST_GUIDED_GRADCAM: {
            return update(state, {
                guidedGradcam: { $set: true },
            })
        }

        default: {
            return state;
        }
    }
};

export default loading;