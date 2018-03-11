import * as actions from 'actionConstants';
import update from 'immutability-helper';

const initialState = {
    gradCam: {},
    guidedGradCam: {},
    layers: false,
    classes: false,
    files: false
};

const analysis = (state = initialState, action) => {
    switch (action.type) {
        
        case actions.REQUEST_IMAGE_VISUALIZATION: {
            const imageId = `${action.payload.imageId}-${action.payload.layerId}-${action.payload.classId}`;
            return update(state, {
                gradCam: { [imageId]: { $set: true } },
                guidedGradCam: { [imageId]: { $set: true } },
            });
        }

        case actions.RECEIVE_IMAGE_VISUALIZATION: {
            return update(state, {
                gradCam: { [action.payload.imageId]: { $set: false } },
                guidedGradCam: { [action.payload.imageId]: { $set: false } },
            });
        }
            

        case actions.REQUEST_CNN_LAYERS:
            return update(state, {
                layers: { $set: true },
            });

        case actions.RECEIVE_CNN_LAYERS:
            return update(state, {
                layers: { $set: false },
            });

        case actions.REQUEST_CNN_CLASSES:
            return update(state, {
                classes: { $set: true },
            });

        case actions.RECEIVE_CNN_CLASSES:
            return update(state, {
                classes: { $set: false },
            });

        case actions.REQUEST_CNN_CLASSIFICATION:
            return update(state, {
                classification: { $set: true },
            });

        case actions.RECEIVE_CNN_CLASSIFICATION:
            return update(state, {
                classification: { $set: false },
            });


        case actions.REQUEST_FILE_UPLOAD:
        case actions.REQUEST_IMAGES:
            return update(state, {
                files: {$set: true}
            });

        case actions.REJECT_IMAGES:
        case actions.RECEIVE_IMAGES:
            return update(state, {
                files: {$set: false}
            });
            
        default:
            return state;
    }
};

export default analysis;