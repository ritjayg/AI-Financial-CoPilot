/**
 * Backend base URL: Vite proxy sends /api → FastAPI in dev.
 */
const BASE = import.meta.env.VITE_API_URL || "";

export async function fetchChatStatus() {
  const res = await fetch(`${BASE}/api/chat/status`);
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  return res.json();
}
