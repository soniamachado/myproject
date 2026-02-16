import { ReactNode } from "react";

interface Props {
  children: ReactNode;
}
export default function Layout({ children }: Props) {
  return (
    <div className="border-4 border-blue-800">
      <h1>Tracks Layout</h1>
      {children}
    </div>
  );
}
