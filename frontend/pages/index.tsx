import { useState } from "react";
import UploadBox from "../components/UploadBox";
import PromptInput from "../components/PromptInput";
import Loader from "../components/Loader";
import axios from "axios";
import { useRouter } from "next/router";

export default function Home() {
  const [file, setFile] = useState<File | null>(null);
  const [prompt, setPrompt] = useState("");
  const [text, setText] = useState("");
  const [loading, setLoading] = useState(false);
  const router = useRouter();

  const handleGenerate = async () => {
    if (!file) return;
    setLoading(true);
    try {
      const fd = new FormData();
      fd.append("file", file);
      const cutoutRes = await axios.post(`${process.env.NEXT_PUBLIC_API_URL}/cutout-photo`, fd, {
        headers: { "Content-Type": "multipart/form-data" },
      });
      const cutoutPath = cutoutRes.data.cutout;

      const bgRes = await axios.post(`${process.env.NEXT_PUBLIC_API_URL}/generate-background`, { prompt });
      const bgPath = bgRes.data.background;

      const composeRes = await axios.post(`${process.env.NEXT_PUBLIC_API_URL}/compose-thumbnail`, {
        background: bgPath,
        cutout: cutoutPath,
        text,
      });
      const thumb = composeRes.data.thumbnail;
      router.push(`/preview?src=${encodeURIComponent(thumb)}`);
    } catch (err) {
      console.error(err);
      alert("Generation failed");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex flex-col items-center p-6">
      <h1 className="text-3xl font-bold mb-6">Generate Stunning Thumbnails with AI</h1>
      <div className="w-full max-w-3xl grid md:grid-cols-2 gap-4">
        <UploadBox onChange={setFile} />
        <div className="flex flex-col gap-4">
          <PromptInput value={prompt} onChange={setPrompt} placeholder="Background prompt" />
          <PromptInput value={text} onChange={setText} placeholder="Overlay text" />
          <button onClick={handleGenerate} className="px-4 py-2 bg-green-600 rounded">Generate</button>
          {loading && <Loader />}
        </div>
      </div>
    </div>
  );
}
