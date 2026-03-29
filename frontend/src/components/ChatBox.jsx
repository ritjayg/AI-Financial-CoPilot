import { useState } from "react";
import { fetchChatStatus } from "../api.js";

export default function ChatBox() {
  const [status, setStatus] = useState(null);
  const [loading, setLoading] = useState(false);

  async function checkBackend() {
    setLoading(true);
    try {
      const data = await fetchChatStatus();
      setStatus(JSON.stringify(data, null, 2));
    } catch (e) {
      setStatus(String(e));
    } finally {
      setLoading(false);
    }
  }

  return (
    <section className="chat">
      <p className="chat__hint">Placeholder UI — wire POST /chat when the backend is ready.</p>
      <button type="button" className="chat__btn" onClick={checkBackend} disabled={loading}>
        {loading ? "Checking…" : "Ping chat API status"}
      </button>
      {status && <pre className="chat__out">{status}</pre>}
    </section>
  );
}
