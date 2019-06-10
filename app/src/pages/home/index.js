import React, { Component } from 'react';

import { Container, Box, Header } from './styles';
import { Chart } from "react-google-charts";

export default class Home extends Component {
  render() {
    return (
        <Container>
            <Header>
                <span className="title">Lorem ipsum</span>
                <span className="subtitle">Lorem ipsum</span>
            </Header>

            <Box className="count-box" color="#390e3d" text="white">
              <div className="divider">
                <p><span className="count">50.000</span> projetos em andamento</p>
                <p><span className="count">11.525</span> relacionados a educação</p>
              </div>

              <div className="divider">
                <p><span className="count">5.548</span> relacionados a saúde</p>
                <p><span className="count">38.146</span> relacionados a tecnologia</p>
              </div>
            </Box>
            <Box>
              <Chart
                chartType="ScatterChart"
                data={[["Age", "Weight"], [4, 5.5], [8, 12]]}
                height="400px"
                legendToggle
              />
            </Box>
            <Box color="#af3365" text="white">Aute quis mollit Lorem eu consequat tempor. Incididunt nulla qui minim pariatur ullamco. Proident esse laboris magna exercitation mollit dolor nulla. Tempor aute magna excepteur elit aliquip elit incididunt commodo ea cupidatat ex esse occaecat aute. Sint nulla culpa ex qui incididunt deserunt deserunt commodo. Velit mollit enim adipisicing ea labore excepteur id pariatur ipsum nulla duis.</Box>
            <Box>Consequat magna dolor excepteur sit. Cillum cupidatat tempor proident pariatur. Qui nostrud non nisi consectetur ut ad irure non ut. Laboris ex ullamco minim dolor excepteur magna aliquip. Pariatur minim labore ex nulla nostrud fugiat esse excepteur non.</Box>
        </Container>
    );
  }
}
