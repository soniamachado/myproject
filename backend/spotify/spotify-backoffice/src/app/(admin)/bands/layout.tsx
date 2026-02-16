import { ReactNode } from "react";

interface Props {
  children: ReactNode;
}
export default function Layout({ children }: Props) {
  return (
    <div className="w-full max-w-7xl mx-auto px-4 py-6 space-y-6">
      <h1>Bands Layout</h1>
      {children}
    </div>
  );
}
