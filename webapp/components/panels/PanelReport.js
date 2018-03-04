import React from 'react';
import { connect } from 'react-redux';
import { compose, nest } from 'recompose';
import { updateField } from 'actions';

import Panel from 'layout/Panel'
import ColonoscopyReport from 'components/ui/ColonoscopyReport';

const enhance = compose(
    connect(
        state => ({
            attachedImages: state.report.attachedImages,
            patientName: state.report.patientName,
            dateOfBirth: state.report.dateOfBirth,
            generalPracticioner: state.report.generalPracticioner,
            hospitalNumber: state.report.hospitalNumber,
            dateOfProcedure: state.report.dateOfProcedure,
            endoscopist: state.report.endoscopist,
            nurses: state.report.nurses,
            medications: state.report.medications,
            instrument: state.report.instrument,
            extentOfExam: state.report.extentOfExam,
            visualization: state.report.visualization,
            coMorbidity: state.report.coMorbidity,
            indicationsForExamination: state.report.indicationsForExamination,
            procedurePerformed: state.report.procedurePerformed,
            findings: state.report.findings,
            endoscopicDiagnosis: state.report.endoscopicDiagnosis,
            recommendations: state.report.recommendations,
            followUp: state.report.followUp,
            opsc4Code: state.report.opsc4Code,
        }),
        dispatch => ({
            updateValue(field, value) {
                dispatch(updateField(field, value));
            }
        })
    )
);

export default enhance(nest(Panel, ColonoscopyReport));