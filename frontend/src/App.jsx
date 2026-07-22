import Navbar from "./components/Navbar";
import Hero from "./components/Hero";
import UploadCard from "./components/UploadCard";
import Stats from "./components/Stats";
import RecentJobs from "./components/RecentJobs";

export default function App() {
  return (
    <div className="min-h-screen bg-slate-950 text-white">

      <Navbar />

      <div className="max-w-6xl mx-auto px-6">

        <Hero />

        <UploadCard />

        <Stats />

        <RecentJobs />

      </div>

    </div>
  );
}