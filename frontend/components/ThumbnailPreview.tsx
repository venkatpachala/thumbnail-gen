interface Props {
  src: string | null;
  onDownload?: () => void;
}

export default function ThumbnailPreview({ src, onDownload }: Props) {
  if (!src) return null;
  return (
    <div className="mt-6">
      <img src={src} alt="thumbnail" className="border w-full max-w-3xl" />
      <div className="mt-4 flex gap-2">
        <button onClick={onDownload} className="px-4 py-2 bg-blue-600 rounded">Download</button>
      </div>
    </div>
  );
}
