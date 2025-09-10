import { useState, ChangeEvent } from "react";

interface Props {
  onChange: (file: File | null) => void;
}

export default function UploadBox({ onChange }: Props) {
  const [preview, setPreview] = useState<string | null>(null);

  const handleFile = (e: ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0] ?? null;
    if (file) {
      const url = URL.createObjectURL(file);
      setPreview(url);
    } else {
      setPreview(null);
    }
    onChange(file);
  };

  return (
    <div className="border-2 border-dashed rounded p-4 text-center">
      <input type="file" accept="image/*" onChange={handleFile} />
      {preview && <img src={preview} alt="preview" className="mt-4 mx-auto max-h-60" />}
    </div>
  );
}
