import React from 'react';
import { 
  Table,
  Container,
  Button,
} from 'semantic-ui-react';

import './convict-table.component.css';

const ConvictTable = ({ data, openModal }) => {
  return (
    <Container className='table-container' text>
      <div className='table-header-container'>
        <h1>Convict Table</h1>
        <Button primary floated='right' animated='fade' onClick={openModal}>
          <Button.Content visible>Add Record</Button.Content>
          <Button.Content hidden>+</Button.Content>
        </Button>
      </div>
      <Table celled>
        <Table.Header>
          <Table.Row>
            <Table.HeaderCell>Name</Table.HeaderCell>
            <Table.HeaderCell>Crime</Table.HeaderCell>
            <Table.HeaderCell>Date</Table.HeaderCell>
          </Table.Row>
        </Table.Header>

        <Table.Body>
          {
            data.map((record) => (
              <Table.Row>
                <Table.Cell>{record.name}</Table.Cell>
                <Table.Cell>{record.crime}</Table.Cell>
                <Table.Cell>{record.date}</Table.Cell>
              </Table.Row>
            ))
          }
        </Table.Body>
      </Table>
    </Container>
  );
}

export default ConvictTable;