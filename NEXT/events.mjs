// Кожна подія — тільки дані, без власної програмної логіки.
export const events = [
  {
    id: "mission_return",
    title: "Повернення з місії",
    description: "Початкова подія. Обери наслідок місії — зміняться доступні епізоди.",
    priority: 100,
    once: true,
    when: { op: "eq", path: "location", value: "garage" },
    choices: [
      { id: "injured", label: "Артур повернувся пораненим", effects: [
        { op: "set_flag", key: "mission_done", value: true },
        { op: "set_flag", key: "arthur_injured", value: true }
      ] },
      { id: "safe", label: "Місія минула без поранень", effects: [
        { op: "set_flag", key: "mission_done", value: true },
        { op: "set_flag", key: "arthur_injured", value: false }
      ] }
    ]
  },
  {
    id: "pager_request",
    title: "Повідомлення на пейджері",
    description: "Система пейджера реагує на завершення місії, незалежно від локації.",
    priority: 90,
    once: true,
    when: { op: "flag", key: "mission_done", value: true },
    choices: [
      { id: "read", label: "Прочитати повідомлення Летті", effects: [
        { op: "set_flag", key: "pager_read", value: true }
      ] }
    ]
  },
  {
    id: "treat_arthur",
    title: "Летті лікує Артура",
    description: "З'являється лише при пораненні Артура, коли гравець у медвідділі.",
    priority: 80,
    once: true,
    when: { all: [
      { op: "flag", key: "arthur_injured", value: true },
      { op: "eq", path: "location", value: "medbay" }
    ] },
    choices: [
      { id: "help", label: "Допомогти Летті", effects: [
        { op: "set_flag", key: "arthur_treated", value: true },
        { op: "set_flag", key: "arthur_injured", value: false },
        { op: "inc", path: "relationships.lettie", by: 5 }
      ] }
    ]
  },
  {
    id: "cafe_followup",
    title: "Розмова в кав'ярні",
    description: "Потребує прочитаного пейджера, лікування та локації кав'ярні.",
    priority: 70,
    once: true,
    when: { all: [
      { op: "flag", key: "pager_read", value: true },
      { op: "flag", key: "arthur_treated", value: true },
      { op: "eq", path: "location", value: "cafe" }
    ] },
    choices: [
      { id: "talk", label: "Поговорити з Летті", effects: [
        { op: "set_flag", key: "lettie_confided", value: true },
        { op: "inc", path: "relationships.lettie", by: 2 }
      ] }
    ]
  },
  {
    id: "lettie_new_topic",
    title: "Нова особиста тема",
    description: "Відкривається, коли у Летті достатньо довіри або гравець мав особисту розмову.",
    priority: 60,
    once: true,
    when: { any: [
      { op: "gte", path: "relationships.lettie", value: 7 },
      { op: "flag", key: "lettie_confided", value: true }
    ] },
    choices: [
      { id: "listen", label: "Вислухати", effects: [
        { op: "set_flag", key: "lettie_topic_done", value: true }
      ] }
    ]
  }
];