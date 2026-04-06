import { useState, useEffect, useCallback, useRef } from "react";

// ═══════════════════════════════════════════════════
// DRIFTER LOOP — DIALOGUE ENGINE PROTOTYPE
// ═══════════════════════════════════════════════════

// ─── CAST DATA ───
const CAST = {
  "Артур": { id: "arthur", color: "#a0c4ff", nameBg: "#1a2a5acc", home: "security_desk" },
  "Елеонор": { id: "eleanor", color: "#d8b4fe", nameBg: "#3a1a5acc", home: "furniture" },
  "Летті": { id: "lettie", color: "#a5f3fc", nameBg: "#0a3a4acc", home: "medbay" },
  "Амір": { id: "amir", color: "#fef08a", nameBg: "#4a3f0acc", home: "arcade" },
  "Аоі": { id: "aoi", color: "#f0abfc", nameBg: "#4a1260cc", home: "music_shop" },
  "Квінсі": { id: "quincy", color: "#fca5a5", nameBg: "#5a1a1acc", home: "range" },
  "Дрифтер": { id: "mc", color: "#facc15", nameBg: "#a855f733", home: null },
};

// ─── DEMO SCENE SCRIPT ───
const DEMO_SCRIPT = [
  // Scene: Foodcourt, morning interrogation
  { type: "scene", bg: "foodcourt", text: "1 грудня / 09:00" },
  { type: "say", who: "Артур", text: "Сідай. Розмова буде коротка." },
  { type: "say", who: "Артур", text: "Ти знаєш хто ми. Ми знаємо хто ти. Питання — навіщо ти тут." },
  { type: "say", who: null, text: "Артур дивиться прямо. Не моргає." },
  {
    type: "menu",
    prompt: "Що відповісти?",
    choices: [
      { text: "Я тут допомогти.", next: "help_branch" },
      { text: "Я тут тому що більше нема куди.", next: "nowhere_branch" },
      { text: "...", next: "silence_branch" },
    ],
  },

  // ─── Branch: help ───
  { type: "label", id: "help_branch" },
  { type: "say", who: "Артур", text: "Допомогти." },
  { type: "say", who: "Артур", text: "Цікаво. Ніхто ще не приходив сюди з такою причиною." },
  { type: "say", who: "Квінсі", text: "lol sure. hero complex much?" },
  { type: "say", who: "Летті", text: "Квінсі. Заткнись." },
  { type: "jump", to: "after_choice" },

  // ─── Branch: nowhere ───
  { type: "label", id: "nowhere_branch" },
  { type: "say", who: "Артур", text: "Тоді ми однакові." },
  { type: "say", who: null, text: "Тиша. Амір дивиться в підлогу. Аоі — у вікно." },
  { type: "say", who: "Елеонор", text: "Ніхто з нас тут не за вибором." },
  { type: "jump", to: "after_choice" },

  // ─── Branch: silence ───
  { type: "label", id: "silence_branch" },
  { type: "say", who: null, text: "Мовчиш." },
  { type: "say", who: "Артур", text: "Добре. Мовчання — теж відповідь." },
  { type: "say", who: "Аоі", text: "...Мені подобається ця людина." },
  { type: "say", who: "Квінсі", text: "u literally know nothing about them" },
  { type: "say", who: "Аоі", text: "Саме тому." },
  { type: "jump", to: "after_choice" },

  // ─── After choice ───
  { type: "label", id: "after_choice" },
  { type: "say", who: "Артур", text: "Неважливо. Тепер ти тут. Правила прості." },
  { type: "say", who: "Артур", text: "Ми — Гекс. Шість осіб. Тепер сім." },
  { type: "say", who: "Амір", text: "Сім — щасливе число!" },
  { type: "say", who: "Летті", text: "Для кого як." },
  { type: "say", who: null, text: "Артур встає. Решта теж." },
  { type: "say", who: "Артур", text: "Мол великий. Огляньсь. Знайди мене коли будеш готовий." },

  // Pager demo
  { type: "pager", who: "Амір", text: "псс якщо заблукаєш — шукай мене в аркадах!" },
  { type: "say", who: null, text: "Пейджер пікає. Перше повідомлення." },

  // Scene transition
  { type: "scene", bg: "mall", text: "1 грудня / 11:00" },
  { type: "say", who: null, text: "Мол Гьольванії. Величезний. Порожній. Тихий." },
  { type: "say", who: null, text: "Десь грає музика. Десь хтось сміється. Десь — ні." },
  { type: "say", who: "Дрифтер", text: "...Де я опинився." },

  { type: "end", text: "Кінець демо. Натисни щоб перезапустити." },
];

