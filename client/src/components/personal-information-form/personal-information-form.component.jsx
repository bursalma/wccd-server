import React from 'react';
import { 
  Form,
  Select,
  Input,
  Header,
  Button,
} from 'semantic-ui-react';

const PersonalInformationForm = ({ options, values, nextStep, handleChange }) => {

  return (
    <Form className='form'>
      <Header as='h2'>Convict Information</Header>
      <Form.Group>
        <Form.Field
          key='firstName'
          control={Input} 
          placeholder='First Name' 
          width={6} 
          onChange={handleChange}
          defaultValue={values.firstName}
          name='firstName'
        />
        <Form.Field
          key='middleName'
          control={Input} 
          placeholder='Middle Name' 
          width={4}
          onChange={handleChange}
          defaultValue={values.middleName}
          name='middleName'
        />
        <Form.Field
          key='lastName'
          control={Input} 
          placeholder='Last Name' 
          width={6}
          onChange={handleChange}
          defaultValue={values.lastName}
          name='lastName'
        />
      </Form.Group>
      <Form.Group>
        <Form.Field
          key='sex'
          control={Select}
          options={options}
          placeholder='Sex'
          width={4}
          onChange={handleChange}
          defaultValue={values.sex}
          name='sex'
        />
        <Form.Field
          key='race'
          control={Select}
          options={options}
          placeholder='Race'
          width={6}
          onChange={handleChange}
          defaultValue={values.race}
          name='race'
        />
        <Form.Field
          key='nationality'
          control={Select}
          options={options}
          placeholder='Nationality'
          width={6}
          onChange={handleChange}
          defaultValue={values.nationality}
          name='nationality'
        />
      </Form.Group>
      <Form.Group>
        <Form.Field
          key='ageGroup'
          control={Select}
          options={options}
          placeholder='Age Group'
          width={6}
          onChange={handleChange}
          defaultValue={values.ageGroup}
          name='ageGroup'
        />
        <Form.Field
          key='company'
          control={Select}
          options={options}
          placeholder='Company'
          width={6}
          onChange={handleChange}
          defaultValue={values.company}
          name='company'
        />
        <Form.Field
          key='affiliation'
          control={Select}
          options={options}
          placeholder='Affiliation'
          width={4}
          onChange={handleChange}
          defaultValue={values.affiliation}
          name='affiliation'
        />
      </Form.Group>
      <div className='form-navigation-buttons'>
        <Button content='Next' icon='right arrow' labelPosition='right' floated='right' onClick={nextStep}/>
      </div>
    </Form>
  )
}

export default PersonalInformationForm;