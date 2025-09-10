interface Props {
  value: string;
  onChange: (v: string) => void;
  placeholder?: string;
}

export default function PromptInput({ value, onChange, placeholder }: Props) {
  return (
    <input
      type="text"
      className="w-full p-3 rounded border bg-gray-800"
      value={value}
      onChange={e => onChange(e.target.value)}
      placeholder={placeholder}
    />
  );
}
