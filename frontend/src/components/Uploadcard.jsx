import { useRef, useState } from "react";
import axios from "axios";

export default function UploadCard() {
  const fileRef = useRef(null);
  const [file, setFile] = useState(null);

  const chooseFile = () => {
    fileRef.current.click();
  };

  const upload = async () => {
    if (!file) {
      alert("Choose a video first");
      return;
    }

    const formData = new FormData();
    formData.append("video", file);

    try {
      const res = await axios.post(
        "http://127.0.0.1:8000/api/upload/",
        formData
      );

      alert(`Uploaded Job #${res.data.id}`);
    } catch (err) {
      console.error(err);
      alert("Upload failed");
    }
  };

  return (
    <div className="mt-12 bg-slate-900 border border-slate-700 rounded-3xl p-12 text-center">

      <div className="text-6xl">
        🎬
      </div>

      <h2 className="text-2xl font-semibold mt-5">
        Upload Video
      </h2>

      <p className="text-gray-400 mt-2">
        Select an MP4, MOV, or AVI file
      </p>

      <input
        hidden
        type="file"
        accept="video/*"
        ref={fileRef}
        onChange={(e) => setFile(e.target.files[0])}
      />

      <button
        onClick={chooseFile}
        className="mt-6 bg-indigo-600 hover:bg-indigo-700 px-6 py-3 rounded-xl"
      >
        Choose Video
      </button>

      {file && (
        <p className="mt-4 text-green-400">
          Selected: {file.name}
        </p>
      )}

      <button
        onClick={upload}
        className="mt-6 ml-4 bg-green-600 hover:bg-green-700 px-6 py-3 rounded-xl"
      >
        Upload
      </button>
    </div>
  );
}