import { useState } from "react"

export default function DeckList({ decklist }) {
    const [isShown, setIsShown] = useState(false)
    const deckArr = decklist.map((item => <li>{item}</li>))

    function toggleIsShown() {
        setIsShown(prevIsShown => !prevIsShown)
    }

    return (
        <>
        <div className="deck-container">
            <button className="deck-btn" onClick={toggleIsShown}>{isShown ? "Hide Decklist" : "Show Full Decklist"}</button>
            {isShown ? 
            <ul className="deck-ul">
                {deckArr}
            </ul> 
            : null}
        </div>
        </>
    )
}