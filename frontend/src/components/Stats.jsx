import { useEffect, useState } from "react";
import api from "../services/api";

export default function Stats() {
  const [stats, setStats] = useState({
    uploads: 0,
    processing: 0,
    completed: 0,
  });

  useEffect(() => {
    fetchStats();
  }, []);

  const fetchStats = async () => {
    const res = await api.get("/jobs/");

    const jobs = res.data;

    setStats({
      uploads: jobs.length,
      processing: jobs.filter(
        (job) => job.status === "Processing"
      ).length,

      completed: jobs.filter(
        (job) => job.status === "Completed"
      ).length,
    });
  };

  return (
    <div className="grid grid-cols-3 gap-6 mt-10">

      <div className="bg-slate-900 p-6 rounded-2xl border border-slate-700">
        <h3 className="text-gray-400">Uploads</h3>
        <p className="text-3xl font-bold mt-2">
          {stats.uploads}
        </p>
      </div>

      <div className="bg-slate-900 p-6 rounded-2xl border border-slate-700">
        <h3 className="text-gray-400">Processing</h3>
        <p className="text-3xl font-bold mt-2 text-yellow-400">
          {stats.processing}
        </p>
      </div>

      <div className="bg-slate-900 p-6 rounded-2xl border border-slate-700">
        <h3 className="text-gray-400">Completed</h3>
        <p className="text-3xl font-bold mt-2 text-green-400">
          {stats.completed}
        </p>
      </div>

    </div>
  );
}