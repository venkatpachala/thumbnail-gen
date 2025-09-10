import { useRouter } from "next/router";
import ThumbnailPreview from "../components/ThumbnailPreview";

export default function Preview() {
  const router = useRouter();
  const { src } = router.query;

  const handleDownload = () => {
    if (typeof src === "string") {
      const link = document.createElement("a");
      link.href = src;
      link.download = "thumbnail.png";
      link.click();
    }
  };

  return (
    <div className="min-h-screen flex flex-col items-center p-6">
      <h1 className="text-3xl font-bold mb-6">Preview</h1>
      <ThumbnailPreview src={typeof src === "string" ? src : null} onDownload={handleDownload} />
      <div className="mt-4 flex gap-2">
        <button onClick={() => router.back()} className="px-4 py-2 bg-gray-700 rounded">Try Again</button>
      </div>
    </div>
  );
}
