import React from 'react';
import ConvictTable from '../../components/convict-table/convict-table.component';
import ConvictForm from '../../components/convict-form/convict-form.component';
import {
  Modal
} from 'semantic-ui-react';

import './home-page.styles.css';

class HomePage extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      data: [
        {name: 'Ali Ciftci', crime: 'Murder', date: '1-1-2020'},
        {name: 'Muhammed Ali Bursal', crime: 'Murder', date: '1-1-2020'},
        {name: 'Ismail Dama', crime: 'Murder', date: '1-1-2020'},
      ],
      formOpen: false,
    }
  }

  openModal = () => {
    this.setState({ formOpen: true });
  }

  closeModal = () => {
    this.setState({ formOpen: false });
  }

  render() {
    return (
      <div className="home">
        <ConvictTable data={this.state.data} openModal={this.openModal}/>
        <Modal
          open={this.state.formOpen}
          onClose={this.closeModal}
          centered
          size='large'
        >
          <ConvictForm handleSubmit></ConvictForm>
        </Modal>
      </div>
    );
  }
}

export default HomePage;