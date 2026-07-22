def generate_summary(job, transcript):

    job.status = "Summarizing"
    job.summary_status = "Running"
    job.save()

    print("🧠 Summary Agent Started")

    prompt = f"""
You are an expert AI video summarizer.

Summarize the following transcript into 5-8 concise bullet points.

Transcript:
{transcript}
"""

    response = client.models.generate_content(
        model="models/gemini-3.6-flash",
        contents=prompt,
    )

    summary = response.text

    job.summary = summary
    job.summary_status = "Completed"

    job.save()

    print("✅ Summary Generated")

    return summary