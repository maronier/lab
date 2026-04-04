from dataclasses import dataclass


@dataclass(frozen=True)
class Profile:
    tone_depth: str
    undertone: str
    skin_type: str


SHADE_MAP = {
    "light": {
        "cool": ["светло-розовый", "розово-лиловый"],
        "warm": ["персиковый", "абрикосовый"],
        "neutral": ["нежно-розовый", "розово-персиковый"],
    },
    "medium": {
        "cool": ["роза", "ягодно-розовый"],
        "warm": ["тёплый персик", "коралл"],
        "neutral": ["розово-коралловый", "пыльная роза"],
    },
    "deep": {
        "cool": ["малина", "сливовый", "ягодный"],
        "warm": ["терракота", "кирпично-коралловый", "мандариновый"],
        "neutral": ["насыщенная роза", "глубокий коралл"],
    },
}

TEXTURE_MAP = {
    "dry": "кремовые или стиковые румяна",
    "oily": "пудровые или запечённые румяна",
    "combo": "легкие пудровые или гибридные текстуры",
    "normal": "подойдёт любая текстура — ориентируйтесь на финиш",
}


def recommend(profile: Profile) -> dict:
    shades = SHADE_MAP[profile.tone_depth][profile.undertone]
    texture = TEXTURE_MAP[profile.skin_type]
    return {
        "shades": shades,
        "texture": texture,
        "application": "Наносите понемногу на яблочки щёк и растушёвывайте к вискам.",
    }


def ask_choice(title: str, options: dict) -> str:
    print(f"\n{title}")
    for key, label in options.items():
        print(f"  {key} — {label}")

    while True:
        value = input("Ваш выбор: ").strip().lower()
        if value in options:
            return value
        print("Не понял выбор. Попробуйте ещё раз.")


def main() -> None:
    print("💄 Mini demo: подбор цвета румян по типу кожи")

    tone_depth = ask_choice(
        "1) Глубина тона кожи:",
        {
            "light": "светлая",
            "medium": "средняя",
            "deep": "смуглая/тёмная",
        },
    )

    undertone = ask_choice(
        "2) Подтон:",
        {
            "warm": "тёплый",
            "cool": "холодный",
            "neutral": "нейтральный",
        },
    )

    skin_type = ask_choice(
        "3) Тип кожи:",
        {
            "dry": "сухая",
            "oily": "жирная",
            "combo": "комбинированная",
            "normal": "нормальная",
        },
    )

    result = recommend(Profile(tone_depth=tone_depth, undertone=undertone, skin_type=skin_type))

    print("\n✨ Ваша персональная рекомендация")
    print(f"Оттенки: {', '.join(result['shades'])}")
    print(f"Текстура: {result['texture']}")
    print(result["application"])


if __name__ == "__main__":
    main()
