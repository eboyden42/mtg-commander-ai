export default function CommanderDeck({ commander, decklist, description }) {

    // const deckArr = decklist.map((item => <li>{item}</li>))

    return (
        <>
        <div className="commander-container" >
            <h1>Commander: {commander}</h1>
            <ul>
                {decklist}
            </ul>
            <p>{description}</p>
        </div>
        </>
    )
}