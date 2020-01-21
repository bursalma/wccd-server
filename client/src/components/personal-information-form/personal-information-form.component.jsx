import React from 'react';
import { 
  Form,
  Select,
  Input,
  Header,
  Button,
} from 'semantic-ui-react';

const PersonalInformationForm = ({ options, values, nextStep, handleChange }) => {

  const saveAndContinue = (e) => {
    e.preventDefault();
    nextStep();
  }

  // const goBack = (e) => {
  //   e.preventDefault();
  //   prevStep();
  // }

  return (
    <Form className='form'>
      <Header as='h2'>Convict Information</Header>
      <Form.Group>
        <Form.Field
          key='firstName'
          control={Input} 
          placeholder='First Name' 
          width={6} 
          onChange={handleChange('firstName')}
          //defaultValue={values.firstName}
        />
        <Form.Field
          key='middleName'
          control={Input} 
          placeholder='Middle Name' 
          width={4}
          onChange={handleChange('middleName')}
          defaultValue={values.middleName}
        />
        <Form.Field
          key='lastName'
          control={Input} 
          placeholder='Last Name' 
          width={6}
          onChange={handleChange('lastName')}
          defaultValue={values.lastName}
        />
      </Form.Group>
      <Form.Group>
        <Form.Field
          key='sex'
          control={Select}
          options={options}
          placeholder='Sex'
          width={4}
          onChange={handleChange('sex')}
          defaultValue={values.sex}
        />
        <Form.Field
          key='race'
          control={Select}
          options={options}
          placeholder='Race'
          width={6}
          onChange={handleChange('race')}
          defaultValue={values.race}
        />
        <Form.Field
          key='nationality'
          control={Select}
          options={options}
          placeholder='Nationality'
          width={6}
          onChange={handleChange('nationality')}
          defaultValue={values.nationality}
        />
      </Form.Group>
      <Form.Group>
        <Form.Field
          key='ageGroup'
          control={Select}
          options={options}
          placeholder='Age Group'
          width={6}
          onChange={handleChange('ageGroup')}
          defaultValue={values.ageGroup}
        />
        <Form.Field
          key='company'
          control={Select}
          options={options}
          placeholder='Company'
          width={6}
          onChange={handleChange('company')}
          defaultValue={values.company}
        />
        <Form.Field
          key='affiliation'
          control={Select}
          options={options}
          placeholder='Affiliation'
          width={4}
          onChange={handleChange('affiliation')}
          defaultValue={values.affiliation}
        />
      </Form.Group>
      {/* <Button onClick={goBack} secondary>Back</Button> */}
      <Button onClick={saveAndContinue} primary>Save & Continue</Button>
    </Form>
  )
}

export default PersonalInformationForm;