import React, { Component } from 'react';
import { withRouter } from 'react-router-dom';
import { compose } from 'recompose';
import { withFirebase } from '../firebase/context';
import { Button, Form, Segment, Message } from 'semantic-ui-react'

const INITIAL_STATE = {
  email: '',
  password: '',
  error: null,
}

class LoginForm extends Component {
  constructor(props) {
    super(props);
    this.state = {...INITIAL_STATE };
  }

  onSubmit = event => {
    const { email, password } = this.state;
    this.props.firebase
      .doSignInWithEmailAndPassword(email, password)
      .then(() => {
        this.setState({ ...INITIAL_STATE });
        this.props.history.push('/');
      })
      .catch(error => {
        this.setState({ error });
      });
    event.preventDefault();
  };

  onChange = event => {
    this.setState({ [event.target.name]: event.target.value });
  };

  render() {
    const { email, password, error } = this.state;
    const isInvalid = password === '' || email === '';
    return (
      <Form size='large' onSubmit={this.onSubmit}>
        <Segment stacked>
          <Form.Input 
            fluid 
            icon='user' 
            iconPosition='left' 
            placeholder='Email Address'
            name='email'
            onChange={this.onChange}
          />
          <Form.Input
            fluid
            icon='lock'
            iconPosition='left'
            placeholder='Password'
            type='password'
            name='password'
            onChange={this.onChange}
          />
          <Button color='teal' fluid size='large' disabled={isInvalid} type="submit">
            Sign In
          </Button>
          {error && 
            <Message>
              {error.message}
            </Message>}
        </Segment>
      </Form>
    );
  }
}

export default compose(
  withRouter,
  withFirebase,
)(LoginForm);
