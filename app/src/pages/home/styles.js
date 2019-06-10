import styled from 'styled-components';
import header from '../../assets/header.png';

export const Container = styled.div`
    .count-box {
        display: flex;
        justify-content: space-evenly;
        
        .count {
            font-size: 60px;
        }
    }
`;

export const Box = styled.div`
    background-color: ${props => props.color ? props.color : 'white'};
    color: ${props => props.text ? props.text : 'black'};
    padding: 20px;
`;

export const Header = styled.div`
    background-image: url(${header});
    background-repeat: no-repeat;
    background-size: cover;
    height: 500px; 
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding-left: 100px;

    span {
        color: #fff;
    }

    .title {
        font-size: 48px;
        text-shadow: 3px 3px #040224; 
    }

    .subtitle {
        text-shadow: 2px 2px #040224; 
    }

    
`