import React, { Component } from 'react';
import Page from 'components/ui/Page';
import TextField from 'components/ui/TextField';
import TextBox from 'components/ui/TextBox';
import ImageAttachment from 'components/ui/ImageAttachment';

import 'style/ui/Report.scss';

const ColonoscopyReport = props =>
    <Page>
        <header className='page-header'>
            <div className='header-section-left'>
                <h3>Endoscopy Report</h3>
            </div>
            <div className='header-section-right'>
                <h3>Gastroscopy (OGD)</h3>
            </div>
        </header>
        
        <div>
            <hr/>
        </div>
        <h4>Guy's & St.Thomas' NHS Foundation Trust</h4>

        <div className='report-page-content'>
            <div className='section-left'>
                <div className='patient-data report-page-section'>
                    
                    <TextField
                        className={'input-group'}
                        label={'Patient Name'}
                        value={props.patientName}
                        onChange={e => props.updateValue('patientName', e.target.value)} 
                    />

                    <TextField 
                        className={'input-group'}
                        label={'Date of Birth'}
                        value={props.dateOfBirth}
                        onChange={e => props.updateValue('dateOfBirth', e.target.value)} 
                    />
                    
                    <TextField 
                        className={'input-group'}
                        label={'General Practicioner'}
                        value={props.generalPracticioner}
                        onChange={e => props.updateValue('generalPracticioner', e.target.value)} 
                    />
                </div>
                <div className='hospital-data report-page-section'>
                    
                    <TextField 
                        className={'input-group'}
                        label={'Hospital Number'} 
                        value={props.hospitalNumber}
                        onChange={e => props.updateValue('hospitalNumber', e.target.value)} 
                    />
                    
                    <TextField 
                        className={'input-group'}
                        label={'Date of Procedure'} 
                        value={props.dateOfProcedure}
                        onChange={e => props.updateValue('dateOfProcedure', e.target.value)} 
                    />

                    <TextField 
                        className={'input-group'}
                        label={'Endoscopist'}
                        value={props.endoscopist}
                        onChange={e => props.updateValue('endoscopist', e.target.value)} 
                    />
                    
                    <TextField 
                        className={'input-group'}
                        label={'Nurses'}
                        value={props.nurses}
                        onChange={e => props.updateValue('nurses', e.target.value)} 
                    />

                    <TextField
                        className={'input-group'}
                        label={'Medications'}
                        value={props.medications}
                        onChange={e => props.updateValue('medications', e.target.value)} 
                    />

                    <TextField 
                        className={'input-group'}
                        label={'Instrument'}
                        value={props.instrument}
                        onChange={e => props.updateValue('instrument', e.target.value)} 
                    />

                    <TextField 
                        className={'input-group'}
                        label={'Extent of Exam'}
                        value={props.extentOfExam}
                        onChange={e => props.updateValue('extentOfExam', e.target.value)} 
                    />

                    <TextField 
                        className={'input-group'}
                        label={'Visualization'}
                        value={props.visualization}
                        onChange={e => props.updateValue('visualization', e.target.value)} 
                    />

                    <TextField 
                        className={'input-group'}
                        label={'Co-morbidity'}
                        value={props.coMorbility}
                        onChange={e => props.updateValue('coMorbility', e.target.value)} 
                    />
                </div>
                <hr />
                <div className='input-box-group report-page-section'>
                    <TextBox 
                        label={'INDICATIONS FOR EXAMINATION'} 
                        value={props.indicationsForExamination}
                        onChange={e => props.updateValue('indicationsForExamination', e.target.innerHTML)} 
                    />
                </div>
                <div className='input-box-group report-page-section'>
                    <TextBox 
                        label={'PROCEDURE PERFORMED'} 
                        value={props.procedurePerformed}
                        onChange={e => props.updateValue('procedurePerformed', e.target.innerHTML)} 
                    />
                </div>
                <div className='input-box-group report-page-section'>
                    <TextBox 
                        label={'FINDINGS'}
                        value={props.findings}
                        onChange={e => props.updateValue('findings', e.target.innerHTML)} 
                    />
                </div>
                <div className='input-box-group report-page-section'>
                    <TextBox 
                        label={'ENDOSCOPIC DIAGNOSIS'} 
                        value={props.endoscopicDiagnosis}
                        onChange={e =>  { 
                            return props.updateValue('endoscopicDiagnosis', e.target.innerHTML)
                        }} 
                    />
                </div>
                <div className='input-box-group report-page-section'>
                    <TextBox 
                        label={'RECOMMENDATIONS'} 
                        value={props.recommendations}
                        onChange={e => props.updateValue('recommendations', e.target.innerHTML)} 
                    />
                </div>
                <div className='input-box-group report-page-section'>
                    <TextBox 
                        label={'FOLLOW UP'} 
                        value={props.followUp}
                        onChange={e => props.updateValue('followUp', e.target.innerHTML)} 
                    />
                </div>
                <div className='input-box-group report-page-section'>
                    <TextField
                        label={'OPCS4 Code'}
                        value={props.opsc4Code}
                        onChange={e => props.updateValue('opsc4Code', e.target.value)} 
                    />
                </div>
                <div className='input-box-group report-page-section'>
                    <span>Signature _____________________</span>
                </div>
            </div>
            <div className='section-right report-attached-images'>
                {Object.keys(props.attachedImages).map(fileId => (
                    <ImageAttachment label={props.attachedImages[fileId].file.name} src={props.attachedImages[fileId].source} />
                ))}
            </div>
        </div>
        <footer>
        </footer>
    </Page>


export default ColonoscopyReport;