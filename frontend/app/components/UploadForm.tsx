"use client";

import { useState } from "react";
import axios from "axios";

export default function UploadForm() {

  const [before, setBefore] = useState<File | null>(null);
  const [after, setAfter] = useState<File | null>(null);
  const [video, setVideo] = useState<string | null>(null);
  const [status, setStatus] = useState("");

  const uploadImages = async () => {

    if (!before || !after) {
      alert("Please upload both images");
      return;
    }

    const formData = new FormData();
    formData.append("before", before);
    formData.append("after", after);

    try {

      setStatus("Processing civic update...");

      const response = await axios.post(
        "http://127.0.0.1:8000/upload",
        formData
      );

      setStatus(response.data.status);
      setVideo(response.data.video);

    } catch (error) {

      setStatus("Error generating update");

    }

  };

  return (

    <div className="bg-white p-6 rounded-xl shadow-md w-[400px]">

      <h2 className="text-xl font-bold mb-4">
        OmniWard AI Dashboard
      </h2>

      <input
        type="file"
        onChange={(e) => setBefore(e.target.files?.[0] || null)}
      />

      <br/><br/>

      <input
        type="file"
        onChange={(e) => setAfter(e.target.files?.[0] || null)}
      />

      <br/><br/>

      <button
        onClick={uploadImages}
        className="bg-blue-500 text-white px-4 py-2 rounded"
      >
        Generate Civic Update
      </button>

      <p className="mt-4">{status}</p>

      {video && (
        <video
          controls
          className="mt-4 w-full"
          src={`http://127.0.0.1:8000/${video}`}
        />
      )}

    </div>
  );
}