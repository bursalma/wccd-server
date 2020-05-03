import React from 'react';
import { 
  Form,
  Select,
  Input,
  Header,
  Button,
} from 'semantic-ui-react';

import SemanticDatepicker from 'react-semantic-ui-datepickers';

const CrimeInformationForm = ({ options, values, nextStep, prevStep, handleChange, handleDateChange }) => {
  return (
    <Form className='form'>
      <Header as='h2'>Crime Information</Header>
         <Form.Group>
           <Form.Field
            key='charges'
            control={Select} 
            options={options}
            placeholder='Charges' 
            width={6} 
            onChange={handleChange}
            defaultValue={values.charges}
            name='charges'
          />
          <Form.Field
            key='courtType'
            control={Select} 
            options={options}
            placeholder='Court Type' 
            width={6} 
            onChange={handleChange}
            defaultValue={values.courtType}
            name='courtType'
          />
          <Form.Field
            key='sentence'
            control={Select} 
            options={options}
            placeholder='Sentence' 
            width={6} 
            onChange={handleChange}
            defaultValue={values.sentence}
            name='sentence'
          />
        </Form.Group>
        <Form.Group>
          <Form.Field
            key='fine'
            control={Select} 
            options={options}
            placeholder='Fine'
            width={6} 
            onChange={handleChange}
            defaultValue={values.fine}
            name='fine'
          />
          <Form.Field
            key='decade'
            control={Select} 
            options={options}
            placeholder='Decade'
            width={6} 
            onChange={handleChange}
            defaultValue={values.decade}
            name='decade'
          />
          <Form.Field
            key='parole'
            control={Select} 
            options={options}
            placeholder='Parole'
            width={6} 
            onChange={handleChange}
            defaultValue={values.parole}
            name='parole'
          />
        </Form.Group>
        <Form.TextArea
            key='summary'
            data-gramm_editor="false" 
            placeholder='Summary about the conviction...'
            onChange={handleChange}
            defaultValue={values.summary}
            name='summary'
        />
        <Form.Group>
          <Form.Field
            key='sourceName'
            control={Input}
            placeholder='Source Name'
            width={6} 
            onChange={handleChange}
            defaultValue={values.sourceName}
            name='sourceName'
          />
          <Form.Input 
            key='sourceUrl'
            control={Input}
            placeholder='Source Url'
            width={6} 
            onChange={handleChange}
            defaultValue={values.sourceUrl}
            name='sourceUrl'
          />
          <SemanticDatepicker width={6} onChange={handleDateChange} format='MM/DD/YYYY' name='sourceDate'/>
        </Form.Group>
      <div className='form-navigation-buttons'>
        <Button content='Previous' icon='left arrow' labelPosition='left' floated='left' onClick={prevStep}/>
        <Button content='Next' icon='right arrow' labelPosition='right' floated='right' onClick={nextStep}/>
      </div>
    </Form>
  )
}

export default CrimeInformationForm;