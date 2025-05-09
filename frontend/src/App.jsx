import { useState } from 'react'
import Form from './components/Form.jsx'
import CommanderDeck from './components/CommanderDeck.jsx'
import Header from './components/Header.jsx'

function App() {
  const [generatedResponse, setGeneratedResponse] = useState(null)
  const api_url = import.meta.env.VITE_APP_API_DIST_URL

  function handleSubmit(event) {
    event.preventDefault()
    const formData = new FormData(event.currentTarget)
    const description = formData.get("description")
    event.currentTarget.reset()

    fetch(api_url, { 
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ description }),
    })
      .then((res) => res.json())
      .then((data) => {
        // console.log("Data:")
        console.log(data)
        setGeneratedResponse(data.message ? createDecks(data.message) : "Request failed...");
      })
      .catch((err) => console.error('Error:', err));
  }

  function createDecks(message) {
    let decks = []
    for (let i = 0; i < message.length; i ++) {
      //  console.log(message[i].commander, message[i].decklist, message[i].description)
       decks.push(<CommanderDeck commander={message[i].commander} decklist={message[i].decklist} description={message[i].description}/>)
    }
    return decks
  }

  return (
    <>
      {/* <Header /> */}
      <Form handleSubmit={handleSubmit} />
      <div>
        {generatedResponse}
      </div>
    </>
  )
}

export default App
