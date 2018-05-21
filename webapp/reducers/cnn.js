import * as actions from 'actionConstants';
import update from 'immutability-helper';

const initialState = {
    layers: [],
    classes: [],
    selectedClass: null,
    selectedLayer: null,
    activeModel: 0,
    classifications: {},
    originalImages: {},
    gradCamImages: {},
    guidedGradCamImages: {},
    availableModels: [],
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
            })
  
        case actions.RECEIVE_SELECTED_IMAGE:{
            return update(state, {
                selectedImageSource: { $set: action.payload.source }
            });
        }

        case actions.RECEIVE_CNN_LAYERS:{
            return update(state, {
                selectedLayer: {$set: state.selectedLayer ? state.selectedLayer : "0"},
                layers: {$set: action.payload.layers}
            });
        }

        case actions.RECEIVE_CNN_CLASSES: {
            return update(state, {
                selectedClass: {$set: state.selectedClass ? state.selectedClass : "0"},
                classes: {$set: action.payload.classes}
            });
        }
        
        case actions.SELECT_CNN_CLASS:
            return update(state, {
                selectedClass: {$set: action.payload.classId}
            });

        case actions.SELECT_CNN_LAYER:
            return update(state, {
                selectedLayer: {$set: action.payload.layerId}
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

        case actions.RECEIVE_AVAILABLE_MODELS: {
            return update(state, {
                availableModels: { $set: action.payload.models },
            });
        }

        case actions.RECEIVE_ACTIVE_MODEL: {
            return update(state, {
                activeModel: { $set: Number(action.payload.model.id) },
                activeModelName: { $set: action.payload.model.name },
            });
        }

        case actions.RECEIVE_MODEL_ACTIVATION: {
            return update(state, {
                activeModel: { $set: Number(action.payload.model.id) },
                activeModelName: { $set: action.payload.model.name },
            });
        }

        default:
            return state;
    }
};

export default cnn;
