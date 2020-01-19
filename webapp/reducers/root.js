import * as actions from '../actionTypes';
import update from 'immutability-helper';

const initialState = {
    images: { },
    layer: 0,
    class: 0,
};

const root = (state = initialState, action) => {
    switch (action.type) {

        case actions.SELECT_IMAGE: {
            return update(state, {
                imageId: { $set: action.payload },
                image:   { $set: state.images[action.payload].imagefile }
            })
        }
        
        case actions.RECEIVE_IMAGES: {
            return update(state, {
                images: { $set: action.payload }
            })
        }

        case actions.RECEIVE_GRADCAM: {
            return update(state, {
                gradCam: { $set: action.payload.blob }
            })
        }

        case actions.RECEIVE_GUIDED_GRADCAM: {
            return update(state, {
                guidedGradCam: { $set: action.payload.blob }
            })
        }

        case actions.SELECT_CLASS: {
            return update(state, {
                class: { $set: action.payload }
            })
        }

        case actions.SELECT_LAYER: {
            return update(state, {
                layer: { $set: action.payload }
            })
        }

        default: {
            return state;
        }
    }
};

export default root;