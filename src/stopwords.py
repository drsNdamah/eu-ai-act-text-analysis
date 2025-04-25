# src/stopwords.py
from wordcloud import STOPWORDS

def get_custom_stopwords():
    additional = {
    "abovementione", "include", "refer", "overview", "verifie", "signature", "alternatively", "taxonomy", "perspective",
    "established", "server", "theft", "leakage", "accidental", "unknown", "unsuitability", "tcn", "ecris",
    "conviction", "reform", "series", "en", "candidate", "duplicate", "incoming", "chatbot",
    "railway", "metro", "bus", "stadium", "gym", "swimming", "hospitality", "cafés", "restaurant", "shop",
    "sequence", "token", "criteria", "brief", "flag", "fourth", "smart", "layer", "neutral",
    "normally", "encouraged", "contemplate", "certifier", "directives", "eea", "scanned", "optional",
    "rape", "organised", "armed", "robbery", "sabotage", "biometrics", "steer",
    "tissue", "organ", "injury", "bodily", "head", "arm", "smile", "frown", "apparent", "issuing", "outlier",
    "clean", "supervised", "datasheet", "layout", "show", "illustration", "photograph", "package", "firmware",
    "radioactive", "grievous", "murder", "munition", "strong", "adjust", "continuously", "difficult", "valuable",
    "compute", "upfront", "planning", "commonly", "barriers", "mind", "evolution", "quick",
    "observance", "mitigating", "window", "teaming", "red", "interpreting", "irregular", "ship", "seizure",
    "hostage", "restraint", "kidnapping", "psychotropic", "drug", "pornography", "terrorism", "proceed",
    "required", "archive", "holder", "underpin", "want", "misinformation", "hard", "preference", "maximise",
    "correspond", "keyword", "guardrail", "combined", "false", "discourage",
    "audits", "asse", "upgrade", "marked", "cancel", "preliminary", "negligently", "intentionally",
    "complainant", "character", "delegated", "message", "mere", "driver", "pilot", "watermark", "trace",
    "manipulation", "pain", "amusement", "satisfaction", "contempt", "shame", "excitement", "embarrassment",
    "disgust", "surprise", "anger", "unmanned", "propeller", "negligent", "aggravating",
    "percentage", "reply", "viability", "revocation", "whispering", "sadness", "happiness",
    "television", "domain", "city", "circulation", "divergence", "import", "cryptographic", "metadata",
    "diverge", "circulate", "obstacle", "watercraft", "michel", "metsola", "brussels", "twentieth", "inclusion",
    "exclusive", "handle", "formal", "prescribed", "misclassifie", "disagreement", "forward", "undisclosed",
    "multilateral", "bilateral", "clearance", "close", "insight", "doctor", "chemical", "predictor",
    "primarily", "generating", "regions", "conclusions", "mix", "terminal", "storing", "participative",
    "oppose", "tacitly", "encouraging", "similarity"
    }
    return set(STOPWORDS).union(additional)
