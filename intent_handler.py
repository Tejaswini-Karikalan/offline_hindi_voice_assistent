def get_intent(text):
    text = text.strip()

    if "नमस्ते" in text:
        return "greeting"

    elif "समय" in text:
        return "time"

    elif "तारीख" in text:
        return "date"

    elif "मदद" in text:
        return "help"

    elif "बंद" in text:
        return "exit"

    elif "धन्यवाद" in text:
        return "thanks"

    elif "नाम" in text:
        return "name"

    elif "स्थिति" in text:
        return "status"

    elif "आवाज़" in text:
        return "audio"

    elif "शुरू" in text:
        return "start"

    elif "रुको" in text:
        return "pause"

    elif "दोहराओ" in text:
        return "repeat"

    elif "साफ" in text:
        return "clear"

    elif "कहाँ" in text:
        return "location"

    elif "ठीक" in text:
        return "ok"

    else:
        return "unknown"