// ─── BG COLORS (placeholder for actual backgrounds) ───
const BG_THEMES = {
  foodcourt: { bg: "linear-gradient(180deg, #0a0a14 0%, #1a1028 50%, #0d0d1a 100%)", label: "Футкорт" },
  mall: { bg: "linear-gradient(180deg, #0d1117 0%, #161b22 50%, #0d1117 100%)", label: "Мол Гьольванії" },
  arcade: { bg: "linear-gradient(180deg, #0a0618 0%, #1a0a30 50%, #0a0618 100%)", label: "Аркади" },
  medbay: { bg: "linear-gradient(180deg, #0a1218 0%, #0d2030 50%, #0a1218 100%)", label: "Медвідділ" },
};

// ─── TYPEWRITER HOOK ───
function useTypewriter(text, speed = 28) {
  const [displayed, setDisplayed] = useState("");
  const [done, setDone] = useState(false);
  const indexRef = useRef(0);

  useEffect(() => {
    setDisplayed("");
    setDone(false);
    indexRef.current = 0;
    if (!text) { setDone(true); return; }

    const iv = setInterval(() => {
      indexRef.current++;
      if (indexRef.current >= text.length) {
        setDisplayed(text);
        setDone(true);
        clearInterval(iv);
      } else {
        setDisplayed(text.slice(0, indexRef.current));
      }
    }, speed);
    return () => clearInterval(iv);
  }, [text, speed]);

  const skip = useCallback(() => {
    setDisplayed(text || "");
    setDone(true);
  }, [text]);

  return { displayed, done, skip };
}

// ═══════════════════════════════════════════════════
// MAIN COMPONENT
// ═══════════════════════════════════════════════════

