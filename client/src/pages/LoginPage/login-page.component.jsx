import React from "react";
import { Grid, Header } from 'semantic-ui-react'

import LoginForm from "../../components/login-form/login-form.component";

import "./login-page.styles.css";

const LoginPage = () => {
  return (
    <Grid textAlign="center" style={{ height: "100vh" }} verticalAlign="middle">
      <Grid.Column style={{ maxWidth: 450 }}>
        <Header as="h2" color="teal" textAlign="center">
          Log-in to your account
        </Header>
        <LoginForm />
      </Grid.Column>
    </Grid>
  );
};

export default LoginPage;
