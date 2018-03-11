import React, { Component } from 'react';
import Page from 'components/ui/Page';
import TextField from 'components/ui/TextField';
import TextBox from 'components/ui/TextBox';
import ImageAttachment from 'components/ui/ImageAttachment';

import 'style/ui/Report.scss';

class ColonoscopyReport extends Component {

    static defaultProps = {
        attachedImages: [],
    }

    render() {
        return (
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
                                value={this.props.patientName}
                                onChange={e => this.props.updateValue('patientName', e.target.value)} 
                            />
        
                            <TextField 
                                className={'input-group'}
                                label={'Date of Birth'}
                                value={this.props.dateOfBirth}
                                onChange={e => this.props.updateValue('dateOfBirth', e.target.value)} 
                            />
                            
                            <TextField 
                                className={'input-group'}
                                label={'General Practicioner'}
                                value={this.props.generalPracticioner}
                                onChange={e => this.props.updateValue('generalPracticioner', e.target.value)} 
                            />
                        </div>
                        <div className='hospital-data report-page-section'>
                            
                            <TextField 
                                className={'input-group'}
                                label={'Hospital Number'} 
                                value={this.props.hospitalNumber}
                                onChange={e => this.props.updateValue('hospitalNumber', e.target.value)} 
                            />
                            
                            <TextField 
                                className={'input-group'}
                                label={'Date of Procedure'} 
                                value={this.props.dateOfProcedure}
                                onChange={e => this.props.updateValue('dateOfProcedure', e.target.value)} 
                            />
        
                            <TextField 
                                className={'input-group'}
                                label={'Endoscopist'}
                                value={this.props.endoscopist}
                                onChange={e => this.props.updateValue('endoscopist', e.target.value)} 
                            />
                            
                            <TextField 
                                className={'input-group'}
                                label={'Nurses'}
                                value={this.props.nurses}
                                onChange={e => this.props.updateValue('nurses', e.target.value)} 
                            />
        
                            <TextField
                                className={'input-group'}
                                label={'Medications'}
                                value={this.props.medications}
                                onChange={e => this.props.updateValue('medications', e.target.value)} 
                            />
        
                            <TextField 
                                className={'input-group'}
                                label={'Instrument'}
                                value={this.props.instrument}
                                onChange={e => this.props.updateValue('instrument', e.target.value)} 
                            />
        
                            <TextField 
                                className={'input-group'}
                                label={'Extent of Exam'}
                                value={this.props.extentOfExam}
                                onChange={e => this.props.updateValue('extentOfExam', e.target.value)} 
                            />
        
                            <TextField 
                                className={'input-group'}
                                label={'Visualization'}
                                value={this.props.visualization}
                                onChange={e => this.props.updateValue('visualization', e.target.value)} 
                            />
        
                            <TextField 
                                className={'input-group'}
                                label={'Co-morbidity'}
                                value={this.props.coMorbility}
                                onChange={e => this.props.updateValue('coMorbility', e.target.value)} 
                            />
                        </div>
                        <hr />
                        <div className='input-box-group report-page-section'>
                            <TextBox 
                                label={'INDICATIONS FOR EXAMINATION'} 
                                value={this.props.indicationsForExamination}
                                onChange={e => this.props.updateValue('indicationsForExamination', e.target.innerHTML)} 
                            />
                        </div>
                        <div className='input-box-group report-page-section'>
                            <TextBox 
                                label={'PROCEDURE PERFORMED'} 
                                value={this.props.procedurePerformed}
                                onChange={e => this.props.updateValue('procedurePerformed', e.target.innerHTML)} 
                            />
                        </div>
                        <div className='input-box-group report-page-section'>
                            <TextBox 
                                label={'FINDINGS'}
                                value={this.props.findings}
                                onChange={e => this.props.updateValue('findings', e.target.innerHTML)} 
                            />
                        </div>
                        <div className='input-box-group report-page-section'>
                            <TextBox 
                                label={'ENDOSCOPIC DIAGNOSIS'} 
                                value={this.props.endoscopicDiagnosis}
                                onChange={e =>  { 
                                    return this.props.updateValue('endoscopicDiagnosis', e.target.innerHTML)
                                }} 
                            />
                        </div>
                        <div className='input-box-group report-page-section'>
                            <TextBox 
                                label={'RECOMMENDATIONS'} 
                                value={this.props.recommendations}
                                onChange={e => this.props.updateValue('recommendations', e.target.innerHTML)} 
                            />
                        </div>
                        <div className='input-box-group report-page-section'>
                            <TextBox 
                                label={'FOLLOW UP'} 
                                value={this.props.followUp}
                                onChange={e => this.props.updateValue('followUp', e.target.innerHTML)} 
                            />
                        </div>
                        <div className='input-box-group report-page-section'>
                            <TextField
                                label={'OPCS4 Code'}
                                value={this.props.opsc4Code}
                                onChange={e => this.props.updateValue('opsc4Code', e.target.value)} 
                            />
                        </div>
                        <div className='input-box-group report-page-section'>
                            <span>Signature _____________________</span>
                        </div>
                    </div>
                    <div className='section-right report-attached-images'>
                        {this.props.attachedImages.map(imageSource => (
                            <ImageAttachment src={imageSource} />
                        ))}
                    </div>
                </div>
                <footer>
                </footer>
            </Page>
        );
    }
}



export default ColonoscopyReport;