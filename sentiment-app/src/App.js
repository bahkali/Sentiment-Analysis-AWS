import "./App.css";

function App() {
  return (
    <div className="App">
      <h3>Input</h3>
      <label htmlFor="markdown-content">Enter some markdown</label>
      <textarea id="markdown-content" />
      <h3>Output</h3>
      <div className="content" />
    </div>
  );
}

export default App;
