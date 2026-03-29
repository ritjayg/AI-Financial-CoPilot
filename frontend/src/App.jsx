import ChatBox from "./components/ChatBox.jsx";
import "./App.css";

export default function App() {
  return (
    <div className="app">
      <header className="app__header">
        <h1>AI Financial Copilot</h1>
        <p className="app__tagline">Full-stack scaffold — connect agents and chat next.</p>
      </header>
      <main className="app__main">
        <ChatBox />
      </main>
    </div>
  );
}
