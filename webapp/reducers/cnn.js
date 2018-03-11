import * as actions from 'actionConstants';
import update from 'immutability-helper';

const initialState = {
    layers: [],
    classes: [],
    selectedClass: 6,
    selectedLayer: 'block5_conv4',
    classifications: {},
    originalImages: {},
    gradCamImages: {},
    guidedGradCamImages: {},    
};

const cnn = (state = initialState, action) => {
    switch (action.type) {

        case actions.RECEIVE_IMAGES:
            return update(state, {
                originalImages: {$merge: action.payload.images}
            })

        case actions.SELECT_FILE:
            return update(state, {
                selectedImageId: {$set: action.payload.fileId},
                selectedImageSource: {$set: state.originalImages[action.payload.fileId].source}
            })
            
        case actions.RECEIVE_CNN_LAYERS:
            return update(state, {
                layers: {$set: action.payload.layers}
            });

        case actions.RECEIVE_CNN_CLASSES:
            return update(state, {
                classes: {$set: action.payload.classes}
            });
        
        case actions.SELECT_CNN_CLASS:
            return update(state, {
                selectedClass: {$set: action.payload.classId}
            });

        case actions.SELECT_CNN_LAYER:
            return update(state, {
                selectedLayer: {$set: state.layers[action.payload.layerId]}
            });

        case actions.RECEIVE_CNN_CLASSIFICATION:
            return update(state, {
                classifications: {$merge: {[action.payload.imageId]: action.payload.classification}}
            });

        case actions.RECEIVE_IMAGE_VISUALIZATION:
            return update(state, {
                gradCamImages: {
                    $merge: {
                        [action.payload.imageId]: action.payload.gradCam
                    }
                },
                guidedGradCamImages: {
                    $merge: {
                        [action.payload.imageId]: action.payload.guidedGradCam
                    }
                },
            });

        default:
            return state;
    }
};

export default cnn;
