import time
import json
import re


def generate_seo(job):

    job.status = "SEO Analysis"
    job.seo_status = "Running"
    job.save()

    print("📈 SEO Agent Started")

    time.sleep(1)

    summary = job.summary or ""

    if not summary:
        seo_data = {
            "title": "No Summary Available",
            "description": "",
            "keywords": []
        }
    else:
        # Title = first meaningful sentence
        title = summary.split(".")[0][:70]

        # Description
        description = summary[:250]

        # Keyword extraction
        words = re.findall(r"\b[a-zA-Z]{5,}\b", summary.lower())

        stopwords = {
            "about", "their", "there", "which", "while",
            "these", "those", "would", "could", "should",
            "people", "video", "using", "other", "through",
            "because", "where", "when", "after", "before"
        }

        keywords = []

        for word in words:
            if word not in stopwords and word not in keywords:
                keywords.append(word)

        seo_data = {
            "title": title,
            "description": description,
            "keywords": keywords[:10]
        }

    job.seo_result = json.dumps(seo_data, indent=2)

    job.seo_status = "Completed"
    job.save()

    print("✅ SEO Agent Finished")

    return seo_data