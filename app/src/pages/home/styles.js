import styled from 'styled-components';

export const Container = styled.div``;

export const Box = styled.div`
    background-color: ${props => props.color ? props.color : 'white'};
    color: ${props => props.text ? props.text : 'black'};
    padding: 20px;
`;

export const Header = styled.div`
    background:
        linear-gradient(to bottom, rgba(26, 30, 228, 0.15), rgba(26, 30, 228, 0.5)),
        url(-);
    height: 300px; 
`