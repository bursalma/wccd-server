import React from 'react';

import PersonalInformationForm from '../personal-information-form/personal-information-form.component'
import CrimeInformationForm from '../crime-information-form.component/crime-information-form.component'

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

  handleChange = event => {
    this.setState({ values: {
      ...this.state.values,
      [event.target.name] : event.target.value 
    }})
  }

  handleDateChange = (event, data) => {
    this.setState({ values: {
      ...this.state.values,
      'sourceDate' : data.value
    }})
  }

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
                values={values}
                options={options}
                />
      case 2:
        return <CrimeInformationForm
                nextStep={this.nextStep}
                prevStep={this.prevStep}
                handleChange={this.handleChange}
                handleDateChange={this.handleDateChange}
                values={values}
                options={options}
                />
      case 3:
        return <PersonalInformationForm
                nextStep={this.nextStep}
                prevStep={this.prevStep}
                handleChange={this.handleChange}
                values={values}
                options={options}
                />
      default:
        return <h1>Success!</h1>
    }
  }
}

export default ConvictForm;