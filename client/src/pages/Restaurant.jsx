import apiServices from "../api/apis"
import Card from 'react-bootstrap/Card'
import Button from 'react-bootstrap/Button'
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'

function Restaurant() {
    return (
    <Container className="mt-3">
        <Row>
            <Card as={Col}>
                <Card.Body>
                    <Card.Title>Card Title</Card.Title>
                    <Card.Subtitle classname="mb-2 text-muted">Card Subtitle</Card.Subtitle>
                    <Card.Text>
                        Some quick example text to build on the card title and make up the bulk of
                        the card's content.
                    </Card.Text>
                    <Button variant="primary">Go somewhere</Button>
                </Card.Body>
            </Card>
            <Card as={Col}>
                <Card.Body>
                    <Card.Title>Card Title</Card.Title>
                    <Card.Subtitle classname="mb-2 text-muted">Card Subtitle</Card.Subtitle>
                    <Card.Text>
                        Some quick example text to build on the card title and make up the bulk of
                        the card's content.
                    </Card.Text>
                    <Button variant="primary">Go somewhere</Button>
                </Card.Body>
            </Card>
        </Row>
    </Container>
    )
}

export default Restaurant