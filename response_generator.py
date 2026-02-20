from datetime import datetime

def generate_response(intent):

    if intent == "greeting":
        return "नमस्ते! मैं तैयार हूँ।"

    elif intent == "time":
        now = datetime.now().strftime("%H:%M")
        return f"अभी समय {now} है।"

    elif intent == "date":
        today = datetime.now().strftime("%d %B %Y")
        return f"आज की तारीख {today} है।"

    elif intent == "help":
        return "आप समय, तारीख, या बंद बोल सकते हैं।"

    elif intent == "thanks":
        return "आपका स्वागत है।"

    elif intent == "name":
        return "मैं आपका ऑफलाइन वॉइस असिस्टेंट हूँ।"

    elif intent == "status":
        return "सिस्टम सही काम कर रहा है।"

    elif intent == "audio":
        return "आवाज़ ठीक से आ रही है।"

    elif intent == "start":
        return "मैं सुन रही हूँ।"

    elif intent == "pause":
        return "रुकी हूँ।"

    elif intent == "repeat":
        return "कृपया फिर से बोलिए।"

    elif intent == "clear":
        return "साफ़ किया गया।"

    elif intent == "location":
        return "आपका सिस्टम लोकल मोड में चल रहा है।"

    elif intent == "ok":
        return "ठीक है।"

    elif intent == "exit":
        return "अलविदा।"
    else:
        return "समझ नहीं आया।"
