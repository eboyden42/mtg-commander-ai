import DeckList from "./DeckList"

export default function CommanderDeck({ commander, decklist, description }) {
    return (
        <>
        <div className="commander-container fade-in" >
            <h1>Commander: {commander}</h1>
            <DeckList decklist={decklist} />
            <p>{description}</p>
        </div>
        </>
    )
}