export default function DrifterLoopPrototype() {
  const [pc, setPc] = useState(0); // program counter
  const [bg, setBg] = useState("mall");
  const [sceneTitle, setSceneTitle] = useState(null);
  const [sceneTitleVisible, setSceneTitleVisible] = useState(false);
  const [currentLine, setCurrentLine] = useState(null);
  const [menuData, setMenuData] = useState(null);
  const [pagerMessages, setPagerMessages] = useState([]);
  const [pagerOpen, setPagerOpen] = useState(false);
  const [pagerFlash, setPagerFlash] = useState(false);
  const [history, setHistory] = useState([]);
  const [ended, setEnded] = useState(false);
  const [speaking, setSpeaking] = useState(null);

  const { displayed, done, skip } = useTypewriter(
    currentLine?.text || "",
    22
  );

  // ─── Label index ───
  const labelMap = useRef({});
  useEffect(() => {
    const map = {};
    DEMO_SCRIPT.forEach((node, i) => {
      if (node.type === "label") map[node.id] = i;
    });
    labelMap.current = map;
  }, []);

  // ─── Execute node ───
  const execute = useCallback((index) => {
    if (index >= DEMO_SCRIPT.length) { setEnded(true); return; }
    const node = DEMO_SCRIPT[index];

    switch (node.type) {
      case "scene":
        setBg(node.bg);
        setCurrentLine(null);
        setMenuData(null);
        setSpeaking(null);
        setSceneTitle(node.text);
        setSceneTitleVisible(true);
        setTimeout(() => {
          setSceneTitleVisible(false);
          setTimeout(() => setPc(index + 1), 600);
        }, 2000);
        break;

      case "say":
        setSpeaking(node.who);
        setCurrentLine({ who: node.who, text: node.text });
        setMenuData(null);
        break;

      case "menu":
        setMenuData(node);
        setCurrentLine(null);
        setSpeaking(null);
        break;

      case "label":
        setPc(index + 1);
        break;

      case "jump":
        const target = labelMap.current[node.to];
        if (target !== undefined) setPc(target + 1);
        break;

      case "pager":
        setPagerMessages((prev) => [...prev, { who: node.who, text: node.text }]);
        setPagerFlash(true);
        setTimeout(() => setPagerFlash(false), 2000);
        setPc(index + 1);
        break;

      case "end":
        setEnded(true);
        setCurrentLine({ who: null, text: node.text });
        break;

      default:
        setPc(index + 1);
    }
  }, []);

  useEffect(() => {
    execute(pc);
  }, [pc, execute]);

  // ─── Advance ───
  const advance = () => {
    if (ended) {
      // restart
      setPc(0);
      setEnded(false);
      setHistory([]);
      setPagerMessages([]);
      setCurrentLine(null);
      setMenuData(null);
      return;
    }
    if (menuData) return;
    if (sceneTitleVisible) return;
    if (!done) { skip(); return; }
    if (currentLine) {
      setHistory((h) => [...h, currentLine]);
    }
    setPc(pc + 1);
  };

  const chooseOption = (choice) => {
    setHistory((h) => [...h, { who: "Дрифтер", text: choice.text, isChoice: true }]);
    setMenuData(null);
    const target = labelMap.current[choice.next];
    if (target !== undefined) setPc(target + 1);
  };

  const bgTheme = BG_THEMES[bg] || BG_THEMES.mall;
  const charData = currentLine?.who ? CAST[currentLine.who] : null;

  return (
    <div
      onClick={advance}
      style={{
        width: "100%",
        height: "100vh",
        background: bgTheme.bg,
        position: "relative",
        overflow: "hidden",
        cursor: menuData ? "default" : "pointer",
        fontFamily: "'Segoe UI', system-ui, sans-serif",
        userSelect: "none",
      }}
    >
      {/* ── Ambient grain ── */}
      <div style={{
        position: "absolute", inset: 0, opacity: 0.03,
        backgroundImage: `url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E")`,
        pointerEvents: "none",
      }} />

      {/* ── Scene title overlay ── */}
      {sceneTitle && (
        <div style={{
          position: "absolute", inset: 0, display: "flex",
          alignItems: "center", justifyContent: "center",
          background: "#000000cc", zIndex: 50,
          opacity: sceneTitleVisible ? 1 : 0,
          transition: "opacity 0.6s ease",
          pointerEvents: "none",
        }}>
          <div style={{
            fontSize: 32, color: "#ffffff90",
            letterSpacing: 6, fontWeight: 200,
          }}>
            {sceneTitle}
          </div>
        </div>
      )}

      {/* ── HUD top bar ── */}
      <div style={{
        position: "absolute", top: 0, left: 0, right: 0,
        padding: "12px 20px", display: "flex",
        justifyContent: "space-between", alignItems: "center",
        background: "linear-gradient(180deg, #00000088 0%, transparent 100%)",
        zIndex: 10,
      }}>
        <div style={{ display: "flex", gap: 16, alignItems: "center" }}>
          <span style={{ color: "#ffffff50", fontSize: 13, letterSpacing: 2 }}>
            {bgTheme.label}
          </span>
        </div>
        <div style={{ display: "flex", gap: 12, alignItems: "center" }}>
          <span style={{ color: "#facc15", fontSize: 13 }}>★ Ранг 1</span>
          <span style={{ color: "#ffffff30", fontSize: 13 }}>|</span>
          <span style={{ color: "#ffffff50", fontSize: 13 }}>0 крон</span>
        </div>
      </div>

      {/* ── Pager (bottom-left) ── */}
      <div
        onClick={(e) => { e.stopPropagation(); setPagerOpen(!pagerOpen); }}
        style={{
          position: "absolute", bottom: 200, left: 20, zIndex: 30,
          width: 52, height: 88, borderRadius: 8,
          background: pagerFlash
            ? "linear-gradient(180deg, #2a1a3a 0%, #1a0a2a 100%)"
            : "linear-gradient(180deg, #1a1a2a 0%, #0d0d1a 100%)",
          border: pagerFlash ? "1px solid #a855f7" : "1px solid #ffffff15",
          cursor: "pointer", display: "flex", flexDirection: "column",
          alignItems: "center", justifyContent: "center", gap: 4,
          transition: "all 0.3s ease",
          boxShadow: pagerFlash ? "0 0 20px #a855f740" : "none",
        }}
      >
        <div style={{
          width: 32, height: 14, borderRadius: 2,
          background: pagerMessages.length > 0 ? "#a855f7" : "#ffffff15",
          display: "flex", alignItems: "center", justifyContent: "center",
        }}>
          <span style={{ fontSize: 7, color: "#000", fontWeight: 700 }}>
            {pagerMessages.length > 0 ? pagerMessages.length : "—"}
          </span>
        </div>
        <div style={{ display: "flex", gap: 3 }}>
          {["◄", "●", "►"].map((b, i) => (
            <div key={i} style={{
              width: 12, height: 12, borderRadius: 2,
              background: "#ffffff08", display: "flex",
              alignItems: "center", justifyContent: "center",
              fontSize: 6, color: "#ffffff30",
            }}>{b}</div>
          ))}
        </div>
      </div>

      {/* ── Pager popup ── */}
      {pagerOpen && pagerMessages.length > 0 && (
        <div
          onClick={(e) => e.stopPropagation()}
          style={{
            position: "absolute", bottom: 300, left: 20, zIndex: 40,
            width: 280, background: "#0d0d1aee",
            border: "1px solid #a855f740", borderRadius: 8,
            padding: 12, display: "flex", flexDirection: "column", gap: 8,
          }}
        >
          <div style={{ fontSize: 10, color: "#a855f7", letterSpacing: 2, marginBottom: 4 }}>
            ПЕЙДЖЕР
          </div>
          {pagerMessages.map((msg, i) => (
            <div key={i} style={{
              padding: "8px 10px", background: "#ffffff06", borderRadius: 6,
            }}>
              <span style={{
                color: CAST[msg.who]?.color || "#fff",
                fontSize: 11, fontWeight: 600,
              }}>{msg.who}</span>
              <div style={{ color: "#ffffff80", fontSize: 12, marginTop: 2 }}>
                {msg.text}
              </div>
            </div>
          ))}
        </div>
      )}

      {/* ── Dialogue box area ── */}
      <div style={{
        position: "absolute", bottom: 0, left: 0, right: 0,
        padding: "0 20px 24px", zIndex: 20,
      }}>
        {/* ── Menu choices ── */}
        {menuData && (
          <div style={{
            marginBottom: 16, display: "flex",
            flexDirection: "column", gap: 6, maxWidth: 600,
          }}>
            <div style={{
              fontSize: 13, color: "#ffffff40", marginBottom: 4,
              letterSpacing: 1,
            }}>
              {menuData.prompt}
            </div>
            {menuData.choices.map((ch, i) => (
              <button
                key={i}
                onClick={(e) => { e.stopPropagation(); chooseOption(ch); }}
                style={{
                  background: "#a855f70a", border: "1px solid #a855f725",
                  borderRadius: 6, padding: "12px 18px",
                  color: "#d8b4fe", fontSize: 14, textAlign: "left",
                  cursor: "pointer", transition: "all 0.15s ease",
                  fontFamily: "inherit",
                }}
                onMouseEnter={(e) => {
                  e.target.style.background = "#a855f718";
                  e.target.style.borderColor = "#a855f750";
                }}
                onMouseLeave={(e) => {
                  e.target.style.background = "#a855f70a";
                  e.target.style.borderColor = "#a855f725";
                }}
              >
                {ch.text}
              </button>
            ))}
          </div>
        )}

        {/* ── Say window ── */}
        {currentLine && (
          <div style={{
            background: "#09090fdd",
            backdropFilter: "blur(12px)",
            borderRadius: 8,
            padding: 0,
            maxWidth: 640,
            border: "1px solid #ffffff08",
          }}>
            {/* Name tag */}
            {currentLine.who && (
              <div style={{
                display: "inline-block",
                background: charData?.nameBg || "#ffffff15",
                padding: "6px 16px",
                borderRadius: "8px 0 8px 0",
                marginBottom: 0,
              }}>
                <span style={{
                  color: charData?.color || "#fff",
                  fontSize: 13, fontWeight: 600,
                  letterSpacing: 1,
                }}>
                  {currentLine.who}
                </span>
              </div>
            )}
            {/* Text */}
            <div style={{
              padding: "14px 20px 16px",
              color: currentLine.who ? "#ffffffcc" : "#ffffff80",
              fontSize: 15,
              lineHeight: 1.6,
              fontStyle: currentLine.who ? "normal" : "italic",
              minHeight: 28,
            }}>
              {displayed}
              {!done && (
                <span style={{
                  opacity: 0.4,
                  animation: "blink 0.8s infinite",
                }}>▌</span>
              )}
            </div>
          </div>
        )}

        {/* ── Click indicator ── */}
        {done && currentLine && !menuData && !ended && (
          <div style={{
            textAlign: "right", marginTop: 6, paddingRight: 8,
          }}>
            <span style={{
              color: "#ffffff20", fontSize: 11,
              animation: "pulse 1.5s infinite",
            }}>
              ▼
            </span>
          </div>
        )}
      </div>

      {/* ── History (scrollback) — press H ── */}
      <style>{`
        @keyframes blink {
          0%, 100% { opacity: 0.4; }
          50% { opacity: 0; }
        }
        @keyframes pulse {
          0%, 100% { opacity: 0.2; }
          50% { opacity: 0.5; }
        }
      `}</style>
    </div>
  );
}