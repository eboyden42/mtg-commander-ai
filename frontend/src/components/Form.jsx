export default function Form({ handleSubmit }) {

  return (
    <>
    <div className="form-container">
      <h3>Input a description below to generate a decklist</h3>
      <form onSubmit={handleSubmit}>
        <input type="text" name="description"/>
        <button>Create decklist</button>
      </form>
    </div>
    </>
  )
}