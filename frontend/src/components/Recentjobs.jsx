import { useEffect, useState } from "react";
import api from "../services/api";

export default function RecentJobs() {
  const [jobs, setJobs] = useState([]);

  useEffect(() => {
    fetchJobs();

    const interval = setInterval(fetchJobs, 1000);

    return () => clearInterval(interval);
  }, []);

  const fetchJobs = async () => {
    try {
      const res = await api.get("/jobs/");
      setJobs(res.data);
    } catch (err) {
      console.error(err);
    }
  };

  const badge = (status) => {
    const colors = {
      Completed: "bg-green-500/20 text-green-400",
      Running: "bg-blue-500/20 text-blue-400",
      Waiting: "bg-gray-500/20 text-gray-400",
      Failed: "bg-red-500/20 text-red-400",
    };

    return (
      <span
        className={`px-2 py-1 rounded-full text-xs font-semibold ${
          colors[status] || "bg-yellow-500/20 text-yellow-400"
        }`}
      >
        {status}
      </span>
    );
  };

  return (
    <div className="mt-12 bg-slate-900 rounded-2xl border border-slate-700 p-6 overflow-x-auto">
      <h2 className="text-2xl font-semibold mb-6">
        Recent Jobs
      </h2>

      <table className="w-full text-sm">
        <thead>
          <tr>
            <th className="text-left pb-4">Video</th>
            <th className="text-left pb-4">Pipeline</th>
            <th className="text-left pb-4">Audio</th>
            <th className="text-left pb-4">Speech</th>
            <th className="text-left pb-4">Summary</th>
            <th className="text-left pb-4">SEO</th>
            <th className="text-left pb-4">Hooks</th>
          </tr>
        </thead>

        <tbody>
          {jobs.map((job) => (
            <tr
              key={job.id}
              className="border-t border-slate-800"
            >
              <td className="py-4">
                {job.video.split("/").pop()}
              </td>

              <td className="py-4">
                {badge(job.status)}
              </td>

              <td className="py-4">
                {badge(job.audio_status)}
              </td>

              <td className="py-4">
                {badge(job.speech_status)}
              </td>

              <td className="py-4">
                {badge(job.summary_status)}
              </td>

              <td className="py-4">
                {badge(job.seo_status)}
              </td>

              <td className="py-4">
                {badge(job.hook_status)}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}