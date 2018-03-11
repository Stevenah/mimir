import * as actions from 'actionConstants';
import update from 'immutability-helper';

const initialState = {
    attachedImages: [],
    patientName: 'Windom Earle',
    dateOfBirth: '07.12.1993',
    generalPracticioner: 'Billy Gregg',
    hospitalNumber: '562346',
    dateOfProcedure: '27.09.2012',
    endoscopist: 'Dan Brownman',
    nurses: 'Jane Doe, Carol Smith',
    medications: 'Xylocaine Sprey',
    instrument: 'G15 - H260',
    extentOfExam: 'Second part of duodenum',
    visualization: 'Good',
    coMorbidity: 'None',
    indicationsForExamination: 'Survailence-Varices',
    procedurePerformed: 'Gastoscopy (OGD)',
    findings: 'Polyps',
    endoscopicDiagnosis: 'Varices. Esophageal. Furthger 4 bands applied',
    recommendations: 'High fiber diet.',
    followUp: 'High fiber diet',
    opsc4Code: 'G45 Gastroscopy (OGD)',
};

const report = (state = initialState, action) => {
    switch (action.type) {
       
        case actions.ATTACH_FILE:
            return update(state, {
                attachedImages: { $push: [ action.payload.imageId ] },
            })
        
        case actions.DETACH_FILE:
            return update(state, {
                attachedImages: { $unshift: [ action.payload.imageId ] }
            })

        case actions.SET_TEXT_FIELD: {
            return update(state, {
                [action.payload.field]: {$set: action.payload.value},
            });
        }

        default:
            return state;
    }
};

export default report;