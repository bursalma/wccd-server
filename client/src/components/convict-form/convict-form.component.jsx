import React, { useState } from 'react';
import { 
  Form,
  Select,
  Input,
  Header,
  Divider,
} from 'semantic-ui-react';
import SemanticDatepicker from 'react-semantic-ui-datepickers';

import PersonalInformationForm from '../personal-information-form/personal-information-form.component'

import 'react-semantic-ui-datepickers/dist/react-semantic-ui-datepickers.css';
import './convict-form.component.css';

class ConvictForm extends React.Component {
  constructor(props){
    super(props)

    this.state = {
      step: 1,
      values: {
        firstName: '',
        middleName: '',
        lastName: '',
        sex: '',
        race: '',
        nationality: '',
        ageGroup: '',
        company: '',
        affiliation: '',
        charges: '',
        courtType: '',
        sentences: '',
        fine: '',
        decade: '',
        parole: '',
        summary: '',
        sourceName: '',
        sourceUrl: '',
        sourceDate: '',
      }
    }
  }

  nextStep = () => {
    const { step } = this.state
    this.setState({
        step : step + 1
    })
  }

  prevStep = () => {
    const { step } = this.state
    this.setState({
        step : step - 1
    })
  }

  handleChange = input => event => {
    console.log(input);
    this.setState({ values: {
      ...this.state.values,
      [input] : event.target.value 
    }})
  }

  // cancelForm = (e) => {
  //   e.preventDefault();

  //   for(let field in this.state.values){
  //     this.setState({ values: {
  //       ...this.state.values,
  //       [field] : ''
  //     }})
  //   }

  //   this.setState({step: 1})
  // }

  render(){
    const { values, step } = this.state;
    const options = [
      { key: 'x', text: 'Waiting for Data', value: 'x'}
    ]

    switch(step){
      case 1: 
        return <PersonalInformationForm
                nextStep={this.nextStep}
                handleChange={this.handleChange}
                // cancelForm={this.cancelForm}
                values={values}
                options={options}
                />
      case 2:
        return <PersonalInformationForm
                nextStep={this.nextStep}
                prevStep={this.prevStep}
                handleChange={this.handleChange}
                // cancelForm={this.cancelForm}
                values={values}
                options={options}
                />
      case 3:
        return <PersonalInformationForm
                nextStep={this.nextStep}
                prevStep={this.prevStep}
                handleChange={this.handleChange}
                // cancelForm={this.cancelForm}
                values={values}
                options={options}
                />
      default:
        return <h1>Success!</h1>
    }
  }

  // return (
    
  //     <Form className='form'>
  //       {/* Convict Information */}
  //       <Header as='h2'>Convict Information</Header>
  //       <Form.Group>
  //         <Form.Field control={Input} placeholder='First Name' width={6} />
  //         <Form.Field control={Input} placeholder='Middle Name' width={4} />
  //         <Form.Field control={Input} placeholder='Last Name' width={6} />
  //       </Form.Group>
  //       <Form.Group>
  //         <Form.Field
  //           control={Select}
  //           options={placeholder}
  //           placeholder='Gender'
  //           width={4}
  //         />
  //         <Form.Field
  //           control={Select}
  //           options={placeholder}
  //           placeholder='Race'
  //           width={6}
  //         />
  //         <Form.Field
  //           control={Select}
  //           options={placeholder}
  //           placeholder='Nationality'
  //           width={6}
  //         />
  //       </Form.Group>
  //       <Form.Group>
  //         <Form.Field
  //           control={Select}
  //           options={placeholder}
  //           placeholder='Age Group'
  //           width={6}
  //         />
  //         <Form.Field
  //           control={Select}
  //           options={placeholder}
  //           placeholder='Company'
  //           width={6}
  //         />
  //         <Form.Field
  //           control={Select}
  //           options={placeholder}
  //           placeholder='Affiliation'
  //           width={4}
  //         />
  //       </Form.Group>
  //       <Divider section/>

  //       {/* Crime Information */}
  //       <Header as='h2'>Crime Information</Header>
  //       <Form.Group>
  //         <Form.Field
  //           control={Select}
  //           options={placeholder}
  //           placeholder='Charges'
  //           width={6}
  //         />
  //         <Form.Field
  //           control={Select}
  //           options={placeholder}
  //           placeholder='Court Type'
  //           width={6}
  //         />
  //         <Form.Field
  //           control={Select}
  //           options={placeholder}
  //           placeholder='Sentence'
  //           width={4}
  //         />
  //       </Form.Group>
  //       <Form.Group>
  //         <Form.Field
  //           control={Select}
  //           options={placeholder}
  //           placeholder='Fine'
  //           width={6}
  //         />
  //         <Form.Field
  //           control={Select}
  //           options={placeholder}
  //           placeholder='Decade'
  //           width={6}
  //         />
  //         <Form.Field
  //           control={Select}
  //           options={placeholder}
  //           placeholder='Parole'
  //           width={4}
  //         />
  //       </Form.Group>
  //       <Form.TextArea placeholder='Summary about the conviction...' />
  //       <Form.Group>
  //         <Form.Field
  //           control={Input}
  //           placeholder='Source Name'
  //           width={6}
  //         />
  //         <Form.Input 
  //           control={Input}
  //           placeholder='Source Url' 
  //           width={6}
  //         />
  //         <SemanticDatepicker />
  //       </Form.Group>
  //     </Form>
  // );
}

export default ConvictForm;