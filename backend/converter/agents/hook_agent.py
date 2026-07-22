import time
import json
import re


def generate_hooks(job):

    job.status = "Generating Hooks"

    job.hook_status = "Running"
    job.save()

    print("🎣 Hook Agent Started")

    time.sleep(1)

    summary = job.summary or ""

    words = re.findall(r"\b[a-zA-Z]{5,}\b", summary.lower())

    keywords = []

    for word in words:
        if word not in keywords:
            keywords.append(word)

    k1 = keywords[0] if len(keywords) > 0 else "success"
    k2 = keywords[1] if len(keywords) > 1 else "leadership"
    k3 = keywords[2] if len(keywords) > 2 else "growth"
    k4 = keywords[3] if len(keywords) > 3 else "mindset"
    k5 = keywords[4] if len(keywords) > 4 else "innovation"

    hooks = [
        f"Why is everyone talking about {k1}?",
        f"The hidden truth about {k2} nobody tells you",
        f"How {k3} can completely change your results",
        f"This simple {k4} shift can transform your life",
        f"What most people misunderstand about {k5}"
    ]

    job.hook_result = json.dumps(hooks, indent=2)

    job.hook_status = "Completed"
    job.save()

    print("✅ Hook Agent Finished")

    return hooks