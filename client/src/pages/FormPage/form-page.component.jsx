import React from 'react';
import { 
  Form, 
  Container,
  Select,
  Input,
  Header,
  Divider,
} from 'semantic-ui-react';
import SemanticDatepicker from 'react-semantic-ui-datepickers';

import 'react-semantic-ui-datepickers/dist/react-semantic-ui-datepickers.css';
import './form-page.component.css';

const FormPage = () => {
  const genders = [
    { key: 'm', text: 'Male', value: 'male' },
    { key: 'f', text: 'Female', value: 'female' },
    { key: 'o', text: 'Other', value: 'other' },
  ]

  const placeholder = [
    { key: 'x', text: 'Waiting for Data', value: 'x'}
  ]

  // const handleChange = (e, { name, value }) => this.setState({ [name]: value })

  // const handleSubmit = () => {
    
  // }

  return (
    <Container className='form-container'>
      <Form className='form'>
        {/* Convict Information */}
        <Header as='h2'>Convict Information</Header>
        <Form.Group>
          <Form.Field control={Input} placeholder='First Name' width={6} />
          <Form.Field control={Input} placeholder='Middle Name' width={4} />
          <Form.Field control={Input} placeholder='Last Name' width={6} />
        </Form.Group>
        <Form.Group>
          <Form.Field
            control={Select}
            options={genders}
            placeholder='Gender'
            width={4}
          />
          <Form.Field
            control={Select}
            options={placeholder}
            placeholder='Race'
            width={6}
          />
          <Form.Field
            control={Select}
            options={placeholder}
            placeholder='Nationality'
            width={6}
          />
        </Form.Group>
        <Form.Group>
          <Form.Field
            control={Select}
            options={placeholder}
            placeholder='Age Group'
            width={6}
          />
          <Form.Field
            control={Select}
            options={placeholder}
            placeholder='Company'
            width={6}
          />
          <Form.Field
            control={Select}
            options={placeholder}
            placeholder='Affiliation'
            width={4}
          />
        </Form.Group>
        <Divider section/>

        {/* Crime Information */}
        <Header as='h2'>Crime Information</Header>
        <Form.Group>
          <Form.Field
            control={Select}
            options={placeholder}
            placeholder='Charges'
            width={6}
          />
          <Form.Field
            control={Select}
            options={placeholder}
            placeholder='Court Type'
            width={6}
          />
          <Form.Field
            control={Select}
            options={placeholder}
            placeholder='Sentence'
            width={4}
          />
        </Form.Group>
        <Form.Group>
          <Form.Field
            control={Select}
            options={placeholder}
            placeholder='Fine'
            width={6}
          />
          <Form.Field
            control={Select}
            options={placeholder}
            placeholder='Decade'
            width={6}
          />
          <Form.Field
            control={Select}
            options={placeholder}
            placeholder='Parole'
            width={4}
          />
        </Form.Group>
        <Form.TextArea placeholder='Summary about the conviction...' />
        <Form.Group>
          <Form.Field
            control={Input}
            placeholder='Source Name'
            width={6}
          />
          <Form.Input 
            control={Input}
            placeholder='Source Url' 
            width={6}
          />
          <SemanticDatepicker />
        </Form.Group>
      </Form>
    </Container>
  );
}

export default FormPage;