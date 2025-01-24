from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def emojifier(input_text):
    # Sentiment analysis using VADER
    analyzer = SentimentIntensityAnalyzer()
    sentiment_score = analyzer.polarity_scores(input_text)['compound']

    # Mapping sentiments to emojis
    if sentiment_score > 0.5:
        sentiment_emoji = "😁🎉"
    elif 0 < sentiment_score <= 0.5:
        sentiment_emoji = "😊👍"
    elif sentiment_score == 0:
        sentiment_emoji = "😐"
    elif -0.5 < sentiment_score < 0:
        sentiment_emoji = "😕"
    else:
        sentiment_emoji = "😢"

    # Lexical mapping
    word_to_emoji = {
        "Python": "🐍💻",
        "happy": "😄",
        "sad": "😢",
        "love": "❤️",
        "music": "🎵",
        "food": "🍔🍕",
        "animals": "🐶🐱",
        "sun": "☀️",
        "rain": "🌧️",
        "books": "📚",
        "television": "📺",
        "vacation": "🏖️",
        "game": "🎮",
        "sports": "🏃‍♂️⚽",
        "sea": "🌊",
        "mountain": "⛰️",
        "snowy": "❄️",
        "night": "🌙",
        "day": "🌞",
        "shopping": "🛒",
        "travel": "✈️🌍",
        "home": "🏠",
        "party": "🎉",
        "coffee": "☕",
        "movie": "🎬",
        "sound": "🔊",
        "lesson": "📖",
        "happiness": "😊",
        "laughter": "😂",
        "children": "👶👦👧",
        "friends": "👯‍♂️",
        "dance": "💃🕺",
        "nature": "🌱🌳",
        "space": "🌌",
        "software": "💻",
        "star": "🌟",
        "family": "👨‍👩‍👧‍👦",
        "wedding": "💍",
        "video": "🎥",
        "heart": "💓",
        "fish": "🐟",
        "water": "💧",
        "fire": "🔥",
        "competition": "🏆",
        "victory": "🥇",
        "call": "📞",
        "ship": "🚢",
        "car": "🚗",
        "bicycle": "🚲",
        "taxi": "🚖",
        "train": "🚆",
        "library": "🏛️",
        "hospital": "🏥",
        "police": "👮",
        "lawyer": "⚖️",
        "airplane": "✈️",
        "building": "🏢",
        "bus": "🚌",
        "summer": "🌞",
        "winter": "❄️",
        "spring": "🌸",
        "autumn": "🍂",
        "wind": "🌬️",
        "table": "🍽️",
        "chair": "🪑",
        "bed": "🛏️",
        "restaurant": "🍴",
        "cafe": "☕",
        "drink": "🍸",
        "center": "🏙️",
        "village": "🏘️",
        "paradise": "🌴",
        "castle": "🏰",
        "palace": "🏯",
        "church": "⛪",
        "smoke": "🚬",
        "shop": "🏪",
        "bank": "💳",
        "money": "💰",
        "soccer": "⚽",
        "basketball": "🏀",
        "tennis": "🎾",
        "luxury": "💎",
        "mystery": "🕵️‍♂️",
        "horror": "👻",
        "transportation": "🚚",
        "mission": "📦",
        "system": "💻",
        "action": "💥",
        "game_card": "🃏",
        "guidance": "🧭",
        "poster": "📜",
        "entertainment": "🎭",
        "festival": "🎉",
        "competition": "🏅",
        "performance": "🎤",
        "theater": "🎭",
        "programming": "🖥️",
        "computer": "💻",
        "copy": "📄",
        "edit": "✂️",
        "kindness": "🤗",
        "courtesy": "🤝",
        "climate": "🌡️",
        "air": "🍃",
        "sound_music": "🎶",
        "rest": "🛌",
        "good_luck": "🍀",
        "gratitude": "🙏",
        "loneliness": "😔",
        "hospitality": "🏡",
        "intensity": "💥",
    }

    # Create the new sentence with emojis
    words = input_text.split()
    emojified_text = " ".join([word + (" " + word_to_emoji[word] if word in word_to_emoji else "") for word in words])

    # Add sentiment emojis at the end
    emojified_text += f" {sentiment_emoji}"

    return emojified_text

# Example usage
if __name__ == "__main__":
    print("Welcome to Emojifier AI! Enter a sentence and we will convert it.")
    while True:
        user_input = input("Enter your sentence: ")
        result = emojifier(user_input)
        print(f"Converted: {result}")
