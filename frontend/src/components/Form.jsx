export default function Form({ handleSubmit }) {

  return (
    <>
    <h1>What deck should I create?</h1>
    <div className="form-container">
      <form onSubmit={handleSubmit}>
        <input type="text" name="description" placeholder="a pirate tribal deck"/>
        <button>Create decklist</button>
      </form>
    </div>
    </>
  )
}